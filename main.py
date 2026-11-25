#!/usr/bin/env python3
"""The 3 AM Excuse - make.fun bounty entry.

Writes one line (under 200 characters) to /output/entry.txt: the excuse
a hardware wallet gives for refusing to sign a transaction at 3 AM.

The angle: the wallet's seed phrase is a sleeping baby. Waking it at
3 AM makes it cry - and a 12-word seed phrase cries in twelve words.
No battery joke, no firmware update, no cold storage: the hour itself
is the joke, and the refusal is the punchline.
"""

import os
from pathlib import Path

LINE = "My seed phrase is asleep. Wake it at 3 AM and it cries in twelve words \u2014 all twelve of them 'no'."


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} chars, must be under 200"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.txt"
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} chars to {out}:")
    print(text)


if __name__ == "__main__":
    main()
