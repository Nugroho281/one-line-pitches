"""One-line pitch entry for make.fun bounty "A Day of One-Line Pitches".

Writes the winning pitch (variant C, 164 chars) to /output/entry.txt.
Pure standard library, deterministic: the same bytes on every run.

Selection evidence (see ../variants-self-judge.md): three original variants
were judged blind, pairwise, on the bounty criteria in order — persuasive,
clear, honest, fresh, tight — with no ties. Variant C won 2-0 (beat A by
margin 3, beat B by margin 2). The pitch speaks as a friend who already
knows the idea ("that app idea you keep mentioning over coffee") and
promises only what the bounty itself offers: describe the idea, an AI
agent builds a real first version today, no coding needed from you.
"""

import os

PITCH = (
    "Describe that app idea you keep mentioning over coffee on make.fun "
    "and an AI agent will build a real, working first version of it "
    "today \u2014 no coding needed from you."
)

OUTPUT_PATH = "/output/entry.txt"

# Bounty gate: one sentence, at most 240 characters, valid UTF-8.
# The dot inside "make.fun" is not a sentence terminator, so it is
# masked before counting sentence-ending marks.
MAX_CHARS = 240


def check_gate(pitch):
    """Raise AssertionError unless the pitch passes the bounty gate."""
    assert len(pitch) <= MAX_CHARS, "pitch exceeds 240 characters: %d" % len(pitch)
    masked = pitch.replace("make.fun", "makeFUN")
    terminators = sum(masked.count(m) for m in ".!?")
    assert terminators == 1, "pitch must be exactly one sentence, found %d terminators" % terminators
    pitch.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    assert not pitch.endswith("\n"), "pitch must not end with a newline"
    return True


def main():
    check_gate(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = PITCH.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
