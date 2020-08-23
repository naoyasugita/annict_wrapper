import dataclasses

from model.staff import Staff
from model.staff import Staffs
from request import ApiRequests
from request_filter import StaffRequestParams


@dataclasses.dataclass
class StaffService:
    def find_staff_info(self, staff_id: int) -> Staff:
        api = ApiRequests()
        params = StaffRequestParams(filter_ids=staff_id).to_dict()
        res = api.staffs(params=params)
        try:
            return Staff(**res["staffs"][0])
        except Exception as e:
            raise e

    def find_staff_info_by_work_id(self, work_id: int) -> Staffs:
        staffs = Staffs()
        api = ApiRequests()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = StaffRequestParams(
                per_page=per_page, page=page, filter_work_id=work_id
            ).to_dict()
            res = api.staffs(params=params)
            page = res["next_page"]
            for staff in res["staffs"]:
                staffs.append(Staff(**staff))
        return staffs
