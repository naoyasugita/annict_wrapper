import pytest
from sora.model.cours import Cours
from sora.model.cours import CoursList
from sora.model.cours import SeasonValue
from sora.model.cours import Year


class TestYear:
    def test_create_instance_when_too_long(self):
        with pytest.raises(AssertionError):
            expected = Year(12345)

    def test_create_instance_when_too_short(self):
        with pytest.raises(AssertionError):
            expected = Year(123)


class TestSeasonValue:
    def test_to_string_when_winter(self):
        actual = "winter"

        expected = SeasonValue(1).to_string()

        assert actual == expected

    def test_to_string_when_spring(self):
        actual = "spring"

        expected = SeasonValue(2).to_string()

        assert actual == expected

    def test_to_string_when_summer(self):
        actual = "summer"

        expected = SeasonValue(3).to_string()

        assert actual == expected

    def test_to_string_when_autumn(self):
        actual = "autumn"

        expected = SeasonValue(4).to_string()

        assert actual == expected

    def test_to_number_when_winter(self):
        actual = 1

        expected = SeasonValue(1).to_number()

        assert actual == expected

    def test_to_number_when_spring(self):
        actual = 2

        expected = SeasonValue(2).to_number()

        assert actual == expected

    def test_to_number_when_summer(self):
        actual = 3

        expected = SeasonValue(3).to_number()

        assert actual == expected

    def test_to_number_when_autumn(self):
        actual = 4

        expected = SeasonValue(4).to_number()

        assert actual == expected

    def test_create_instance_when_invalid_number(self):
        with pytest.raises(ValueError):
            expected = SeasonValue(5)

    def test_create_instance_when_string(self):
        with pytest.raises(ValueError):
            expected = SeasonValue("1")


class TestCoursModel:
    def test_to_dict(self, fixture_cours):
        actual = fixture_cours["to_dict"]
        cours = fixture_cours["cours"]

        expected = cours.to_dict()

        assert actual == expected

    def test_from_dict(self, fixture_cours):
        actual = fixture_cours["cours"]

        cours_dict = fixture_cours["cours_dict"]
        expected = Cours.from_dict(cours_dict)

        assert actual == expected

    def test_is_target_cours_when_true(self, fixture_cours):
        actual = True

        cours = fixture_cours["cours"]
        expected = cours.is_target_cours(2014, "autumn")

        assert actual == expected

    def test_is_target_cours_when_false(self, fixture_cours):
        actual = False

        cours = fixture_cours["cours"]
        expected = cours.is_target_cours(2015, "autumn")

        assert actual == expected


class TestCoursModel:
    def test_cours_list_append_when_type_ok(self, fixture_cours):
        cours_list = CoursList()
        cours = fixture_cours["cours"]
        cours_2 = fixture_cours["cours"]
        cours_list.append(cours)
        cours_list.append(cours_2)

        expected = len(cours_list._list)

        actual = 2

        assert actual == expected

    def test_cours_list_append_when_type_error(self):
        cours_list = CoursList()
        with pytest.raises(TypeError):
            cours_list.append("dammy")

    def test_works_to_dict(self, fixture_cours):
        cours_list = CoursList()
        cours = fixture_cours["cours"]
        cours_list.append(cours)
        expected = cours_list.to_dict()

        cours_dict = fixture_cours["to_dict"]
        actual = [cours_dict]

        assert actual == expected
