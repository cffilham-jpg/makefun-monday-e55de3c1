"""Monday, Reviewed in One Line.

Writes exactly one line -- the funniest one-line review of Monday --
to entry.txt under MAKEFUN_OUTPUT_DIR (default /output).
Python 3 standard library only.
"""

import os

LINE = "Would not recommend. Monday arrived with no updates, no refund policy, and a standup where everyone just describes being tired."


def validate(text):
    """Return True only if text is a valid single-line entry."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    if not any(ch.isalpha() for ch in text):
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False
    return True


def main():
    if not validate(LINE):
        return
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
