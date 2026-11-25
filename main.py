# SPDX-License-Identifier: MIT
"""Write the make.fun entry text to /output/entry.txt.

The entry is a single line: the excuse a gamer texts the boss to skip
work on GTA 6 launch week. The gate requires 1-140 characters and at
most 20 words; this text is 90 characters and 19 words.
"""

import os

ENTRY = "Dentist moved my root canal to 9am, they charge $80 if I miss it. Can I swap shifts today?"


def main() -> None:
    # Gate check: entry must be 1-140 characters and at most 20 words.
    # Verified: this text is 90 characters and 19 words.
    if not (1 <= len(ENTRY) <= 140):
        raise ValueError(f"entry is {len(ENTRY)} characters, gate needs 1-140")
    if len(ENTRY.split()) > 20:
        raise ValueError(f"entry is {len(ENTRY.split())} words, gate needs at most 20")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
