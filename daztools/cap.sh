#!/bin/bash
# Capture the UE level viewport over the MCP HTTP endpoint and write a PNG.
# usage: cap.sh <outfile.png> <x> <y> <z> <pitch> <yaw>
OUT="$1"; X="$2"; Y="$3"; Z="$4"; P="$5"; YW="$6"
U="http://127.0.0.1:8000/mcp"
H_JSON="Content-Type: application/json"
H_ACC="Accept: application/json, text/event-stream"

SID=$(curl -s -D - -o /dev/null -X POST "$U" -H "$H_JSON" -H "$H_ACC" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"cap","version":"1"}}}' \
  | grep -i '^Mcp-Session-Id:' | sed 's/.*: *//' | tr -d '\r\n')

curl -s -X POST "$U" -H "$H_JSON" -H "$H_ACC" -H "Mcp-Session-Id: $SID" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}' > /dev/null

BODY=$(cat <<EOF
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"call_tool","arguments":{
"toolset_name":"EditorToolset.EditorAppToolset","tool_name":"CaptureViewport","arguments":{
"captureTransform":{"location":{"x":$X,"y":$Y,"z":$Z},"rotation":{"pitch":$P,"yaw":$YW,"roll":0},"scale":{"x":1,"y":1,"z":1}},
"annotations":{"gridSpacing":0,"gridExtent":0,"gridHeight":0,"maxLabelDistance":0,"classFilter":null,"maxLabels":0},
"bShowUI":false}}}}
EOF
)

curl -s --max-time 180 -X POST "$U" -H "$H_JSON" -H "$H_ACC" -H "Mcp-Session-Id: $SID" -d "$BODY" > ./_cap_raw.txt
PY_BIN=$(command -v python3 || command -v python)
"$PY_BIN" "$(dirname "$0")/parse2.py" "$OUT"; exit 0
cat >/dev/null <<PY
import sys, json, base64, re
raw = open('./_cap_raw.txt', encoding='utf-8', errors='replace').read()
chunks = []
for line in raw.splitlines():
    if line.startswith('data:'):
        chunks.append(line[5:].strip())
payload = ''.join(chunks) if chunks else raw
m = re.search(r'"data"\s*:\s*"([A-Za-z0-9+/=]{500,})"', payload)
if not m:
    print('NO IMAGE. head:', payload[:600]); sys.exit(1)
png = base64.b64decode(m.group(1))
open(sys.argv[1], 'wb').write(png)
print('wrote', sys.argv[1], len(png), 'bytes')
PY
