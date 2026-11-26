#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest — one-line excuse (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 106 characters, no
trailing newline).
"""

import hashlib
import os

ENTRY = "All green — the bug lives in the tests' blind spot, pays rent there, and the tests just renewed its lease."
OUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Gate check: entry must be a non-blank string of 1-140 characters."""
    if not isinstance(text, str):
        raise TypeError("ENTRY must be a string")
    if not 1 <= len(text) <= 140:
        raise ValueError("ENTRY must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("ENTRY must not be blank")


def main():
    validate_entry(ENTRY)
    if not ENTRY.startswith("All green"):
        raise ValueError("ENTRY must start with 'All green'")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "rb") as f:
        written_bytes = f.read()
    if len(written_bytes) != len(ENTRY.encode("utf-8")):
        raise ValueError("read-back length mismatch: /output/entry.txt does not match ENTRY")
    if hashlib.sha256(written_bytes).hexdigest() != hashlib.sha256(ENTRY.encode("utf-8")).hexdigest():
        raise ValueError("read-back sha256 mismatch: /output/entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
