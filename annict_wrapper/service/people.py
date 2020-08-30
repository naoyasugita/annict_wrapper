import dataclasses

from annict_wrapper.model.people import People
from annict_wrapper.model.people import Peoples
from annict_wrapper.request import ApiRequests
from annict_wrapper.request_filter import PeopleRequestParams


@dataclasses.dataclass
class PeopleService:
    api: ApiRequests

    def find_people_info(self, people_id: int) -> People:
        params = PeopleRequestParams(filter_ids=people_id).to_dict()
        res = self.api.people(params=params)
        try:
            return People(**res["people"][0])
        except Exception as e:
            raise e

    def find_all_people_info(self) -> Peoples:
        # TODO データ永続化処理で使用する
        peoples = Peoples()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = PeopleRequestParams(per_page=per_page, page=page).to_dict()
            res = self.api.people(params=params)
            page = res["next_page"]
            for people in res["people"]:
                peoples.append(People(**people))
        return peoples
