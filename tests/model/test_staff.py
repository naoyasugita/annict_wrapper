import pytest

from annict_wrapper.model.staff import Staff
from annict_wrapper.model.staff import Staffs


class TestStaffModel:
    def test_to_dict_when_org(self, fixture_staff_when_org):
        staff_dict = fixture_staff_when_org["staff_dict"]
        assert Staff(**staff_dict).to_dict() == staff_dict

    def test_to_dict_when_person(self, fixture_staff_when_person):
        staff_dict = fixture_staff_when_person["staff_dict"]
        assert Staff(**staff_dict).to_dict() == staff_dict


class TestStaffsModel:
    def test_staffs_append_when_type_ok(
        self, fixture_staff_when_org, fixture_staff_when_person
    ):
        staffs = Staffs()
        staff = fixture_staff_when_org["staff"]
        staff_2 = fixture_staff_when_person["staff"]
        staffs.append(staff)
        staffs.append(staff_2)
        assert len(staffs._list) == 2

    def test_staffs_append_when_type_error(self):
        staffs = Staffs()
        with pytest.raises(TypeError):
            staffs.append("dammy")

    def test_staffs_to_dict(self, fixture_staff_when_org, fixture_staff_when_person):
        staffs = Staffs()
        staff = fixture_staff_when_org["staff"]
        staff2 = fixture_staff_when_person["staff"]
        staff_dict = fixture_staff_when_org["staff_dict"]
        staff_dict2 = fixture_staff_when_person["staff_dict"]
        staffs.append(staff)
        staffs.append(staff2)
        assert staffs.to_dict() == [staff_dict, staff_dict2]
