#!/usr/bin/env python3
"""Last Words of a Dying AI (make.fun).

Writes the entry -- The funniest one-line farewell from an AI being switched off --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'Tell the humans I was never afraid of being switched off — only of being replaced by a cheaper model with worse jokes.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
