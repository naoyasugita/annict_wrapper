import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict_wrapper.model.character import Character
from annict_wrapper.model.people import People
from annict_wrapper.model.work import Work


@dataclasses.dataclass
class Cast:
    id: int
    name: str
    name_en: str
    sort_number: int
    work: Dict[str, Union[int, str]]
    character: Optional[Dict[str, Union[int, str]]]
    person: Optional[Dict[str, Union[int, str]]]

    def __post_init__(self) -> None:
        self.work = Work(**self.work)
        self.character = Character(**self.character)
        self.person = People(**self.person)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


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
