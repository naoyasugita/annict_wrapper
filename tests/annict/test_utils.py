from datetime import datetime

import pytest
from annict.model.series import Series
from annict.model.work import Cours
from annict.utils import check_date_format
from annict.utils import create_season_by_year_and_cours
from annict.utils import delete_none_for_dict
from annict.utils import from_bool
from annict.utils import from_datetime
from annict.utils import from_int
from annict.utils import from_none
from annict.utils import from_str
from annict.utils import to_class


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


class TestCreateSeasonByYearAndCours:
    def test_create_season_by_year_and_cours(self):
        year = 2020
        cours = Cours["spring"]
        expected = create_season_by_year_and_cours(year, cours)

        actual = str(year) + "-" + cours.name

        assert actual == expected


class TestCheckDateFormat:
    def test_check_date_format(self):
        dt = "2016/05/06 21:10"
        expected = check_date_format(dt)

        actual = True

        assert actual == expected

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


class TestTypeChecker:
    def test_from_int_when_int(self):
        actual = 1
        expected = from_int(1)

        assert actual == expected

    def test_from_int_when_str(self):
        with pytest.raises(AssertionError):
            expected = from_int("1")

    def test_from_int_when_bool(self):
        with pytest.raises(AssertionError):
            expected = from_int(True)

    def test_from_str_when_str(self):
        actual = "test"
        expected = from_str("test")

        assert actual == expected

    def test_from_str_when_int(self):
        with pytest.raises(AssertionError):
            expected = from_str(1)

    def test_from_datetime_when_datetime_1(self):
        """ YYYY-MM-DD hh:mm """
        actual = datetime(2016, 5, 6, 21, 10)
        expected = from_datetime("2016-05-06 21:10")

        assert actual == expected

    def test_from_datetime_when_datetime_2(self):
        """ YYYYMMDDhhmmss """
        actual = datetime(2020, 10, 10, 11, 11, 22)
        expected = from_datetime("20201010111122")

        assert actual == expected

    def test_from_datetime_when_datetime_3(self):
        """ YYYYMMDDhhmmss """
        actual = datetime(2020, 10, 10, 11, 11, 22)
        expected = from_datetime("20201010111122")

        assert actual == expected

    def test_from_datetime_when_int(self):
        """ YYYYMMDDhhmmss """
        with pytest.raises(TypeError):
            expected = from_datetime(123)

    def test_from_bool_when_bool(self):
        actual = True
        expected = from_bool(True)

        assert actual == expected

    def test_from_bool_when_int(self):
        with pytest.raises(AssertionError):
            expected = from_bool(1)

    def test_from_bool_when_str(self):
        with pytest.raises(AssertionError):
            expected = from_bool("True")

    def test_from_none_when_none(self):
        actual = None
        expected = from_none(None)

        assert actual == expected

    def test_from_none_when_int(self):
        with pytest.raises(AssertionError):
            expected = from_none(1)

    def test_to_class_when_class(self, fixture_series):
        actual = fixture_series["series_dict"]
        series = fixture_series["series"]
        expected = to_class(Series, series)

        assert actual == expected

    def test_to_class_when_not_class(self, fixture_series, fixture_work):
        actual = fixture_work["work_dict"]
        work = fixture_work["work"]
        with pytest.raises(AssertionError):
            expected = to_class(Series, work)
