"""Copy the bundled news image to the grader's output directory.

The entry image (entry.png) is the front page built for this bounty: it sums
up the world's news of Sunday 22 November 2026 in one image. The program
does no network, no randomness and no clock reads, so every run writes the
exact same bytes.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit("entry.png is missing from the repository")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
