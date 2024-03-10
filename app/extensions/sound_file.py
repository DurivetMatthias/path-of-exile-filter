from app.extensions.base_class import Extension
from app import categories


class Sound(Extension):
    def __init__(
        self,
        *,
        file: categories.SOUND_FILE,
        volume: categories.VOLUME = categories.VOLUME.MEDIUM,
    ):
        super().__init__()
        self.file = file
        self.volume = volume

    def __str__(self):
        return f"""
            CustomAlertSound "{self.file.value}" {self.volume.value}
        """
