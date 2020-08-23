import dataclasses
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
