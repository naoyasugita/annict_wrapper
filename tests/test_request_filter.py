import pytest

from annict_wrapper.request_filter import CastRequestParams
from annict_wrapper.request_filter import CharacterRequestParams
from annict_wrapper.request_filter import EpisodeRequestParams
from annict_wrapper.request_filter import OrganizationRequestParams
from annict_wrapper.request_filter import PeopleRequestParams
from annict_wrapper.request_filter import ProgramRequestParams
from annict_wrapper.request_filter import SeriesRequestParams
from annict_wrapper.request_filter import StaffRequestParams
from annict_wrapper.request_filter import WorkRequestParams


class TestCharacterRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_name": "株式会社",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
        }
        character_request_params = CharacterRequestParams(**params)
        assert character_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        character_request_params = CharacterRequestParams(**params)
        assert character_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        character_request_params = CharacterRequestParams(**params)
        assert character_request_params.to_dict() == params


class TestCastRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_work_id": 1111,
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_sort_number": "desc",
        }
        cast_request_params = CastRequestParams(**params)
        assert cast_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        cast_request_params = CastRequestParams(**params)
        assert cast_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        cast_request_params = CastRequestParams(**params)
        assert cast_request_params.to_dict() == params


class TestProgramRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_channel_ids": 123,
            "filter_work_ids": 1111,
            "filter_started_at_gt": "2016/05/06 21:10",
            "filter_started_at_lt": "2016/05/06 21:10",
            "filter_unwatched": True,
            "filter_rebroadcast": True,
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_started_at": "desc",
        }
        program_request_params = ProgramRequestParams(**params)
        assert program_request_params.to_dict() == params

    def test_to_dict_when_format_of_started_at_is_different(self):
        params = {
            "filter_started_at_gt": "2016-05-06 21:10",
        }
        with pytest.raises(ValueError):
            ProgramRequestParams(**params)

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        program_request_params = ProgramRequestParams(**params)
        assert program_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        program_request_params = ProgramRequestParams(**params)
        assert program_request_params.to_dict() == params


class TestStaffRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_work_id": 1111,
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_sort_number": "desc",
        }
        staff_request_params = StaffRequestParams(**params)
        assert staff_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        staff_request_params = StaffRequestParams(**params)
        assert staff_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        staff_request_params = StaffRequestParams(**params)
        assert staff_request_params.to_dict() == params


class TestEpisodeequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_work_id": 123,
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_sort_number": "desc",
        }
        episode_request_params = EpisodeRequestParams(**params)
        assert episode_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        episode_request_params = EpisodeRequestParams(**params)
        assert episode_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        episode_request_params = EpisodeRequestParams(**params)
        assert episode_request_params.to_dict() == params


class TestSeriesRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_name": "株式会社",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
        }
        series_request_params = SeriesRequestParams(**params)
        assert series_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        series_request_params = SeriesRequestParams(**params)
        assert series_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        series_request_params = SeriesRequestParams(**params)
        assert series_request_params.to_dict() == params


class TestOrganizationRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_name": "株式会社",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
        }
        organization_request_params = OrganizationRequestParams(**params)
        assert organization_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        organization_request_params = WorkRequestParams(**params)
        assert organization_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        organization_request_params = WorkRequestParams(**params)
        assert organization_request_params.to_dict() == params


class TestWorkRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_season": "2016-spring",
            "filter_title": "shirobako",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_season": "desc",
            "sort_watchers_count": "desc",
        }
        work_request_params = WorkRequestParams(**params)
        assert work_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        work_request_params = WorkRequestParams(**params)
        assert work_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        work_request_params = WorkRequestParams(**params)
        assert work_request_params.to_dict() == params


class TestPeopleRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_name": "井上",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
        }
        people_request_params = PeopleRequestParams(**params)
        assert people_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        people_request_params = PeopleRequestParams(**params)
        assert people_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        people_request_params = PeopleRequestParams(**params)
        assert people_request_params.to_dict() == params
