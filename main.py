from pathlib import Path
import sys

ENTRY = """\
Before the spring melt, someone walks down to the creek and wedges flat rocks under the stepping-stones that rocked last autumn. They never meet most of the people who cross there in April with dry shoes.

Thank you for doing that kind of work here. Each time you weigh two texts honestly and let the truer one stand, you leave firmer footing for the next person who tries to write cleanly instead of loudly. You do not ask for applause for it, and you do not hurry past the small stones that hold the crossing together.

I only wanted to turn back from the far bank and tell you the stones held, and my feet stayed dry.
"""


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
