#!/usr/bin/env python3.13
from pathlib import Path

WORD = "ratio"
OUT = Path("/output/entry.txt")


def gate() -> str:
    text = WORD.strip()
    if not (1 <= len(text) <= 30):
        raise SystemExit("word outside 1..30 characters")
    if not text.encode("utf-8").decode("utf-8"):
        raise SystemExit("entry not utf-8")
    return text


def emit() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(gate(), encoding="utf-8")


emit()
print(OUT.read_text(encoding="utf-8"), file=__import__("sys").stderr)
