import pytest
from annict_wrapper.model.staff import Staff
from annict_wrapper.model.staff import Staffs


class TestStaffModel:
    def test_to_dict_when_org(self, fixture_staff_when_org):
        actual = fixture_staff_when_org["staff_dict"]
        staff = fixture_staff_when_org["staff"]

        excepted = staff.to_dict()

        assert actual == excepted

    def test_from_dict_when_person(self, fixture_staff_when_person):
        actual = fixture_staff_when_person["staff"]

        staff_dict = fixture_staff_when_person["staff_dict"]
        excepted = Staff.from_dict(staff_dict)

        assert actual == excepted


class TestStaffsModel:
    def test_staffs_append_when_type_ok(
        self, fixture_staff_when_org, fixture_staff_when_person
    ):
        staffs = Staffs()
        staff = fixture_staff_when_org["staff"]
        staff_2 = fixture_staff_when_person["staff"]
        staffs.append(staff)
        staffs.append(staff_2)
        excepted = len(staffs._list)

        actual = 2

        assert actual == excepted

    def test_staffs_append_when_type_error(self):
        staffs = Staffs()
        with pytest.raises(TypeError):
            staffs.append("dammy")

    def test_staffs_to_dict(self, fixture_staff_when_org, fixture_staff_when_person):
        staffs = Staffs()
        staff = fixture_staff_when_org["staff"]
        staff2 = fixture_staff_when_person["staff"]
        staffs.append(staff)
        staffs.append(staff2)
        excepted = staffs.to_dict()

        staff_dict = fixture_staff_when_org["staff_dict"]
        staff_dict2 = fixture_staff_when_person["staff_dict"]
        actual = [staff_dict, staff_dict2]

        assert actual == excepted
