#!/usr/bin/env python3
"""Commits android/keystore/readzen.keystore.b64 to readori/readzen via GitHub API."""
import json
import base64
import urllib.request
import urllib.error
import os
import sys

def main():
    pat = os.environ.get("READZEN_PAT", "")
    print("PAT length:", len(pat))
    if not pat:
        print("ERROR: READZEN_PAT env var is empty")
        sys.exit(1)

    keystore_path = "/tmp/readzen.keystore"
    if not os.path.exists(keystore_path):
        print("ERROR: keystore file not found at", keystore_path)
        sys.exit(1)

    with open(keystore_path, "rb") as f:
        keystore_bytes = f.read()
    print("Keystore binary size:", len(keystore_bytes), "bytes")

    # readzen.keystore.b64 stores base64(binary keystore)
    file_content_text = base64.b64encode(keystore_bytes).decode("utf-8")
    print("Base64 content length:", len(file_content_text), "chars")

    # GitHub API content = base64(file bytes)
    api_content = base64.b64encode(file_content_text.encode("utf-8")).decode("utf-8")

    url = "https://api.github.com/repos/readori/readzen/contents/android/keystore/readzen.keystore.b64"
    payload = json.dumps({
        "message": "ci: commit stable keystore (readzen-release, RSA2048, valid 100yr)",
        "content": api_content
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, method="PUT")
    req.add_header("Authorization", "token " + pat)
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            html_url = result.get("content", {}).get("html_url", "committed")
            print("SUCCESS:", html_url)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print("HTTP ERROR", e.code, ":", body[:2000])
        sys.exit(1)
    except Exception as ex:
        print("UNEXPECTED ERROR:", str(ex))
        sys.exit(1)

if __name__ == "__main__":
    main()
