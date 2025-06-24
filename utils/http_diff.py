# core/http_diff.py

import difflib
import requests

def run(domain):
    print(f"[HTTP Diff] Running HTTP diff on {domain}...")

    # Define two variations of the request
    url_1 = f"http://{domain}/test?role=user"
    url_2 = f"http://{domain}/test?role=admin"

    try:
        response_1 = requests.get(url_1, timeout=10)
        response_2 = requests.get(url_2, timeout=10)

        diff = difflib.unified_diff(
            response_1.text.splitlines(),
            response_2.text.splitlines(),
            fromfile='user',
            tofile='admin',
            lineterm=''
        )

        print("\n".join(diff) or "[HTTP Diff] No significant difference found.")

    except Exception as e:
        print(f"[HTTP Diff] Error: {e}")

    print("[HTTP Diff] Scan complete.")

