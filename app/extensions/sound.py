from app.extensions.base_class import Extension
from app import categories


class Sound(Extension):
    def __init__(
        self,
        *,
        file: categories.SOUND_FILE,
        volume: categories.VOLUME = categories.VOLUME.MEDIUM,
        silent: bool = False,
    ):
        super().__init__()
        self.file = file
        self.volume = volume
        self.silent = silent

    def __str__(self):
        if self.silent:
            return f"""
                DisableDropSound
                PlayEffect None
                PlayAlertSound None
                CustomAlertSound None
            """

        return f"""
            CustomAlertSound "{self.file.value}" {self.volume.value}
        """
