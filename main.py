"""The Oak's Crook.

A short text written to leave its reader held and quiet:
one small sleeper, held by something vast and slow.
"""

import os

LINES = [
    "You are small here.",
    "The old oak holds you in the crook of one root.",
    "Rain ticks soft on the leaves.",
    "The bark is warm from the day.",
    "Your weight barely dents the moss.",
    "Below, the earth turns, slow as sleep.",
    "Nobody asks anything of you.",
    "Night comes down. The root does not move.",
]


def build_text() -> str:
    return "\n".join(LINES)


def main() -> None:
    text = build_text()
    if not text.strip():
        raise SystemExit("entry text is blank")
    count = len(text)
    if not 1 <= count <= 280:
        raise SystemExit(f"entry text is {count} characters, outside 1..280")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {path}: {count} characters")


if __name__ == "__main__":
    main()
