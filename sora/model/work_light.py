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
class WorkId:
    """ APIで管理するアニメ作品に割り当てられているユニークなID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class Title:
    """ アニメ作品名 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class WorkLight:
    work_id: WorkId
    title: Title

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.work_id)["value"],
            "title": dataclasses.asdict(self.title)["value"],
        }

    @staticmethod
    def from_dict(work_light_dict: dict) -> "WorkLight":
        assert isinstance(work_light_dict, dict)
        return WorkLight(
            WorkId(work_light_dict.get("id")),
            Title(work_light_dict.get("title")),
        )


@dataclasses.dataclass
class WorkLightList:
    _list: List[WorkLight] = dataclasses.field(default_factory=list)

    def append(self, work_light: WorkLight) -> None:
        if isinstance(work_light, WorkLight):
            self._list.append(work_light)
        else:
            raise TypeError("data is not work_light")

    def to_dict(self) -> list:
        return [work_light.to_dict() for work_light in self._list]
