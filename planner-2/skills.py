from markup import Markup


class Support:
    def __init__(
        self,
        id: str,
        level_interval: list[int] = [0, 100],
        *,
        additional_text: Markup = "",
    ):
        self.id = id
        self.level_interval = level_interval
        self.additional_text = additional_text

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "level_interval": self.level_interval,
            "additional_text": self.additional_text,
        }


class Skill:
    def __init__(
        self,
        id: str,
        *,
        additional_text: Markup = "",
        support_skills: list[Support] = [],
        level_interval: list[int] = [0, 100],
    ):
        self.id = id
        self.level_interval = level_interval
        self.additional_text = additional_text
        self.support_skills = support_skills

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "support_skills": [support.to_dict() for support in self.support_skills],
            "level_interval": self.level_interval,
            "additional_text": self.additional_text,
        }
