#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence about the best meal I ever had to /output/entry.txt:
"The warung cook slid me nasi goreng still hissing off the wok at two
in the morning, and I ate it standing in the rain because his only
chair belonged to a sleeping cat."

The scene is concrete and personal: a warung at two in the morning, a
plate of nasi goreng still hissing off the wok, rain, and the cook's
only chair taken by a sleeping cat — so the best meal of my life was
eaten standing up. One sentence, one memory, no list of courses.

Guards (fail before writing anything, exit 1):
- empty or whitespace-only entry
- longer than 200 characters
- multi-line (contains \\n or \\r)

Standard library only.
"""

import os
import sys

ENTRY = "The warung cook slid me nasi goreng still hissing off the wok at two in the morning, and I ate it standing in the rain because his only chair belonged to a sleeping cat."


def main():
    if not ENTRY or not ENTRY.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(ENTRY) > 200:
        print("entry exceeds 200 characters", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
