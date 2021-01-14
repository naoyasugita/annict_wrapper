import dataclasses
from typing import Dict
from typing import Optional
from typing import Union

from annict_wrapper.model.work import Work
from annict_wrapper.utils import from_bool
from annict_wrapper.utils import from_datetime
from annict_wrapper.utils import from_int
from annict_wrapper.utils import from_none
from annict_wrapper.utils import from_str
from annict_wrapper.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class EpisodeId:
    """ エピソードのID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class NumberText:
    """ エピソードの話数 (表記用) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Number:
    """ エピソードの話数 """

    value: Optional[int]
    text: NumberText

    def __post_init__(self) -> None:
        if self.value is not None:
            from_int(self.value)
        else:
            from_none(self.value)
        assert isinstance(self.text, NumberText)


@dataclasses.dataclass(frozen=True)
class SortNumber:
    """ ソート用の番号。話数でソートすると正しく並べられないケースがあるため、このフィールドが存在します。 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class Title:
    """ サブタイトル """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class RecordsCount:
    """ 記録数 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class RecordCommentsCount:
    """ 感想付きの記録数 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass
class PrevEpisode:
    episode_id: EpisodeId
    number: Number
    sort_number: SortNumber
    title: Title
    records_count: RecordsCount
    record_comments_count: RecordCommentsCount

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.episode_id)["value"],
            "number": dataclasses.asdict(self.number)["value"]
            if self.number is not None
            else None,
            "number_text": dataclasses.asdict(self.number.text)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "title": dataclasses.asdict(self.title)["value"],
            "records_count": dataclasses.asdict(self.records_count)["value"],
            "record_comments_count": dataclasses.asdict(self.record_comments_count)[
                "value"
            ],
        }

    @staticmethod
    def from_dict(episode_dict: dict) -> "PrevEpisode":
        assert isinstance(episode_dict, dict)
        return PrevEpisode(
            EpisodeId(episode_dict["id"]),
            Number(
                episode_dict["number"]
                if episode_dict.get("number") is not None
                else None,
                NumberText(episode_dict["number_text"]),
            ),
            SortNumber(episode_dict["sort_number"]),
            Title(episode_dict["title"]),
            RecordsCount(episode_dict["records_count"]),
            RecordCommentsCount(episode_dict["record_comments_count"]),
        )


@dataclasses.dataclass
class NextEpisode:
    episode_id: EpisodeId
    number: Number
    sort_number: SortNumber
    title: Title
    records_count: RecordsCount
    record_comments_count: RecordCommentsCount

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.episode_id)["value"],
            "number": dataclasses.asdict(self.number)["value"]
            if self.number is not None
            else None,
            "number_text": dataclasses.asdict(self.number.text)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "title": dataclasses.asdict(self.title)["value"],
            "records_count": dataclasses.asdict(self.records_count)["value"],
            "record_comments_count": dataclasses.asdict(self.record_comments_count)[
                "value"
            ],
        }

    @staticmethod
    def from_dict(episode_dict: dict) -> "NextEpisode":
        assert isinstance(episode_dict, dict)
        return NextEpisode(
            EpisodeId(episode_dict["id"]),
            Number(
                episode_dict["number"]
                if episode_dict.get("number") is not None
                else None,
                NumberText(episode_dict["number_text"]),
            ),
            SortNumber(episode_dict["sort_number"]),
            Title(episode_dict["title"]),
            RecordsCount(episode_dict["records_count"]),
            RecordCommentsCount(episode_dict["record_comments_count"]),
        )


@dataclasses.dataclass
class Episode:
    episode_id: EpisodeId
    number: Number
    sort_number: SortNumber
    title: Title
    records_count: RecordsCount
    record_comments_count: RecordCommentsCount
    work: Work
    prev_episode: Optional[PrevEpisode] = None
    next_episode: Optional[NextEpisode] = None

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.episode_id)["value"],
            "number": dataclasses.asdict(self.number)["value"]
            if self.number is not None
            else None,
            "number_text": dataclasses.asdict(self.number.text)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "title": dataclasses.asdict(self.title)["value"],
            "records_count": dataclasses.asdict(self.records_count)["value"],
            "record_comments_count": dataclasses.asdict(self.record_comments_count)[
                "value"
            ],
            "work": to_class(Work, self.work),
            "prev_episode": to_class(PrevEpisode, self.prev_episode)
            if self.prev_episode is not None
            else None,
            "next_episode": to_class(NextEpisode, self.next_episode)
            if self.next_episode is not None
            else None,
        }

    @staticmethod
    def from_dict(episode_dict: dict) -> "Episode":
        assert isinstance(episode_dict, dict)
        return Episode(
            EpisodeId(episode_dict["id"]),
            Number(
                episode_dict["number"]
                if episode_dict.get("number") is not None
                else None,
                NumberText(episode_dict["number_text"]),
            ),
            SortNumber(episode_dict["sort_number"]),
            Title(episode_dict["title"]),
            RecordsCount(episode_dict["records_count"]),
            RecordCommentsCount(episode_dict["record_comments_count"]),
            Work.from_dict(episode_dict["work"]),
            PrevEpisode.from_dict(episode_dict["prev_episode"])
            if episode_dict.get("prev_episode") is not None
            else None,
            NextEpisode.from_dict(episode_dict["next_episode"])
            if episode_dict.get("next_episode") is not None
            else None,
        )
