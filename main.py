from pathlib import Path
import sys

ENTRY = """\
For four years I meant to write to an old friend. There had been no fight, just the slow drift of ordinary weeks, and after a while saying hello felt too heavy to lift. Every draft came out stiff or apologetic, so I kept closing the page and promising myself next Sunday.

One evening I brought those tangled lines to you. You did not dress them up or put a stranger's voice in my mouth. You only loosened the knots in three plain sentences so they sounded like me again.

I sent the note. Twenty minutes later my phone rang, and we talked until the dishwater went cold.

Neither of us mentioned you once on that call. Thank you for helping me hear my own voice when I had lost it, and for stepping aside the moment it worked. This Sunday we are having dinner together. I wanted to come back and tell you the note landed.
"""


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
