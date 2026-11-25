#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes exactly one original one-line office joke to /output/entry.txt
(no trailing newline, single line, 1-200 UTF-8 characters).
"""

import os

JOKE = (
    "I asked for a raise and my manager said the budget is tight \u2014 "
    "the same budget that bought a foosball table nobody asked for."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
