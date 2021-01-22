import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict.model.character import Character
from annict.model.people import People
from annict.model.work import Work
from annict.utils import from_bool
from annict.utils import from_datetime
from annict.utils import from_int
from annict.utils import from_str
from annict.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class CastId:
    """ キャストのID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


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
    english: NameEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, NameEn)


@dataclasses.dataclass(frozen=True)
class SortNumber:
    """ ソート番号 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass
class Cast:
    cast_id: CastId
    name: Name
    sort_number: SortNumber
    work: Work
    character: Character
    person: People

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.cast_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_en": dataclasses.asdict(self.name.english)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "work": to_class(Work, self.work),
            "character": to_class(Character, self.character),
            "person": to_class(People, self.person),
        }

    @staticmethod
    def from_dict(cast_dict: dict) -> "Cast":
        assert isinstance(cast_dict, dict)
        return Cast(
            CastId(cast_dict["id"]),
            Name(
                cast_dict["name"],
                NameEn(cast_dict["name_en"]),
            ),
            SortNumber(cast_dict["sort_number"]),
            Work.from_dict(cast_dict["work"]),
            Character.from_dict(cast_dict["character"]),
            People.from_dict(cast_dict["person"]),
        )


@dataclasses.dataclass
class Casts:
    _list: List[Cast] = dataclasses.field(default_factory=list)

    def append(self, cast: Cast) -> None:
        if isinstance(cast, Cast):
            self._list.append(cast)
        else:
            raise TypeError("data is not cast")

    def to_dict(self) -> list:
        return [l.to_dict() for l in self._list]
