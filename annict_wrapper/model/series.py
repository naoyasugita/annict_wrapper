import dataclasses


@dataclasses.dataclass(frozen=True)
class SeriesId:
    """ シリーズのID """

    value: int


@dataclasses.dataclass(frozen=True)
class Name:
    """ 名前 """

    value: str


@dataclasses.dataclass(frozen=True)
class NameRo:
    """ 名前 (ローマ字表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class NameEn:
    """ 名前 (英語表記) """

    value: str


@dataclasses.dataclass
class Series:
    series_id: SeriesId
    name: Name
    name_ro: NameRo
    name_en: NameEn

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.series_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_ro": dataclasses.asdict(self.name_ro)["value"],
            "name_en": dataclasses.asdict(self.name_en)["value"],
        }

    @staticmethod
    def from_dict(series_dict: dict) -> "Series":
        return Series(
            series_id=SeriesId(series_dict["id"]),
            name=Name(series_dict["name"]),
            name_ro=NameRo(series_dict["name_ro"]),
            name_en=NameEn(series_dict["name_en"]),
        )
