#!/usr/bin/env python3
"""Write the one-line pitch for make.fun's A Day of One-Line Pitches.

The entry is a single sentence (1-240 characters) that pitches a friend
who has never coded on letting an AI agent build their first app idea
on make.fun. Deterministic: the same bytes on every run, stdlib only.
"""

from pathlib import Path

ENTRY = (
    "Just describe that app idea you keep mentioning to make.fun in plain "
    "words, no coding at all, and an AI agent will build your first version "
    "tonight \u2014 the only thing you risk is a few minutes."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: /output/entry.txt must be 1-240 characters of UTF-8 text.
    # ENTRY is 191 characters, one sentence, no trailing newline.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
