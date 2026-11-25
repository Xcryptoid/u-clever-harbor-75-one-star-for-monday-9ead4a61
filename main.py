"""One Star for Monday — entrypoint.

Copies the pre-written one-line review (entry.txt) into the output
directory the grader provides, nothing more.
"""

import os
import shutil


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    # The review itself never changes at runtime: it is written once,
    # in entry.txt, and this script only hands that exact text to the
    # grader, so every run of the entry produces the same 22 words.
    main()
