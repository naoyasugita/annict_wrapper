import dataclasses
from datetime import datetime
from typing import Dict
from typing import List
from typing import Union

from annict.model.episode import Episode
from annict.model.work import Work
from annict.utils import from_bool
from annict.utils import from_datetime
from annict.utils import from_int
from annict.utils import from_str
from annict.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class ProgramId:
    """ 放送予定ID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class StartedAt:
    """ 放送開始日時 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class IsRebroadcast:
    """ この放送予定が再放送かどうか。再放送の場合は true が、そうでない場合は false が格納されています。 """

    value: bool

    def __post_init__(self) -> None:
        from_bool(self.value)


@dataclasses.dataclass
class Channel:
    """ チャンネル情報 """

    id: int
    name: str

    def __post_init__(self) -> None:
        from_int(self.id)
        from_str(self.name)

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name}

    @staticmethod
    def from_dict(channel_dict: dict) -> "Channel":
        assert isinstance(channel_dict, dict)
        return Channel(id=channel_dict["id"], name=channel_dict["name"])


@dataclasses.dataclass
class Program:
    program_id: ProgramId
    started_at: StartedAt
    is_rebroadcast: IsRebroadcast
    channel: Channel
    work: Work
    episode: Episode

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.program_id)["value"],
            "started_at": dataclasses.asdict(self.started_at)["value"],
            "is_rebroadcast": dataclasses.asdict(self.is_rebroadcast)["value"],
            "channel": to_class(Channel, self.channel),
            "work": to_class(Work, self.work),
            "episode": to_class(Episode, self.episode),
        }

    @staticmethod
    def from_dict(program_dict: dict) -> "Program":
        assert isinstance(program_dict, dict)
        return Program(
            program_id=ProgramId(program_dict["id"]),
            started_at=StartedAt(program_dict["started_at"]),
            is_rebroadcast=IsRebroadcast(program_dict["is_rebroadcast"]),
            channel=Channel.from_dict(program_dict["channel"]),
            work=Work.from_dict(program_dict["work"]),
            episode=Episode.from_dict(program_dict["episode"]),
        )


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
