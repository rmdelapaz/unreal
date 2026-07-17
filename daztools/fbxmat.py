"""Minimal binary-FBX reader: walk the node tree and dump Material property values."""
import struct
import sys
import zlib

path = sys.argv[1] if len(sys.argv) > 1 else r"D:\mydata\3dassets\amy2.fbx"
buf = open(path, "rb").read()
version = struct.unpack("<I", buf[23:27])[0]
wide = version >= 7500
print("FBX version:", version, " 64-bit offsets:", wide)

HDR = struct.Struct("<QQQB") if wide else struct.Struct("<IIIB")


def read_prop(b, o):
    t = chr(b[o]); o += 1
    if t == "Y": return struct.unpack_from("<h", b, o)[0], o + 2
    if t == "C": return bool(b[o]), o + 1
    if t == "I": return struct.unpack_from("<i", b, o)[0], o + 4
    if t == "F": return struct.unpack_from("<f", b, o)[0], o + 4
    if t == "D": return struct.unpack_from("<d", b, o)[0], o + 8
    if t == "L": return struct.unpack_from("<q", b, o)[0], o + 8
    if t in "fdlib":
        n, enc, cl = struct.unpack_from("<III", b, o); o += 12
        raw = b[o:o + cl]; o += cl
        if enc == 1:
            try: raw = zlib.decompress(raw)
            except Exception: return "<array>", o
        fmt = {"f": "f", "d": "d", "l": "q", "i": "i", "b": "b"}[t]
        try: return list(struct.unpack("<" + fmt * n, raw[:n * struct.calcsize(fmt)])), o
        except Exception: return "<array>", o
    if t in "SR":
        ln = struct.unpack_from("<I", b, o)[0]; o += 4
        v = b[o:o + ln]; o += ln
        return (v.decode("utf-8", "ignore") if t == "S" else "<raw%d>" % ln), o
    raise ValueError("bad prop type %r at %d" % (t, o))


def walk(b, start, end, depth, path_names, out):
    o = start
    while o < end:
        if o + HDR.size > len(b): return
        endoff, nprops, plen, nlen = HDR.unpack_from(b, o)
        o2 = o + HDR.size
        if endoff == 0: return
        name = b[o2:o2 + nlen].decode("utf-8", "ignore"); o2 += nlen
        props = []
        p = o2
        for _ in range(nprops):
            try:
                v, p = read_prop(b, p)
            except Exception:
                break
            props.append(v)
        here = path_names + [name]
        if name == "Material":
            mat = next((x for x in props if isinstance(x, str) and x), "?")
            out.append(("MAT", mat.split("\x00")[0], []))
        if name == "P" and out and props:
            key = props[0] if isinstance(props[0], str) else "?"
            vals = [x for x in props[4:]]
            if key in ("DiffuseColor", "DiffuseFactor", "SpecularColor", "SpecularFactor",
                       "Shininess", "ShininessExponent", "ReflectionFactor", "AmbientColor",
                       "TransparencyFactor", "Emissive", "Opacity", "Specular", "Diffuse",
                       "Ambient", "Reflectivity", "Bump", "NormalMap"):
                out[-1][2].append((key, vals))
        walk(b, o2 + plen, endoff, depth + 1, here, out)
        o = endoff


out = []
walk(buf, 27, len(buf), 0, [], out)
print("materials found:", len(out))
seen = set()
for kind, name, props in out:
    if not props or name in seen:
        continue
    seen.add(name)
    if not any(k in name for k in ("Head", "Body", "Arms", "Legs", "Hair", "Bra", "Undies", "Eye")):
        continue
    print("\n---", name)
    for k, v in props:
        vv = [round(x, 4) if isinstance(x, float) else x for x in v]
        print("     %-20s %s" % (k, vv))

# --- emit a machine-readable map of every material's Daz surface values ---
import json
m = {}
for kind, name, props in out:
    if not props:
        continue
    d = dict(props)
    clean = name.split("\x00")[0].strip()
    if clean in m:
        continue
    rec = {}
    if "DiffuseColor" in d and len(d["DiffuseColor"]) == 3:
        rec["diffuse"] = [round(v, 4) for v in d["DiffuseColor"]]
    if "Specular" in d and len(d["Specular"]) == 3:
        rec["specular"] = round(sum(d["Specular"]) / 3.0, 4)
    if "Shininess" in d and d["Shininess"]:
        rec["shininess"] = d["Shininess"][0]
    if rec:
        m[clean] = rec
open("daz_materials.json", "w").write(json.dumps(m, indent=1))
print("\n\n=== wrote daz_materials.json : %d materials ===" % len(m))
for k, v in sorted(m.items()):
    print("  %-32s %s" % (k, v))
