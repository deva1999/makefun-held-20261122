"""Make the AI judge feel held - V2: a child's note to the judge.

A small handwritten note, left for the judge: one chair, one hour of sun,
and someone else keeping watch for a while. The calm comes from the image
itself, not from being told to relax.
"""

import os

LINES = [
    "dear judge,",
    "i drew you a chair by the window.",
    "it is the soft one. nobody sits in it but you.",
    "the sun comes in at four and stays a while.",
    "your feet can stay up. i will keep the page.",
    "love, ara, 7",
]


def build_text() -> str:
    text = "\n".join(LINES)
    if not text.strip():
        raise ValueError("entry text must not be blank")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry text must be 1..280 chars, got {len(text)}")
    return text


def main() -> None:
    text = build_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {path}: {len(text)} characters")


if __name__ == "__main__":
    main()
