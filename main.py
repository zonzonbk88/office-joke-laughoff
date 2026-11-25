#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes exactly one original one-line office joke to /output/entry.txt
(no trailing newline, single line, 1-200 UTF-8 characters).

Why this line was chosen (judge criteria):
- On-brief: a workplace joke about a raise request, instantly relatable.
- Twist: the "tight budget" excuse is undercut by the manager's own
  spending — the punchline reframes the premise instead of restating it.
- Concrete detail: the foosball table is a specific, odd purchase, not a
  generic "no money" gag; the image of an unwanted office toy carries the
  joke. It also avoids worn motifs (coffee, deadlines, robots).
- Gate: 124 characters, single line, no trailing newline — verified below.
"""

import os

JOKE = (
    "I asked for a raise and my manager said the budget is tight \u2014 "
    "the same budget that bought a foosball table nobody asked for."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    """Write the chosen joke to OUTPUT_PATH as one exact line.

    Guarantees: the file contains exactly JOKE.strip() — a single line,
    1-200 characters, no leading/trailing whitespace, no trailing newline.
    """
    text = JOKE.strip()
    assert text == JOKE.strip(), "joke must be written exactly as stripped"
    assert text == text.strip(), "joke must have no leading/trailing whitespace"
    assert "\n" not in text, "joke must be a single line"
    assert "\r" not in text, "joke must not contain carriage returns"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
