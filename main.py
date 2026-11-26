#!/usr/bin/env python3
"""Invent a Word We Need — entry for make.fun.

Coins one new English word and writes it with its one-line definition
to /output/entry.txt (gate: 1-140 UTF-8 characters).
"""

import os

WORD = "Alarmnesia"
DEFINITION = (
    "the brief confusion on waking when your alarm rings and you cannot "
    "remember what day it is or why it matters."
)

# The entry is exactly: word + part of speech + em dash + definition.
ENTRY = f"{WORD} (n.) \u2014 {DEFINITION}"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
