import dataclasses

from model.people import People
from model.people import Peoples
from request import ApiRequests
from request_filter import PeopleRequestParams


@dataclasses.dataclass
class PeopleService:
    def find_people_info(self, people_id: int) -> People:
        api = ApiRequests()
        params = PeopleRequestParams(filter_ids=people_id).to_dict()
        res = api.people(params=params)
        return People(**res["people"][0])

    def find_all_people_info(self) -> Peoples:
        # TODO データ永続化処理で使用する
        peoples = Peoples()
        count = 0
        api = ApiRequests()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            count += 1
            print(count)
            params = PeopleRequestParams(per_page=per_page, page=page).to_dict()
            res = api.people(params=params)
            page = res["next_page"]
            for people in res["people"]:
                peoples.append(People(**people))
        return peoples
