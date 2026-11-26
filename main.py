#!/usr/bin/env python3
"""Write the one-line GPS joke to /output/entry.txt.

The entry is one sentence about a GPS that declares arrival far too
early. It works by a reversal: the setup is a navigation error everyone
has suffered, and the punchline reframes that error as emotional
validation — the machine's misplaced certainty becomes the most
confidence anyone has ever had in the speaker. The joke lands on the
self-deprecating twist at the very end, with no explanation after it.

The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-200 characters, not only
whitespace, a single line) before it is written.
"""

import os

# Parts of the line: the setup states the GPS's premature verdict, the
# punchline turns that error into the speaker's proudest compliment.
SETUP = "My GPS said 'you have arrived' while I was still on the highway"
PUNCHLINE = "the most confidence anyone has ever had in me."

# The em dash joins setup and punchline in one breath; the line reads as
# a single sentence with the laugh landing on its last words.
LINE = SETUP + " \u2014 " + PUNCHLINE


def validate(text):
    """Gate check: UTF-8, 1-200 chars, not only whitespace, one line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    print(entry, end="")


if __name__ == "__main__":
    main()
