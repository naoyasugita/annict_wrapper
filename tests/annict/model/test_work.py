import pytest
from annict.model.work import Cours
from annict.model.work import Work
from annict.model.work import Works


class TestWorkModel:
    def test_to_dict(self, fixture_work):
        actual = fixture_work["to_dict"]
        work = fixture_work["work"]

        expected = work.to_dict()

        assert actual == expected

    def test_from_dict(self, fixture_work):
        actual = fixture_work["work"]

        work_dict = fixture_work["work_dict"]
        expected = Work.from_dict(work_dict)

        assert actual == expected


class TestWorksModel:
    def test_works_append_when_type_ok(self, fixture_work):
        works = Works()
        work = fixture_work["work"]
        work_2 = fixture_work["work"]
        works.append(work)
        works.append(work_2)

        expected = len(works._list)

        actual = 2

        assert actual == expected

    def test_works_append_when_type_error(self):
        works = Works()
        with pytest.raises(TypeError):
            works.append("dammy")

    def test_works_to_dict(self, fixture_work):
        works = Works()
        work = fixture_work["work"]
        works.append(work)
        expected = works.to_dict()

        work_dict = fixture_work["to_dict"]
        actual = [work_dict]

        assert actual == expected

    def test_find_by_media(self, fixture_work, fixture_work_movie):
        works = Works()
        works.append(fixture_work["work"])  # tv
        works.append(fixture_work["work"])  # tv
        works.append(fixture_work["work"])  # tv
        works.append(fixture_work_movie["work"])  # movie

        expected = len(works.find_by_media("tv"))

        actual = 3

        assert actual == expected
