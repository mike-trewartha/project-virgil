#!/usr/bin/env python3
import os
import sys
import glob
import json
import yaml
from jsonschema import validate, ValidationError

SCHEMA_PATH = "templates/playbook_schema.json"
PLAYBOOKS_DIR = "playbooks/**/*.md"

def load_schema(schema_path):
    try:
        with open(schema_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"[-] Error loading schema: {e}")
        sys.exit(1)

def extract_frontmatter(filepath):
    """Extracts YAML frontmatter from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if not content.startswith("---"):
        return None
        
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
        
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        print(f"[-] YAML parsing error in {filepath}: {e}")
        return None

def main():
    print(f"[*] Loading schema from {SCHEMA_PATH}...")
    schema = load_schema(SCHEMA_PATH)
    
    playbook_files = glob.glob(PLAYBOOKS_DIR, recursive=True)
    if not playbook_files:
        print("[-] No playbooks found to validate.")
        sys.exit(1)
        
    print(f"[*] Found {len(playbook_files)} playbooks to validate.")
    
    errors = 0
    for filepath in playbook_files:
        frontmatter = extract_frontmatter(filepath)
        
        if not frontmatter:
            print(f"[!] SKIP: No valid YAML frontmatter found in {filepath}")
            continue
            
        try:
            validate(instance=frontmatter, schema=schema)
            print(f"[+] PASS: {filepath}")
        except ValidationError as e:
            print(f"[-] FAIL: {filepath}")
            print(f"    Reason: {e.message}")
            print(f"    Path: /{' / '.join([str(p) for p in e.path])}")
            errors += 1

    if errors > 0:
        print(f"\n[-] Validation failed with {errors} error(s).")
        sys.exit(1)
    else:
        print("\n[+] All playbooks passed schema validation.")
        sys.exit(0)

if __name__ == "__main__":
    main()
