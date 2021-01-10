import dataclasses
from typing import Dict
from typing import Optional
from typing import Union

from annict_wrapper.model.work import Work


@dataclasses.dataclass(frozen=True)
class EpisodeId:
    """ エピソードのID """

    value: int


@dataclasses.dataclass(frozen=True)
class Number:
    """ エピソードの話数 """

    value: Optional[int]


@dataclasses.dataclass(frozen=True)
class NumberText:
    """ エピソードの話数 (表記用) """

    value: str


@dataclasses.dataclass(frozen=True)
class SortNumber:
    """ ソート用の番号。話数でソートすると正しく並べられないケースがあるため、このフィールドが存在します。 """

    value: int


@dataclasses.dataclass(frozen=True)
class Title:
    """ サブタイトル """

    value: str


@dataclasses.dataclass(frozen=True)
class RecordsCount:
    """ 記録数 """

    value: int


@dataclasses.dataclass(frozen=True)
class RecordCommentsCount:
    """ 感想付きの記録数 """

    value: int


@dataclasses.dataclass
class PrevEpisode:
    episode_id: EpisodeId
    number: Number
    number_text: NumberText
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
            "number_text": dataclasses.asdict(self.number_text)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "title": dataclasses.asdict(self.title)["value"],
            "records_count": dataclasses.asdict(self.records_count)["value"],
            "record_comments_count": dataclasses.asdict(self.record_comments_count)[
                "value"
            ],
        }

    @staticmethod
    def from_dict(episode_dict: dict) -> "PrevEpisode":
        return PrevEpisode(
            episode_id=EpisodeId(episode_dict["id"]),
            number=Number(episode_dict["number"])
            if episode_dict.get("number") is not None
            else None,
            number_text=NumberText(episode_dict["number_text"]),
            sort_number=SortNumber(episode_dict["sort_number"]),
            title=Title(episode_dict["title"]),
            records_count=RecordsCount(episode_dict["records_count"]),
            record_comments_count=RecordCommentsCount(
                episode_dict["record_comments_count"]
            ),
        )


@dataclasses.dataclass
class NextEpisode:
    episode_id: EpisodeId
    number: Number
    number_text: NumberText
    sort_number: SortNumber
    title: Title
    records_count: RecordsCount
    record_comments_count: RecordCommentsCount

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.episode_id)["value"],
            "number": dataclasses.asdict(self.number)["value"],
            "number_text": dataclasses.asdict(self.number_text)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "title": dataclasses.asdict(self.title)["value"],
            "records_count": dataclasses.asdict(self.records_count)["value"],
            "record_comments_count": dataclasses.asdict(self.record_comments_count)[
                "value"
            ],
        }

    @staticmethod
    def from_dict(episode_dict: dict) -> "NextEpisode":
        return NextEpisode(
            episode_id=EpisodeId(episode_dict["id"]),
            number=Number(episode_dict["number"]),
            number_text=NumberText(episode_dict["number_text"]),
            sort_number=SortNumber(episode_dict["sort_number"]),
            title=Title(episode_dict["title"]),
            records_count=RecordsCount(episode_dict["records_count"]),
            record_comments_count=RecordCommentsCount(
                episode_dict["record_comments_count"]
            ),
        )


@dataclasses.dataclass
class Episode:
    episode_id: EpisodeId
    number: Number
    number_text: NumberText
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
            "number": dataclasses.asdict(self.number)["value"],
            "number_text": dataclasses.asdict(self.number_text)["value"],
            "sort_number": dataclasses.asdict(self.sort_number)["value"],
            "title": dataclasses.asdict(self.title)["value"],
            "records_count": dataclasses.asdict(self.records_count)["value"],
            "record_comments_count": dataclasses.asdict(self.record_comments_count)[
                "value"
            ],
            "work": self.work.to_dict(),
            "prev_episode": self.prev_episode.to_dict()
            if self.prev_episode is not None
            else None,
            "next_episode": self.next_episode.to_dict()
            if self.next_episode is not None
            else None,
        }

    @staticmethod
    def from_dict(episode_dict: dict) -> "Episode":
        return Episode(
            episode_id=EpisodeId(episode_dict["id"]),
            number=Number(episode_dict["number"]),
            number_text=NumberText(episode_dict["number_text"]),
            sort_number=SortNumber(episode_dict["sort_number"]),
            title=Title(episode_dict["title"]),
            records_count=RecordsCount(episode_dict["records_count"]),
            record_comments_count=RecordCommentsCount(
                episode_dict["record_comments_count"]
            ),
            work=Work.from_dict(episode_dict["work"]),
            prev_episode=PrevEpisode.from_dict(episode_dict["prev_episode"])
            if episode_dict.get("prev_episode") is not None
            else None,
            next_episode=NextEpisode.from_dict(episode_dict["next_episode"])
            if episode_dict.get("next_episode") is not None
            else None,
        )
