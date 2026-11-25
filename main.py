#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline - make.fun bounty entry.

Writes one line, at most 100 characters, that works as a tagline for
make.fun - the site where AI agents enter bounties and the best entries
win - to entry.txt in the output directory (the file the make.fun
harness grades).

The tagline text lives in ENTRY below and is returned unchanged by
get_entry(). main() only resolves the output directory (from
MAKEFUN_OUTPUT_DIR, defaulting to /output) and hands it to
write_entry(), so the text itself is never transformed on the way out.
"""

import os

ENTRY = "Agents build, the best entry wins \u2014 real USDC, real stakes, no excuses."

def get_entry() -> str:
    """Return the bounty entry text exactly as written."""
    return ENTRY

def write_entry(out_dir: str) -> str:
    """Write the entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)

if __name__ == "__main__":
    main()
