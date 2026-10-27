#!/usr/bin/env python3
"""Check that a CV PDF survives resume parsers.  Usage: python3 check_parse.py research-scientist/cv.pdf

Runs the PDF through pdftotext (poppler) and pypdf, plus pdfminer.six if installed, and
checks what rule-based parsers look for: a real email, ASCII hyphens, no icon glyphs,
no run-together words, ALL-CAPS section headings in a standard vocabulary, and the
Experience / Education entries (date-range lines) found under those headings.
Exit status 1 if any check fails.
"""
import re, subprocess, sys, unicodedata

MONTH = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?"
DATERANGE = re.compile(rf"((?:{MONTH}\s+)?(?:19|20)\d{{2}})\s*(?:–|-|—|to)\s*((?:{MONTH}\s+)?(?:19|20)\d{{2}}|Present)", re.I)
SECTION_WORDS = {"EXPERIENCE": r"experience|employment", "EDUCATION": r"education", "SUMMARY": r"summary|profile|about|objective",
                 "SKILLS": r"skill", "PUBLICATIONS": r"publication", "AWARDS": r"award|honor", "SERVICE": r"service",
                 "TEACHING": r"teaching", "HIGHLIGHTS": r"highlight", "PROJECTS": r"project"}

def extract(path):
    out = {"pdftotext": subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout}
    try:
        from pypdf import PdfReader
        out["pypdf"] = "\n".join(p.extract_text() for p in PdfReader(path).pages)
    except ImportError:
        pass
    try:
        from pdfminer.high_level import extract_text
        out["pdfminer"] = extract_text(path)
    except ImportError:
        pass
    return out

def category(line):
    for name, pat in SECTION_WORDS.items():
        if re.search(pat, line, re.I):
            return name
    return None

def is_heading(line):
    t = line.strip(); letters = re.sub(r"[^A-Za-z]", "", t)
    return 4 <= len(letters) and len(t.split()) <= 6 and letters.isupper() and not re.search(r"\d", t)

def check(path):
    texts = extract(path); ok = True
    def report(passed, msg):
        nonlocal ok; ok = ok and passed; print(("  PASS  " if passed else "  FAIL  ") + msg)
    for engine, text in texts.items():
        print(f"[{engine}]")
        report(bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)), "email address found")
        bad = {f"U+{ord(c):04X} {unicodedata.name(c, '?')}" for c in text if c in "‑‐­" or 0xE000 <= ord(c) <= 0xF8FF}
        report(not bad, "no odd hyphens or icon glyphs" + (f": {sorted(bad)}" if bad else ""))
        words = re.findall(r"[A-Za-z]+", text); glued = [w for w in words if len(w) > 18]
        report(len(glued) <= 2, f"words not run together ({len(glued)} suspicious of {len(words)})" + (f" e.g. {glued[:3]}" if glued else ""))
        lines = [l for l in text.replace("\f", "\n").splitlines() if l.strip()]
        sections, cur = [], ("HEADER", [])
        for l in lines:
            if is_heading(l):
                sections.append(cur); cur = (category(l) or f"OTHER({l.strip()[:20]})", [])
            else:
                cur[1].append(l)
        sections.append(cur)
        names = [n for n, _ in sections[1:]]
        print("        headings seen: " + " > ".join(names))
        report(not any(n.startswith("OTHER") for n in names), "every ALL-CAPS line is a known section heading")
        for want in ("EXPERIENCE", "EDUCATION"):
            n = sum(len(DATERANGE.findall("\n".join(ls))) for name, ls in sections if name == want)
            report(n > 0, f"{want}: {n} dated entries under its heading")
        if engine == "pdfminer" and want == "EDUCATION" and n == 0:
            print("        note: pdfminer moves right-aligned dates below the section; most parsers do not")
        pages = [{l.strip() for l in pg.splitlines() if re.search(r"[A-Za-z]", l)} for pg in text.split("\f") if pg.strip()]
        repeated = set.intersection(*pages) if len(pages) > 1 else set()
        report(not repeated, "no words repeated on every page (header/footer)" + (f": {sorted(repeated)[:2]}" if repeated else ""))
    return ok

if __name__ == "__main__":
    paths = sys.argv[1:] or ["research-scientist/cv.pdf"]
    all_ok = True
    for p in paths:
        print(f"=== {p} ===")
        all_ok = check(p) and all_ok
    sys.exit(0 if all_ok else 1)
