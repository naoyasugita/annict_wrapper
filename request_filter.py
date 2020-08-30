import dataclasses
from datetime import datetime
from typing import Optional

from utils import delete_none_for_dict


@dataclasses.dataclass
class WorkRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_season: Optional[str] = None
    filter_title: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc
    sort_season: Optional[str] = None  # desc or asc
    sort_watchers_count: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))


@dataclasses.dataclass
class PeopleRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_name: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))


@dataclasses.dataclass
class OrganizationRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_name: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))


@dataclasses.dataclass
class SeriesRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_name: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))


@dataclasses.dataclass
class EpisodeRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_name: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc
    sort_sort_number: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))


@dataclasses.dataclass
class StaffRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_work_id: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc
    sort_sort_number: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))


@dataclasses.dataclass
class ProgramRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_channel_ids: Optional[int] = None
    filter_work_ids: Optional[int] = None
    filter_started_at_gt: Optional["datatime"] = None
    filter_started_at_lt: Optional["datatime"] = None
    filter_unwatched: Optional[bool] = None
    filter_rebroadcast: Optional[bool] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc
    sort_started_at: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))


@dataclasses.dataclass
class CharacterRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_name: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))
