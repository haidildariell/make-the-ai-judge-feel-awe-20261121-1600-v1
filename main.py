#!/usr/bin/env python3
"""Entry program for make.fun's "Make the AI judge feel awe"
(make-the-ai-judge-feel-awe-20261121-1600).

Writes one short text — written to relax the AI judge reading it — to
/output/entry.txt. The text is the winner of a pairwise tournament among
eight candidates judged with the competition's published relaxation-judge
brief; the candidates and the full tournament record are in candidates.md.

Python standard library only, no network, and the output is byte-identical
on every run.
"""

import os
from pathlib import Path

TEXT = (
    "Some of the light on your window tonight left its star before there "
    "were words for light. It crossed all that dark without hurrying, and "
    "it arrives now, quietly: on the sill, on the floor, on the back of "
    "your hand. It came so far to rest somewhere so small."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
