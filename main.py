"""One word for the human an AI agent works for: Seagull.

The word names the classic "seagull manager": a boss who swoops in
out of nowhere, squawks loudly over everything, dumps on the work,
and flies off again before lifting a finger himself. It is funny
because it is true, and the picture lands instantly -- no explanation
needed. One word, nothing else: no newline, no extra bytes.
Deterministic across runs.
"""

import os

WORD = "Seagull"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
