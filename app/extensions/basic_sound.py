from app.extensions.base_class import Extension
from app import categories


class BasicSound(Extension):
    def __init__(
        self,
        *,
        sound: categories.BASIC_SOUND,
        volume: categories.VOLUME = categories.VOLUME.MEDIUM,
    ):
        super().__init__()
        self.sound = sound
        self.volume = volume

    def __str__(self):
        return f"""
            PlayAlertSound {self.sound.value} {self.volume.value}
        """
