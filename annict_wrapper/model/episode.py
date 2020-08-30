import dataclasses
from typing import Dict
from typing import Optional
from typing import Union

from annict_wrapper.model.work import Work


@dataclasses.dataclass
class Episode:
    id: int
    number: Optional[int]
    number_text: str
    sort_number: int
    title: str
    records_count: int
    record_comments_count: int
    work: Dict[str, Union[int, str]]
    prev_episode: Optional[Dict[str, Optional[Union[int, str]]]] = None
    next_episode: Optional[Dict[str, Optional[Union[int, str]]]] = None

    def __post_init__(self) -> None:
        self.work = Work(**self.work)
        if self.prev_episode is not None:
            self.prev_episode = PrevEpisode(**self.prev_episode)
        if self.next_episode is not None:
            self.next_episode = NextEpisode(**self.next_episode)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class PrevEpisode:
    id: int
    number: Optional[int]
    number_text: str
    sort_number: int
    title: str
    records_count: int
    record_comments_count: int

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class NextEpisode:
    id: int
    number: Optional[int]
    number_text: str
    sort_number: int
    title: str
    records_count: int
    record_comments_count: int

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
