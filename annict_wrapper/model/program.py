import dataclasses
from datetime import datetime
from typing import Dict
from typing import List
from typing import Union

from annict_wrapper.model.episode import Episode
from annict_wrapper.model.work import Work


@dataclasses.dataclass
class Channel:
    id: int
    name: str


@dataclasses.dataclass
class Program:
    id: int
    started_at: datetime
    is_rebroadcast: bool
    channel: Dict[int, str]
    work: Dict[str, Union[int, str]]
    episode: Dict[str, Union[int, str]]

    def __post_init__(self) -> None:
        self.channel = Channel(**self.channel)
        self.work = Work(**self.work)
        self.episode = Episode(**self.episode)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Programs:
    _list: List[Program] = dataclasses.field(default_factory=list)

    def append(self, program: Program) -> None:
        if isinstance(program, Program):
            self._list.append(program)
        else:
            raise TypeError("data is not program")

    def to_dict(self) -> list:
        return [l.to_dict() for l in self._list]
