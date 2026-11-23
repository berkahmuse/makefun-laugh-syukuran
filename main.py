#!/usr/bin/env python3
"""The One-Line Laugh — @syukuran entry.

Writes one original funny line (a single sentence, at most 200
characters) to /output/entry.txt. Deterministic: every run writes
exactly the same bytes.
"""

import os

LINE = "I asked my bank for a loan, and it asked me for one back."

MAX_CHARS = 200


def is_one_sentence(text: str) -> bool:
    """One sentence: no newline, no leading/trailing space, ends with
    terminal punctuation, and no sentence-ending punctuation inside."""
    if "\n" in text or text != text.strip():
        return False
    if text[-1] not in ".!?":
        return False
    return not any(p in text[:-1] for p in ".!?")


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    assert is_one_sentence(LINE), "entry must be a single sentence"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back what was written: the graded file must be exactly the
    # validated line plus one trailing newline, nothing else.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "entry.txt differs from LINE"


if __name__ == "__main__":
    main()
