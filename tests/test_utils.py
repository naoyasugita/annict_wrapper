import pytest

from annict_wrapper.model.work import Cool
from annict_wrapper.utils import create_season_by_year_and_cool
from annict_wrapper.utils import delete_none_for_dict


class TestDeleteNoneForDict:
    def test_delete_none_for_dict_when_not_in_none(self):
        dic = {
            "fields": "id",
            "filter_ids": 123,
        }
        assert delete_none_for_dict(dic) == dic

    def test_delete_none_for_dict_when_in_none(self):
        dic = {
            "fields": "id",
            "filter_ids": None,
        }

        assert delete_none_for_dict(dic) == {"fields": "id"}

    def test_delete_none_for_dict_when_all_none(self):
        dic = {
            "fields": None,
            "filter_ids": None,
        }
        assert delete_none_for_dict(dic) == {}


class TestCreateSeasonByYearAndCool:
    def test_create_season_by_year_and_cool(self):
        year = 2020
        cool = Cool["spring"]
        actual = str(year) + "-" + cool.name
        expected = create_season_by_year_and_cool(year, cool)
        assert actual == expected
