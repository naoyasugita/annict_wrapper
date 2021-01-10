import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict_wrapper.model.character import Character
from annict_wrapper.model.people import People
from annict_wrapper.model.work import Work


@dataclasses.dataclass(frozen=True)
class CastId:
    """ キャストのID """
    value: int

@dataclasses.dataclass(frozen=True)
class Name:
    """ 名前 """
    value: str

@dataclasses.dataclass(frozen=True)
class NameEn:
    """ 名前 (英語表記) """
    value: str

@dataclasses.dataclass(frozen=True)
class SortNumber:
    """ ソート番号 """
    value: int

@dataclasses.dataclass
class Cast:
    cast_id: CastId
    name: Name
    name_en: NameEn
    sort_number: SortNumber
    work: Work
    character: Character
    person: People

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.cast_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_en": dataclasses.asdict(self.name_en)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "work": self.work.to_dict(),
            "character": self.character.to_dict(),
            "person": self.person.to_dict(),
        }

    @staticmethod
    def from_dict(cast_dict: dict) -> "Cast":
        return Cast(
            cast_id = CastId(cast_dict["id"]),
            name = Name(cast_dict["name"]),
            name_en = NameEn(cast_dict["name_en"]),
            sort_number = SortNumber(cast_dict["sort_number"]),
            work = Work.from_dict(cast_dict["work"]),
            character = Character.from_dict(cast_dict["character"]),
            person = People.from_dict(cast_dict["person"]),
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
