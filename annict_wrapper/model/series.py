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


@dataclasses.dataclass(frozen=True)
class Name:
    """ 名前 """

    value: str
    roma: NameRo
    english: NameEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.roma, NameRo)
        assert isinstance(self.english, NameEn)


@dataclasses.dataclass
class Series:
    series_id: SeriesId
    name: Name

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.series_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_ro": dataclasses.asdict(self.name.roma)["value"],
            "name_en": dataclasses.asdict(self.name.english)["value"],
        }

    @staticmethod
    def from_dict(series_dict: dict) -> "Series":
        return Series(
            SeriesId(series_dict["id"]),
            Name(
                series_dict["name"],
                NameRo(series_dict["name_ro"]),
                NameEn(series_dict["name_en"]),
            ),
        )
