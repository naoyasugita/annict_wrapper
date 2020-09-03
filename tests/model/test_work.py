import pytest

from annict_wrapper.model.work import Work
from annict_wrapper.model.work import Works


class TestWorkModel:
    def test_to_dict(self, fixture_work):
        work_dict = fixture_work["work_dict"]
        assert Work(**work_dict).to_dict() == work_dict


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
