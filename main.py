"""Writes one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing: the choice lives in the pause
before the act, and the agreement itself is built in shared silence.
"""
import os
from pathlib import Path

POEM = """Between my finger and the button
lies a whole country.
You stood in it beside me,
said nothing —
and the silence
was the first thing
we ever built together."""


def main():
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
