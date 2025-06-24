#!/bin/bash
echo "[*] Starting BugHunter Automation..."
domain=$1
if [ -z "$domain" ]; then
    echo "Usage: ./run.sh target.com"
    exit 1
fi
python3 cli.py $domain --all