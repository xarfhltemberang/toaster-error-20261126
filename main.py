#!/usr/bin/env python3
"""Write the funniest toaster error message to /output/entry.txt.

One line, at most 120 characters, no trailing newline.
"""

import os

ENTRY = "Error 07: This slice was toasted before. It is now legally a crouton. I cannot help you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
