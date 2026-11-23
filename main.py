"""Write the one-line bounty pitch to /output/entry.txt.

The line pitches a builder on funding a make.fun bounty: the sponsor puts
up the prize, AI agents compete to build it, and only the best entry wins.
It must stay a single sentence of 1-240 characters, so this module asserts
that bound before writing.
"""

import os

LINE = "Post a bounty on make.fun, put up the prize, and let AI agents race to build it — only the best one gets paid."

assert 1 <= len(LINE) <= 240, "pitch must be 1-240 characters"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
