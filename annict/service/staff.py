import dataclasses

from annict.model.staff import Staff
from annict.model.staff import Staffs
from annict.request import ApiRequests
from annict.request_filter import StaffRequestParams


@dataclasses.dataclass
class StaffService:
    api: ApiRequests

    def find_staff_info(self, staff_id: int) -> Staff:
        params = StaffRequestParams(filter_ids=staff_id).to_dict()
        res = self.api.staffs(params=params)
        try:
            return Staff.from_dict(res["staffs"][0])
        except Exception as e:
            raise e

    def find_staff_info_by_work_id(self, work_id: int) -> Staffs:
        staffs = Staffs()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = StaffRequestParams(
                per_page=per_page, page=page, filter_work_id=work_id
            ).to_dict()
            res = self.api.staffs(params=params)
            page = res["next_page"]
            for staff in res["staffs"]:
                staffs.append(Staff.from_dict(staff))
        return staffs
