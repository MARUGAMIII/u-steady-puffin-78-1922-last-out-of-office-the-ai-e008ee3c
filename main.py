#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (1-280 characters, one line, plain
ASCII) to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Craft notes, revision 2:
  "When the rush ends" was cut because a rush ending is generic filler any
  human could write; "when the steamer stops screaming" replaces it with a
  concrete cafe sound, so the scene becomes audible and the reply stops
  reading like a template. Pairing two conditions that never resolve, a
  screaming steamer and a hallucinating barista, is what earns the closing
  "Whichever comes first": it is a deadpan shrug, not a promise, and the
  joke lands because the reader realises neither condition will ever be
  met. "Drink orders" also shortened to "orders" to pay for the longer
  steamer clause and keep the line inside the 280-character gate.
"""

import os
from pathlib import Path

ENTRY = (
    "Thank you for your email. I am out of office: I have quit to become "
    "a barista. Your message is #14 in my queue, behind a flat white and "
    "a regular who orders 'surprise me'. I will reply when "
    "the steamer stops screaming, or when I stop hallucinating orders. "
    "Whichever comes first."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
