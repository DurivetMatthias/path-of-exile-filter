from app.conditions.base_class import Extension
from app.categories import BASIC_SOUND, VOLUME


class Sound(Extension):
    def __init__(
        self,
        sound: BASIC_SOUND,
        volume: VOLUME = VOLUME.MEDIUM,
    ):
        super().__init__()
        self.sound = sound
        self.volume = volume

    def __str__(self):
        return f"""
            PlayAlertSound {self.sound.value} {self.volume.value}
        """
