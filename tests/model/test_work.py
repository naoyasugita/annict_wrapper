import pytest

from annict_wrapper.model.work import Cool
from annict_wrapper.model.work import Work
from annict_wrapper.model.work import Works


class TestWorkModel:
    def test_to_dict(self, fixture_work):
        work_dict = fixture_work["work_dict"]
        assert Work(**work_dict).to_dict() == work_dict

    def test_get_cool(self, fixture_work):
        release_year, season = fixture_work["work_dict"]["season_name"].split("-")
        work = fixture_work["work"]
        assert work.get_cool() == (int(release_year), Cool[season])


class TestWorksModel:
    def test_works_append_when_type_ok(self, fixture_work):
        works = Works()
        work = fixture_work["work"]
        work_2 = fixture_work["work"]
        works.append(work)
        works.append(work_2)
        assert len(works._list) == 2

    def test_works_append_when_type_error(self):
        works = Works()
        with pytest.raises(TypeError):
            works.append("dammy")

    def test_works_to_dict(self, fixture_work):
        works = Works()
        work = fixture_work["work"]
        work_dict = fixture_work["work_dict"]
        works.append(work)
        assert works.to_dict() == [work_dict]

    def test_find_by_media(self, fixture_work, fixture_work_movie):
        works = Works()
        works.append(fixture_work["work"])  # tv
        works.append(fixture_work["work"])  # tv
        works.append(fixture_work["work"])  # tv
        works.append(fixture_work_movie["work"])  # movie

        assert len(works.find_by_media("tv")) == 3

