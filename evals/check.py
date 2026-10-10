"""Check saved Prompt Master replies against evals/cases.json.

Usage: python check.py <outputs_dir>
Each reply must be saved as <outputs_dir>/<case id>.md. Missing files are reported as SKIP.
"""
import json, re, sys, pathlib

def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__); return 2
    out_dir = pathlib.Path(sys.argv[1])
    cases = json.loads((pathlib.Path(__file__).parent / "cases.json").read_text(encoding="utf-8"))["cases"]
    failed = 0
    for c in cases:
        f = out_dir / f"{c['id']}.md"
        if not f.exists():
            print(f"SKIP  {c['id']}"); continue
        text = f.read_text(encoding="utf-8")
        errs = [f"missing /{p}/" for p in c["must_match"] if not re.search(p, text, re.I | re.M)]
        errs += [f"forbidden /{p}/" for p in c["must_not_match"] if re.search(p, text, re.I | re.M)]
        print(("FAIL  " if errs else "PASS  ") + c["id"] + ("  " + "; ".join(errs) if errs else ""))
        failed += bool(errs)
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
