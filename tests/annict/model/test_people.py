import pytest
from annict.model.people import People
from annict.model.people import Peoples


class TestPeopleModel:
    def test_to_dict(self, fixture_people):
        actual = fixture_people["people_dict"]

        people = fixture_people["people"]
        expected = people.to_dict()

        assert actual == expected

    def test_from_dict(self, fixture_people):
        actual = fixture_people["people"]

        people_dict = fixture_people["people_dict"]
        expected = People.from_dict(people_dict)

        assert actual == expected


class TestPeoplesModel:
    def test_peoples_append_when_type_ok(self, fixture_people):
        peoples = Peoples()
        people = fixture_people["people"]
        people_2 = fixture_people["people"]
        peoples.append(people)
        peoples.append(people_2)
        expected = len(peoples._list)

        actual = 2

        assert actual == expected

    def test_peoples_append_when_type_error(self):
        peoples = Peoples()
        with pytest.raises(TypeError):
            peoples.append("dammy")

    def test_peoples_to_dict(self, fixture_people):
        peoples = Peoples()
        people = fixture_people["people"]
        peoples.append(people)
        expected = peoples.to_dict()

        people_dict = fixture_people["people_dict"]
        actual = [people_dict]

        assert actual == expected
