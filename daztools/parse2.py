"""Robust extractor for CaptureViewport / CaptureAssetImage responses.

Handles both transports the MCP endpoint uses:
  * SSE  -> lines beginning "data:" that concatenate to one JSON doc
  * plain application/json
and both payload shapes (returnValue.image.data / returnValue.data).
Falls back to a raw base64 scan so a schema change can't break the shot.
"""
import base64
import json
import re
import sys

out = sys.argv[1]
raw = open("./_cap_raw.txt", encoding="utf-8", errors="replace").read()

chunks = [l[5:].strip() for l in raw.splitlines() if l.startswith("data:")]
payload = "".join(chunks) if chunks else raw

b64 = None
try:
    doc = json.loads(payload)
    text = doc["result"]["content"][0]["text"]     # inner JSON is a *string*
    rv = json.loads(text)["returnValue"]
    b64 = rv["image"]["data"] if "image" in rv else rv["data"]
except Exception:
    m = re.search(r'\\?"data\\?"\s*:\s*\\?"([A-Za-z0-9+/=]{500,})', payload)
    if m:
        b64 = m.group(1)

if not b64:
    print("NO IMAGE. head:", payload[:400])
    sys.exit(1)

png = base64.b64decode(b64)
open(out, "wb").write(png)
print("wrote %s  %d bytes" % (out, len(png)))
