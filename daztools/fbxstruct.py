"""Walk a binary FBX and report Model/Geometry/Deformer structure + skeleton roots.

Answers: how many separate skeleton hierarchies does this file contain, and which
mesh nodes are skinned to which root?
"""
import struct
import sys
import zlib
from collections import Counter, defaultdict

path = sys.argv[1] if len(sys.argv) > 1 else r"D:\mydata\3dassets\guardsman.fbx"
buf = open(path, "rb").read()
version = struct.unpack("<I", buf[23:27])[0]
wide = version >= 7500
HDR = struct.Struct("<QQQB") if wide else struct.Struct("<IIIB")
print("FBX version:", version, "64-bit:", wide, "size:", len(buf))


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
            except Exception: return "<arr>", o
        fmt = {"f": "f", "d": "d", "l": "q", "i": "i", "b": "b"}[t]
        try: return list(struct.unpack("<" + fmt * n, raw[:n * struct.calcsize(fmt)])), o
        except Exception: return "<arr>", o
    if t in "SR":
        ln = struct.unpack_from("<I", b, o)[0]; o += 4
        v = b[o:o + ln]; o += ln
        return (v.decode("utf-8", "ignore") if t == "S" else "<raw%d>" % ln), o
    raise ValueError("bad prop %r" % t)


objects = {}   # uid -> (kind, name, subtype)
connections = []  # (child_uid, parent_uid)


def walk(b, start, end, stack):
    o = start
    while o < end:
        if o + HDR.size > len(b): return
        endoff, nprops, plen, nlen = HDR.unpack_from(b, o)
        if endoff == 0: return
        o2 = o + HDR.size
        name = b[o2:o2 + nlen].decode("utf-8", "ignore"); o2 += nlen
        props = []
        p = o2
        for _ in range(nprops):
            try:
                v, p = read_prop(b, p)
            except Exception:
                break
            props.append(v)

        if name in ("Model", "Geometry", "Deformer", "NodeAttribute") and len(props) >= 3:
            uid = props[0]
            nm = props[1].split("\x00")[0] if isinstance(props[1], str) else "?"
            sub = props[2] if isinstance(props[2], str) else "?"
            objects[uid] = (name, nm, sub)
        if name == "C" and len(props) >= 3:
            connections.append((props[1], props[2]))

        walk(b, o2 + plen, endoff, stack + [name])
        o = endoff


walk(buf, 27, len(buf), [])

kinds = Counter((k, s) for k, n, s in objects.values())
print("\n--- object counts by (node, subtype) ---")
for (k, s), n in sorted(kinds.items()):
    print("  %-14s %-16s %d" % (k, s, n))

# skeleton roots: Model/LimbNode or Model/Null whose parent is not a LimbNode
parent_of = {}
for c, p in connections:
    parent_of.setdefault(c, p)

limbs = {u for u, (k, n, s) in objects.items() if k == "Model" and s in ("LimbNode", "Limb")}
roots = []
for u in limbs:
    p = parent_of.get(u)
    if p not in limbs:
        roots.append(u)
print("\n--- skeleton roots (LimbNode whose parent is not a limb): %d ---" % len(roots))
for u in roots:
    print("   root bone:", objects[u][1], " parent:", objects.get(parent_of.get(u), ("-", "<scene>", "-"))[1])

# how many bones total, and name histogram for 'hip'
names = Counter(objects[u][1] for u in limbs)
print("\ntotal LimbNode bones:", len(limbs))
print("distinct bone names:", len(names))
dupes = {n: c for n, c in names.items() if c > 1}
print("bone names appearing MORE THAN ONCE:", len(dupes))
for n, c in sorted(dupes.items(), key=lambda x: -x[1])[:15]:
    print("   x%-3d %s" % (c, n))

# meshes
meshes = [(u, n) for u, (k, n, s) in objects.items() if k == "Geometry" and s == "Mesh"]
print("\n--- Geometry/Mesh nodes: %d ---" % len(meshes))
skins = {u for u, (k, n, s) in objects.items() if k == "Deformer" and s == "Skin"}
# geometry -> skin connection
children = defaultdict(list)
for c, p in connections:
    children[p].append(c)
skinned = 0
for u, n in sorted(meshes, key=lambda x: x[1]):
    has = any(c in skins for c in children.get(u, []))
    skinned += has
    print("   %-42s skin:%s" % (n[:42], "YES" if has else "no"))
print("\nskinned meshes: %d / %d" % (skinned, len(meshes)))
