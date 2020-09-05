from datetime import datetime

import pytest

from annict_wrapper.model.work import Cool
from annict_wrapper.utils import check_date_format
from annict_wrapper.utils import create_season_by_year_and_cool
from annict_wrapper.utils import delete_none_for_dict


class TestDeleteNoneForDict:
    def test_delete_none_for_dict_when_not_in_none(self):
        actual = {
            "fields": "id",
            "filter_ids": 123,
        }

        expected = delete_none_for_dict(actual)

        assert actual == expected

    def test_delete_none_for_dict_when_in_none(self):
        dic = {
            "fields": "id",
            "filter_ids": None,
        }
        expected = delete_none_for_dict(dic)

        actual = {"fields": "id"}

        assert actual == expected

    def test_delete_none_for_dict_when_all_none(self):
        dic = {
            "fields": None,
            "filter_ids": None,
        }
        expected = delete_none_for_dict(dic)

        actual = {}

        assert actual == expected


class TestCreateSeasonByYearAndCool:
    def test_create_season_by_year_and_cool(self):
        year = 2020
        cool = Cool["spring"]
        expected = create_season_by_year_and_cool(year, cool)

        actual = str(year) + "-" + cool.name

        assert actual == expected


class TestCheckDateFormat:
    def test_check_date_format(self):
        dt = "2016/05/06 21:10"
        excepted = check_date_format(dt)

        actual = True

        assert actual == excepted

    def test_check_date_format_when_missed_format_1(self):
        dt = "2016-05-06 21:10"
        expected = check_date_format(dt)

        actual = False

        assert actual == expected

    def test_check_date_format_when_missed_format_2(self):
        dt = "2016/05/06 21:10:12"
        expected = check_date_format(dt)

        actual = False

        assert actual == expected

    def test_check_date_format_when_missed_format_3(self):
        dt = "2016年05月06日 21時10分"
        expected = check_date_format(dt)

        actual = False

        assert actual == expected
