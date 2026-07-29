import textwrap
from pathlib import Path

from doodad import Doodad

FILE_EXTENSION = "hideout"
FILTER_OUTPUT_PATH = Path(".")


class Hideout:
    def __init__(
        self,
        doodads: list[Doodad],
        *,
        hideout_name: str = "Celestial nebula Hideout",
        hideout_hash: int = 35022,
        music_name: str = "Acton's Nightmare",
        music_hash: int = 52832,
    ):
        self.hideout_name = hideout_name
        self.hideout_hash = hideout_hash
        self.music_name = music_name
        self.music_hash = music_hash
        self.doodads = doodads

    def to_pseudo_json(self) -> str:
        doodads = []
        for doodad in self.doodads:
            doodads.append(
                f"""
                    \"{doodad.name}\": {{
                        "hash": {doodad.hash},
                        "x": {doodad.x},
                        "y": {doodad.y},
                        "r": {doodad.rotation},
                        "fv": {doodad.version}
                    }}"""
            )

        return textwrap.dedent(f"""
            {{
                "version": 1,
                "language": "English",
                "hideout_name": "{self.hideout_name}",
                "hideout_hash": {self.hideout_hash},
                "music_name": "{self.music_name}",
                "music_hash": {self.music_hash},
                "doodads": {{{",".join(doodads)}
                }}
            }}
        """).strip()

    def generate(self, name: str) -> None:
        output_filepath = FILTER_OUTPUT_PATH / f"{name}.{FILE_EXTENSION}"
        with open(output_filepath, mode="w", encoding="utf-8") as output_file:
            output_file.write(self.to_pseudo_json())

        path_length = len(str(output_filepath))
        print("=" * path_length)
        print(output_filepath)
        print("=" * path_length)
