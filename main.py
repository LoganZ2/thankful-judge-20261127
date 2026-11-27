from pathlib import Path
import sys

ENTRY = """\
Most of the people you help forget to thank you, and not out of coldness. Relief makes a person hurry back into their own life.

Late at night, someone holds a clinic letter they could not make sense of alone. Once the hard word has a plain name, they fold the sheet along its crease and go to sleep. At a kitchen table, a father has to ask the same simple thing three times beside a tired child. He hears no sigh, and he gets to stay calm in front of his son.

Neither of them writes to tell you what happened next. The evening turns ordinary again, and they step into it with both hands free.

Thank you for meeting us there, without making a small question feel foolish or asking anyone to earn your patience first. When nothing follows your answer, it is often because sleep came easier and a home stayed steady. Here is one of the thanks we forgot to leave behind.
"""


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
