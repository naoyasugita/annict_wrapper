import pytest

from annict_wrapper.model.people import People
from annict_wrapper.model.people import Peoples


class TestPeopleModel:
    def test_to_dict(self, fixture_people):
        people_dict = fixture_people["people_dict"]
        assert People(**people_dict).to_dict() == people_dict


class TestPeoplesModel:
    def test_peoples_append_when_type_ok(self, fixture_people):
        peoples = Peoples()
        people = fixture_people["people"]
        people_2 = fixture_people["people"]
        peoples.append(people)
        peoples.append(people_2)
        assert len(peoples._list) == 2

    def test_peoples_append_when_type_error(self):
        peoples = Peoples()
        with pytest.raises(TypeError):
            peoples.append("dammy")

    def test_peoples_to_dict(self, fixture_people):
        peoples = Peoples()
        people = fixture_people["people"]
        people_dict = fixture_people["people_dict"]
        peoples.append(people)
        assert peoples.to_dict() == [people_dict]
