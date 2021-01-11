import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict_wrapper.model.organization import Organization
from annict_wrapper.model.people import People
from annict_wrapper.model.work import Work
from annict_wrapper.utils import from_bool
from annict_wrapper.utils import from_datetime
from annict_wrapper.utils import from_int
from annict_wrapper.utils import from_str
from annict_wrapper.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class StaffId:
    """ スタッフのID """

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
class NameEn:
    """ 名前 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)

@dataclasses.dataclass(frozen=True)
class RoleText:
    """ 担当。主要な担当名 (監督やアニメーション制作など) が登録されています。 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)

@dataclasses.dataclass(frozen=True)
class RoleOther:
    """ その他の担当 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)

@dataclasses.dataclass(frozen=True)
class RoleOtherEn:
    """ その他の担当 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)

@dataclasses.dataclass(frozen=True)
class SortNumber:
    """ ソート番号 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)

@dataclasses.dataclass
class Staff:
    staff_id: StaffId
    name: Name
    name_en: NameEn
    role_text: RoleText
    role_other: RoleOther
    role_other_en: RoleOtherEn
    sort_number: SortNumber
    work: Work
    organization: Optional[Organization] = None
    person: Optional[People] = None

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.staff_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_en": dataclasses.asdict(self.name_en)["value"],
            "role_text": dataclasses.asdict(self.role_text)["value"],
            "role_other": dataclasses.asdict(self.role_other)["value"],
            "role_other_en": dataclasses.asdict(self.role_other_en)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "work": to_class(Work, self.work),
            "organization": to_class(Organization, self.organization)
            if self.organization is not None
            else None,
            "person": to_class(People, self.person) if self.person is not None else None,
        }

    @staticmethod
    def from_dict(staff_dict: dict) -> "Staff":
        assert isinstance(staff_dict, dict)
        return Staff(
            staff_id=StaffId(staff_dict["id"]),
            name=Name(staff_dict["name"]),
            name_en=NameEn(staff_dict["name_en"]),
            role_text=RoleText(staff_dict["role_text"]),
            role_other=RoleOther(staff_dict["role_other"]),
            role_other_en=RoleOtherEn(staff_dict["role_other_en"]),
            sort_number=SortNumber(staff_dict["sort_number"]),
            work=Work.from_dict(work_dict=staff_dict["work"]),
            organization=Organization.from_dict(
                organization_dict=staff_dict["organization"]
            )
            if staff_dict.get("organization") is not None
            else None,
            person=People.from_dict(people_dict=staff_dict["person"])
            if staff_dict.get("person") is not None
            else None,
        )


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
