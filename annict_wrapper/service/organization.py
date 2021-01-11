import dataclasses

from annict_wrapper.model.organization import Organization
from annict_wrapper.model.organization import Organizations
from annict_wrapper.request import ApiRequests
from annict_wrapper.request_filter import OrganizationRequestParams


@dataclasses.dataclass
class OrganizationService:
    api: ApiRequests

    def find_organization_info(self, organization_id: int) -> Organization:
        params = OrganizationRequestParams(filter_ids=organization_id).to_dict()
        res = self.api.organizations(params=params)
        try:
            return Organization.from_dict(res["organizations"][0])
        except Exception as e:
            raise e

    def find_all_organization_info(self) -> Organizations:
        # TODO データ永続化処理で使用する
        organizations = Organizations()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = OrganizationRequestParams(per_page=per_page, page=page).to_dict()
            res = self.api.organizations(params=params)
            page = res["next_page"]
            for o in res["organizations"]:
                organizations.append(Organization.from_dict(o))
        return organizations
