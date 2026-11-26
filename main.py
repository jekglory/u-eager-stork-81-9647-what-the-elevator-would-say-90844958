"""What the elevator would say, if it could talk.

Writes a single funny line (1-120 characters) in the elevator's own
voice to /output/entry.txt. Pure Python standard library, no imports
beyond os. Deterministic: the same bytes on every run.
"""

import os

# The line: every passenger mashes the call button twice, as if the
# second press were a turbo mode. The elevator answers in its own
# voice — it is not faster, it is just spiteful, and its maintenance
# schedule is old enough to vote. The joke lands on the first read:
# a real, recognisable passenger habit, then a surprise turn that
# only an elevator could deliver.
LINE = (
    "You press the button twice like that helps. It doesn't. "
    "I run on spite and a maintenance schedule from 1998."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 120  # sealed gate: /output/entry.txt must be 1..120 characters


def main() -> None:
    line = LINE.strip()
    if not (1 <= len(line) <= MAX_CHARS):
        raise SystemExit(f"line must be 1-{MAX_CHARS} characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    # The grader owns /output: create it only if missing, never remove it.
    # Write exactly the line, no trailing newline, so the file's byte
    # count equals the line's character count.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    print(f"({len(line)} characters -> {OUTPUT_FILE})")


if __name__ == "__main__":
    main()
