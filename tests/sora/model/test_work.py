import pytest
# from sora.model.work import Cours
from sora.model.work import Work
from sora.model.work import Works


class TestWorkModel:
    def test_to_dict(self, fixture_work):
        actual = fixture_work["to_dict"]
        work = fixture_work["work"]

        excepted = work.to_dict()

        assert actual == excepted

    def test_from_dict(self, fixture_work):
        actual = fixture_work["work"]

        work_dict = fixture_work["work_dict"]
        excepted = Work.from_dict(work_dict)

        assert actual == excepted

    # def test_get_cours(self, fixture_work):
    #     release_year, season = fixture_work["work"].season_name.value.split("-")
    #     actual = (int(release_year), Cours[season])

    #     excepted = fixture_work["work"].get_cours()

    #     assert actual == excepted


class TestWorksModel:
    def test_works_append_when_type_ok(self, fixture_work):
        works = Works()
        work = fixture_work["work"]
        work_2 = fixture_work["work"]
        works.append(work)
        works.append(work_2)

        excepted = len(works._list)

        actual = 2

        assert actual == excepted

    def test_works_append_when_type_error(self):
        works = Works()
        with pytest.raises(TypeError):
            works.append("dammy")

    def test_works_to_dict(self, fixture_work):
        works = Works()
        work = fixture_work["work"]
        works.append(work)
        excepted = works.to_dict()

        work_dict = fixture_work["to_dict"]
        actual = [work_dict]

        assert actual == excepted
