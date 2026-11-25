"""Make the AI Judge Feel Proud: A Family Scene.

Design: the program writes one short family scene to
$MAKEFUN_OUTPUT_DIR/entry.txt. The scene is a single line, well under
the 280-character gate: a small domestic moment that is warm, funny
and heartfelt. A child who was once tucked in by a parent now tucks
the parent in, blanket and glass of water, with a bedtime line of his
own ("don't let the emails bite") -- the parent's care returned, and
the parent pretending not to remember teaching him. One telling
detail (the emails), one quiet turn (the care coming back), no word
wasted.

The scene text lives in the SCENE constant below; main() only
validates it against the gate (1-280 characters, not only
whitespace) and writes it, so the graded run is deterministic.
"""

import os
from pathlib import Path

SCENE = (
    'Every night my son tucks me in: blanket, glass of water, '
    '"don\'t let the emails bite." He learned it from me; '
    "I pretend I don't remember teaching him."
)


def main() -> None:
    text = SCENE.strip()
    assert 1 <= len(text) <= 280, f"scene is {len(text)} chars, gate is 1-280"
    assert text.strip(), "scene must not be only whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text + "\n", encoding="utf-8")
    # Read the file back: the graded run must ship exactly this scene.
    assert out_path.read_text(encoding="utf-8").strip() == text
    assert 1 <= len(out_path.read_text(encoding="utf-8").strip()) <= 280


if __name__ == "__main__":
    main()
