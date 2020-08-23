import dataclasses

from model.organization import Organization
from model.organization import Organizations
from request import ApiRequests
from request_filter import OrganizationRequestParams


@dataclasses.dataclass
class OrganizationService:
    def find_organization_info(self, organization_id: int) -> Organization:
        api = ApiRequests()
        params = OrganizationRequestParams(filter_ids=organization_id).to_dict()
        res = api.organizations(params=params)
        return Organization(**res["organizations"][0])

    def find_all_organization_info(self) -> Organizations:
        # TODO データ永続化処理で使用する
        organizations = Organizations()
        api = ApiRequests()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = OrganizationRequestParams(per_page=per_page, page=page).to_dict()
            res = api.organizations(params=params)
            page = res["next_page"]
            for o in res["organizations"]:
                print(o)
                organizations.append(Organization(**o))
        return organizations
