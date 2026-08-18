#!/usr/bin/env python3
"""Resumable upload into a Drive folder. The MCP connector cannot handle files
this size, so this goes straight at the Drive v3 resumable endpoint.

Usage: python3 drive_upload.py <folder_id> <path> [<path> ...]
"""
import json, mimetypes, os, sys, urllib.request, urllib.parse

CRED = os.path.expanduser("~/.gdocs_creds/slides_token.json")
CHUNK = 8 * 1024 * 1024


def access_token():
    c = json.load(open(CRED))
    body = urllib.parse.urlencode({
        "client_id": c["client_id"], "client_secret": c["client_secret"],
        "refresh_token": c["refresh_token"], "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body)
    return json.load(urllib.request.urlopen(req))["access_token"]


def upload(tok, folder, path):
    name = os.path.basename(path)
    size = os.path.getsize(path)
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    meta = json.dumps({"name": name, "parents": [folder]}).encode()
    req = urllib.request.Request(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable"
        "&supportsAllDrives=true",
        data=meta, method="POST",
        headers={"Authorization": "Bearer " + tok,
                 "Content-Type": "application/json; charset=UTF-8",
                 "X-Upload-Content-Type": mime,
                 "X-Upload-Content-Length": str(size)})
    session = urllib.request.urlopen(req).headers["Location"]

    sent = 0
    with open(path, "rb") as fh:
        while sent < size:
            buf = fh.read(CHUNK)
            end = sent + len(buf) - 1
            r = urllib.request.Request(
                session, data=buf, method="PUT",
                headers={"Content-Length": str(len(buf)),
                         "Content-Range": f"bytes {sent}-{end}/{size}"})
            try:
                resp = urllib.request.urlopen(r)
                out = json.load(resp)
                print(f"  {name}  DONE  id={out['id']}")
                return out["id"]
            except urllib.error.HTTPError as e:
                if e.code != 308:
                    raise
                sent = end + 1
                pct = 100 * sent / size
                print(f"  {name}  {pct:5.1f}%  ({sent/1e6:.0f} / {size/1e6:.0f} MB)",
                      flush=True)
    return None


if __name__ == "__main__":
    folder, paths = sys.argv[1], sys.argv[2:]
    tok = access_token()
    for p in paths:
        print(f"uploading {p} ({os.path.getsize(p)/1e6:.0f} MB)")
        upload(tok, folder, p)
