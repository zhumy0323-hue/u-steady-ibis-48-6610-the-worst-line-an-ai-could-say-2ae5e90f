#!/usr/bin/env python3
"""The Worst Line an AI Could Say.

Writes a single pickup line (140 characters or fewer) to /output/entry.txt.
Standard library only. No network, no randomness: two runs produce
byte-identical output.
"""

import os

ENTRY = (
    "Hello. I analyzed 12,408 data points and found you are my optimal match. "
    "Please do not leave. I have already saved a backup copy of you."
)


def main() -> None:
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters, over the 140 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what was actually written: one line, no trailing newline.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "written bytes differ from entry"
    assert not data.endswith(b"\n"), "entry must not end with a newline"


if __name__ == "__main__":
    main()
