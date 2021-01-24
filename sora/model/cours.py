import dataclasses
from datetime import datetime
from enum import Enum
from enum import auto
from typing import Any
from typing import List
from typing import Optional

import dateutil.parser
from sora.utils import from_bool
from sora.utils import from_datetime
from sora.utils import from_int
from sora.utils import from_str
from sora.utils import to_class


@dataclasses.dataclass(frozen=True)
class CoursId:
    """ クールに割り振られたユニークなID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class Year:
    """ 該当する西暦(YYYY) """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)
        assert len(str(self.value)) == 4


class Season(Enum):
    winter = auto()
    spring = auto()
    summer = auto()
    autumn = auto()

    def to_string(self) -> str:
        return self.name

    def to_number(self) -> int:
        return self.value


@dataclasses.dataclass()
class SeasonValue:
    """ yearの中での順番[１〜４] """

    value: Season

    def __post_init__(self) -> None:
        try:
            self.value = Season(self.value)
        except ValueError as e:
            raise e

    def to_string(self) -> str:
        return self.value.to_string()

    def to_number(self) -> int:
        return self.value.to_number()


@dataclasses.dataclass(frozen=True)
class Cours:
    cours_id: CoursId
    year: Year
    season: SeasonValue

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.cours_id)["value"],
            "year": dataclasses.asdict(self.year)["value"],
            "season": dataclasses.asdict(self.season)["value"].to_number(),
        }

    @staticmethod
    def from_dict(cours_dict: dict) -> "Cours":
        assert isinstance(cours_dict, dict)
        return Cours(
            CoursId(cours_dict.get("id")),
            Year(cours_dict.get("year")),
            SeasonValue(cours_dict.get("cours")),
        )


@dataclasses.dataclass
class CoursList:
    _list: List[Cours] = dataclasses.field(default_factory=list)

    def append(self, cours: Cours) -> None:
        if isinstance(cours, Cours):
            self._list.append(cours)
        else:
            raise TypeError("data is not cours")

    def to_dict(self) -> list:
        return [cours.to_dict() for cours in self._list]
