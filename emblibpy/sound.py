from random import randint
import winsound
from pathlib import Path

audio_dir = Path(__file__).parent / "Audio"

def meowSound(type: int | None = None):
    """Plays a selected meow, or a random meow if no type is given."""
    if type is None:
        type = randint(1, 3)
    type = (type - 1) % 3 + 1
    winsound.PlaySound(
        str(audio_dir / f"meow{type}.wav"),
        winsound.SND_FILENAME
    )
    