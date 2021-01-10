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
class NameKana:
    """ 名前 (かな表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class NameEn:
    """ 名前 (英語表記) """

    value: str



@dataclasses.dataclass
class Series:
    series_id: SeriesId
    name: Name
    name_ro: NameKana
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
            name=SeriesId(series_dict["name"]),
            name_ro=SeriesId(series_dict["name_ro"]),
            name_en=SeriesId(series_dict["name_en"]),
        )
