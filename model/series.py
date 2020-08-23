import dataclasses


@dataclasses.dataclass
class Series:
    id: int
    name: str
    name_ro: str
    name_en: str

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
