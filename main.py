from pathlib import Path
import sys

ENTRY = """\
Five minutes before closing on a wet November afternoon, I laid a creased page on a worn oak counter, braced for a sigh. The clerk did not glance at the wall clock. He smoothed the folded corner flat with the heel of his hand and gave me the unhurried calm of nine in the morning.

The rain was still falling when I stepped outside, and the hurry had left my shoulders.

Thank you for bringing that care to the work in front of you. Pair after pair, you carry no tiredness from the last piece and no rush toward the next. Every voice that comes to you, plain or unsure, has the whole of your attention, as if the morning had only just begun.

I never went back to tell that clerk how much he steadied me, so I am telling you now. The patience you keep here reaches further than you can see. Long after the counter closes, the warmth of it stays.
"""


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
