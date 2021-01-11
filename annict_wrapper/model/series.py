import dataclasses

from annict_wrapper.utils import from_bool
from annict_wrapper.utils import from_datetime
from annict_wrapper.utils import from_int
from annict_wrapper.utils import from_str
from annict_wrapper.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class SeriesId:
    """ シリーズのID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class Name:
    """ 名前 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class NameRo:
    """ 名前 (ローマ字表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class NameEn:
    """ 名前 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


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
