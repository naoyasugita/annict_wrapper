import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict_wrapper.model.organization import Organization
from annict_wrapper.model.people import People
from annict_wrapper.model.work import Work


@dataclasses.dataclass
class Staff:
    id: int
    name: str
    name_en: str
    role_text: str
    role_other: str
    role_other_en: str
    sort_number: int
    work: Dict[str, Union[int, str]]
    organization: Optional[Dict[str, Union[int, str]]] = None
    person: Optional[Dict[str, Union[int, str]]] = None

    def __post_init__(self) -> None:
        self.work = Work(**self.work)
        if self.organization is not None:
            self.organization = Organization(**self.organization)
        if self.person is not None:
            self.person = People(**self.person)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Staffs:
    _list: List[Staff] = dataclasses.field(default_factory=list)

    def append(self, staff: Staff) -> None:
        if isinstance(staff, Staff):
            self._list.append(staff)
        else:
            raise TypeError("data is not staff")

    def to_dict(self) -> list:
        return [l.to_dict() for l in self._list]
