import dataclasses
from datetime import datetime
from typing import Optional

from annict_wrapper.utils import check_date_format
from annict_wrapper.utils import delete_none_for_dict


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
class StartedAt:
    dt: str

    def __post_init__(self):
        if not check_date_format(self.dt):
            raise ValueError(f"dt in missed format. correct format is %Y/%m/%d %H:%M.")


@dataclasses.dataclass
class ProgramRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_channel_ids: Optional[int] = None
    filter_work_ids: Optional[int] = None
    filter_started_at_gt: Optional["str"] = None
    filter_started_at_lt: Optional["str"] = None
    filter_unwatched: Optional[bool] = None
    filter_rebroadcast: Optional[bool] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc
    sort_started_at: Optional[str] = None  # desc or asc

    def __post_init__(self):
        try:
            if self.filter_started_at_gt is not None:
                self.filter_started_at_gt = StartedAt(self.filter_started_at_gt).dt
            if self.filter_started_at_lt is not None:
                self.filter_started_at_lt = StartedAt(self.filter_started_at_lt).dt
        except ValueError:
            raise

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))


@dataclasses.dataclass
class CastRequestParams:
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
class CharacterRequestParams:
    fields: Optional[str] = None
    filter_ids: Optional[int] = None
    filter_name: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None  # max 50
    sort_id: Optional[str] = None  # desc or asc

    def to_dict(self):
        return delete_none_for_dict(dataclasses.asdict(self))
