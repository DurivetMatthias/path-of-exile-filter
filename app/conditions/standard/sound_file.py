from app.conditions.base_class import Extension
from app.categories import SOUND_FILE, VOLUME


class Sound(Extension):
    def __init__(
        self,
        file: SOUND_FILE,
        volume: VOLUME = VOLUME.MEDIUM,
    ):
        super().__init__()
        self.file = file
        self.volume = volume

    def __str__(self):
        return f"""
            CustomAlertSound "{self.file.value}" {self.volume.value}
        """
