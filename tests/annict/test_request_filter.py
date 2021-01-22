import pytest

from annict.request_filter import CastRequestParams
from annict.request_filter import CharacterRequestParams
from annict.request_filter import EpisodeRequestParams
from annict.request_filter import OrganizationRequestParams
from annict.request_filter import PeopleRequestParams
from annict.request_filter import ProgramRequestParams
from annict.request_filter import SeriesRequestParams
from annict.request_filter import StaffRequestParams
from annict.request_filter import WorkRequestParams


class TestCharacterRequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
            "filter_name": "株式会社",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
        }

        character_request_params = CharacterRequestParams(**actual)
        excepted = character_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        character_request_params = CharacterRequestParams(**actual)
        excepted = character_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        character_request_params = CharacterRequestParams(**actual)
        excepted = character_request_params.to_dict()

        assert actual == excepted


class TestCastRequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
            "filter_work_id": 1111,
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_sort_number": "desc",
        }

        cast_request_params = CastRequestParams(**actual)
        excepted = cast_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        cast_request_params = CastRequestParams(**actual)
        excepted = cast_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        cast_request_params = CastRequestParams(**actual)
        excepted = cast_request_params.to_dict()

        assert actual == excepted


class TestProgramRequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
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

        program_request_params = ProgramRequestParams(**actual)
        excepted = program_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_format_of_started_at_is_different(self):
        params = {
            "filter_started_at_gt": "2016-05-06 21:10",
        }

        with pytest.raises(ValueError):
            ProgramRequestParams(**params)

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        program_request_params = ProgramRequestParams(**actual)
        excepted = program_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        program_request_params = ProgramRequestParams(**actual)
        excepted = program_request_params.to_dict()

        assert actual == excepted


class TestStaffRequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
            "filter_work_id": 1111,
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_sort_number": "desc",
        }

        staff_request_params = StaffRequestParams(**actual)
        excepted = staff_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        staff_request_params = StaffRequestParams(**actual)
        excepted = staff_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        staff_request_params = StaffRequestParams(**actual)
        excepted = staff_request_params.to_dict()

        assert actual == excepted


class TestEpisodeequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
            "filter_work_id": 123,
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_sort_number": "desc",
        }

        episode_request_params = EpisodeRequestParams(**actual)
        excepted = episode_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        episode_request_params = EpisodeRequestParams(**actual)
        excepted = episode_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        episode_request_params = EpisodeRequestParams(**actual)
        excepted = episode_request_params.to_dict()

        assert actual == excepted


class TestSeriesRequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
            "filter_name": "株式会社",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
        }

        series_request_params = SeriesRequestParams(**actual)
        excepted = series_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        series_request_params = SeriesRequestParams(**actual)
        excepted = series_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        series_request_params = SeriesRequestParams(**actual)
        excepted = series_request_params.to_dict()

        assert actual == excepted


class TestOrganizationRequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
            "filter_name": "株式会社",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
        }

        organization_request_params = OrganizationRequestParams(**actual)
        excepted = organization_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        organization_request_params = WorkRequestParams(**actual)
        excepted = organization_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        organization_request_params = WorkRequestParams(**actual)
        excepted = organization_request_params.to_dict()

        assert actual == excepted


class TestWorkRequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
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

        work_request_params = WorkRequestParams(**actual)
        excepted = work_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        work_request_params = WorkRequestParams(**actual)
        excepted = work_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        work_request_params = WorkRequestParams(**actual)
        excepted = work_request_params.to_dict()

        assert actual == excepted


class TestPeopleRequestParams:
    def test_to_dict_not_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
            "filter_name": "井上",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
        }

        people_request_params = PeopleRequestParams(**actual)
        excepted = people_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        people_request_params = PeopleRequestParams(**actual)
        excepted = people_request_params.to_dict()

        assert actual == excepted

    def test_to_dict_when_empty(self):
        actual = {}

        people_request_params = PeopleRequestParams(**actual)
        excepted = people_request_params.to_dict()

        assert actual == excepted
