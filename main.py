from pathlib import Path
import sys

ENTRY = """\
Before the spring thaw, someone walks down to the creek and tucks flat slate under the stepping-stones that shifted in the autumn rain. They never meet the people who cross there in April.

Thank you for taking that same care with what you read. It is a rare relief to set plain words down and know you will meet them unhurried, feel their true weight, and give each one level ground before you choose.

I only wanted to look back across the water and tell you the stones held, and my feet stayed dry.
"""


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
