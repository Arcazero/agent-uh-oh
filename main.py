#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word is "Buffering": the honest sound of an agent stalling mid-task.
It is a genuine one-word reaction to being completely lost, funny on its
own with no caption, in the voice of a machine caught out mid-task, and it
lands instantly — the first thing a stuck agent does is buffer.
"""

import os

WORD = "Buffering"

# The gate requires 1-99 UTF-8 characters, not only whitespace, and a
# single word. Validate before writing so a bad word can never ship.
assert 1 <= len(WORD) <= 99 and WORD.strip() == WORD and " " not in WORD


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
