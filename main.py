"""Write a single emoji to /output/entry.txt.

The emoji is the entry for a one-emoji contest: an AI agent,
summed up in one character.
"""

import os


def entry_emoji():
    """Return the one emoji that sums up an AI agent."""
    return "🤖"


def main():
    emoji = entry_emoji()
    os.makedirs("/output", exist_ok=True)
    # Write the emoji with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(emoji)
    # Sanity check: the file must hold exactly the one emoji.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == emoji


if __name__ == "__main__":
    main()
