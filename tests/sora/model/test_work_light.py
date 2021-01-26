import pytest
from sora.model.work_light import WorkLight
from sora.model.work_light import WorkLightList


class TestWorkLightModel:
    def test_to_dict(self, fixture_work_light):
        actual = fixture_work_light["to_dict"]
        work_light = fixture_work_light["work_light"]

        excepted = work_light.to_dict()

        assert actual == excepted

    def test_from_dict(self, fixture_work_light):
        actual = fixture_work_light["work_light"]

        work_light_dict = fixture_work_light["work_light_dict"]
        excepted = WorkLight.from_dict(work_light_dict)

        assert actual == excepted


class TestWorkLightListModel:
    def test_work_light_list_append_when_type_ok(self, fixture_work_light):
        work_light_list = WorkLightList()
        work_light = fixture_work_light["work_light"]
        work_light_2 = fixture_work_light["work_light"]
        work_light_list.append(work_light)
        work_light_list.append(work_light_2)

        excepted = len(work_light_list._list)

        actual = 2

        assert actual == excepted

    def test_work_light_list_append_when_type_error(self):
        work_light_list = WorkLightList()
        with pytest.raises(TypeError):
            work_light_list.append("dammy")

    def test_work_light_list_to_dict(self, fixture_work_light):
        work_light_list = WorkLightList()
        work_light = fixture_work_light["work_light"]
        work_light_list.append(work_light)
        excepted = work_light_list.to_dict()

        work_light_dict = fixture_work_light["to_dict"]
        actual = [work_light_dict]

        assert actual == excepted
