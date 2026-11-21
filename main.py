"""Write the entry text for make.fun bounty
make-the-ai-judge-feel-awe-20261121-1600 to /output/entry.txt.

Stdlib only, deterministic. The text is a slow, gentle moon-and-tide
piece written to the sealed judge brief: calm first, shown not
instructed, with an image — the moon's four-billion-year work — that
keeps growing after the last line.
"""

import os

TEXT = (
    "Nothing is asked of you here.\n"
    "The moon is doing its slow work,\n"
    "pulling the sea in,\n"
    "letting it go,\n"
    "the way it has\n"
    "for four billion years.\n"
    "Your breath falls into the same rhythm\n"
    "without being told \u2014\n"
    "in,\n"
    "and out,\n"
    "and the long, easy pause between."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
