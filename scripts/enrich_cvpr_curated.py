#!/usr/bin/env python3
"""Enrich the curated cvpr2026-data.json with affiliations (and upgrade placeholder
talk titles) by matching each talk against the exhaustive cvpr2026-all.json speaker
data. The viewer already supports a per-talk `aff` field (affiliation filter, modal,
search) -- it was just never populated.
"""
import json, os, re, unicodedata

HERE = os.path.dirname(__file__)
CUR = os.path.join(HERE, "..", "public", "cvpr2026-data.json")
ALL = os.path.join(HERE, "..", "public", "cvpr2026-all.json")

cur = json.load(open(CUR))
alld = json.load(open(ALL))

# curated workshop key -> exhaustive (all.json) workshop key
WS_MAP = {
    "BitterLessons": "BitterLessons", "VAR": "VAR", "EgoVis": "EgoVis", "T4V": "T4V",
    "COGVL": "CogVL", "VITA": "VITA", "CV4Smalls": "CV4Smalls", "ViSCALE": "ViSCALE",
    "ReLearn": "ReLearn", "DataMFM": "DataMFM", "CVinW": "CVinW",
    "KnowledgeMR": "KnowledgeMR", "MAR": "MAR", "A2A-MML": "A2AMML", "LOVEU": "LOVEU",
    "MMR": "MMRAGI", "SAUAFG": "SAUAFG",
}

def strip(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower().strip()

def parse_who(who):
    """Return (surname, firsthint) from a curated 'who' string."""
    m = re.match(r"^(.*?)\s*\(([^)]+)\)\s*$", who)
    if m:
        return strip(m.group(1)), strip(m.group(2))
    base = re.sub(r"\bet al\.?$", "", who).strip()
    return strip(base), None

def match_speaker(who, speakers):
    sur, hint = parse_who(who)
    if sur in ("panel", "panel 1", "panel 2", "panel 3"):
        return None
    cands = []
    for sp in speakers:
        full = strip(sp["name"])
        toks = full.split()
        if not toks:
            continue
        last = toks[-1]
        surname_ok = (last == sur) or any(t == sur for t in toks) or sur in full
        if not surname_ok:
            continue
        if hint:
            hint_ok = any(t.startswith(hint) or hint.startswith(t) for t in toks)
            score = 2 if hint_ok else 0
            if not hint_ok:
                continue
        else:
            score = 1 if last == sur else 0
        cands.append((score, sp))
    if not cands:
        return None
    cands.sort(key=lambda x: -x[0])
    return cands[0][1]

n_aff = n_title = n_miss = 0
missed = []
for t in cur["talks"]:
    wkey = WS_MAP.get(t["ws"])
    ws = alld["workshops"].get(wkey) if wkey else None
    if not ws:
        continue
    sp = match_speaker(t["who"], ws["speakers"])
    if not sp:
        if not str(t["who"]).lower().startswith("panel"):
            n_miss += 1
            missed.append(t["ws"] + " / " + t["who"])
        continue
    if sp.get("affil") and not t.get("aff"):
        t["aff"] = sp["affil"]
        n_aff += 1
    # conservative title upgrade: only when curated title is a bare placeholder
    if sp.get("title") and t.get("title") == t.get("who"):
        t["title"] = sp["title"]
        n_title += 1

# reorder keys so `aff` sits next to `who` for readability
order = ["day", "s", "e", "ws", "room", "who", "aff", "topic", "tier", "title", "tags", "id"]
cur["talks"] = [{k: t[k] for k in order if k in t} for t in cur["talks"]]

# attach the full co-speaker roster (name/affil/role) to each curated workshop
n_roster = 0
for ckey, w in cur["workshops"].items():
    wkey = WS_MAP.get(ckey)
    ws = alld["workshops"].get(wkey) if wkey else None
    if not ws or not ws["speakers"]:
        continue
    w["speakers"] = [
        {"name": s["name"], "affil": s["affil"], "role": s["role"]}
        for s in ws["speakers"]
    ]
    n_roster += 1
print("workshop rosters attached:", n_roster)

json.dump(cur, open(CUR, "w"), ensure_ascii=False, indent=1)
print("affiliations added:", n_aff)
print("placeholder titles upgraded:", n_title)
print("unmatched (non-panel) talks:", n_miss)
for m in missed:
    print("   MISS:", m)
