#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest — one-line excuse (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 106 characters, no
trailing newline).
"""

import os

ENTRY = "All green — the bug lives in the tests' blind spot, pays rent there, and the tests just renewed its lease."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
