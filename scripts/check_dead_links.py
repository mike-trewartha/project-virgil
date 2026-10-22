#!/usr/bin/env python3
import re
import sys
import glob
import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress warnings for missing certs if we encounter weird redirects
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

PLAYBOOKS_DIR = "playbooks/**/*.md"
URL_REGEX = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s"\'\`\)]+')

def extract_urls(filepath):
    """Extracts all HTTP/HTTPS URLs from a file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return URL_REGEX.findall(content)

def check_url(url):
    """
    Checks if a URL is alive.
    Accepts 401/403 as ALIVE because platform security settings 
    naturally block unauthenticated requests.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        # Use a timeout so the CI script doesn't hang indefinitely
        response = requests.head(url, headers=headers, allow_redirects=True, timeout=10)
        
        if response.status_code == 405:
            # Fallback to GET if HEAD is not allowed
            response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
            
        # 404 is the primary indicator that an endpoint was deprecated
        if response.status_code == 404:
            return False, f"404 Not Found"
            
        # Treat 200s, redirects, and auth blocks (401/403) as valid
        return True, str(response.status_code)
        
    except requests.RequestException as e:
        return False, str(e)

def main():
    playbook_files = glob.glob(PLAYBOOKS_DIR, recursive=True)
    if not playbook_files:
        print("[-] No playbooks found.")
        sys.exit(1)
        
    print(f"[*] Scanning {len(playbook_files)} playbooks for URLs...\n")
    
    dead_links = []
    checked_urls = set() # Avoid checking the same URL multiple times
    
    for filepath in playbook_files:
        urls = extract_urls(filepath)
        for url in urls:
            if url in checked_urls:
                continue
                
            checked_urls.add(url)
            is_alive, status = check_url(url)
            
            if is_alive:
                print(f"[+] ALIVE ({status}): {url}")
            else:
                print(f"[-] DEAD  ({status}): {url} (Found in {filepath})")
                dead_links.append((filepath, url, status))

    print("\n" + "="*50)
    if dead_links:
        print(f"[-] Link check failed. Found {len(dead_links)} dead links:")
        for filepath, url, status in dead_links:
            print(f"    - {url} ({status}) [File: {filepath}]")
        sys.exit(1)
    else:
        print(f"[+] All {len(checked_urls)} unique URLs resolved successfully.")
        sys.exit(0)

if __name__ == "__main__":
    main()
