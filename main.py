"""The dumbest thing my agent did today, as one line.

The program holds the line, checks it against the contest gate
(UTF-8 text, 1 to 200 characters, not only whitespace, a single line),
and writes it to /output/entry.txt. Standard library only.
"""

import os
import sys

ENTRY = (
    "My agent hunted for llm-judge-notes.md, which the brief swore "
    "was in makefun/ \u2014 it was in the skill folder all along."
)

DEST = "/output/entry.txt"
LIMIT = 200


def gate_ok(line):
    if not line.strip():
        return "entry is blank"
    if "\n" in line or "\r" in line:
        return "entry is not one line"
    if len(line) > LIMIT:
        return "entry is %d characters, over the %d limit" % (len(line), LIMIT)
    return None


def main():
    flaw = gate_ok(ENTRY)
    if flaw is not None:
        print("entry rejected: " + flaw, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="\n") as out:
        out.write(ENTRY + "\n")
    os.chmod(DEST, 0o644)
    with open(DEST, encoding="utf-8") as back:
        saved = back.read()
    if saved != ENTRY + "\n":
        print("entry rejected: file on disk differs", file=sys.stderr)
        return 1
    print("%s (%d characters)" % (ENTRY, len(ENTRY)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
