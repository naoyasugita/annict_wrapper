import dataclasses
from typing import List
from typing import Union

from sora.model.work import Work
from sora.model.work import Works
from sora.request import SoraApiClient


@dataclasses.dataclass
class WorkService:
    api: SoraApiClient

    def fetch_work_by_year_cours(self, year: int, cours: int) -> List[Union[Work]]:
        try:
            works = Works()
            res = self.api.year_cours(year, cours)
            for work in res:
                works.append(Work.from_dict(work))
            return works
        except Exception as e:
            raise e

    # def find_work_info(self, work_id: int) -> Work:
    #     params = WorkRequestParams(filter_ids=work_id).to_dict()
    #     res = self.api.works(params=params)
    #     try:
    #         return Work.from_dict(res["works"][0])
    #     except Exception as e:
    #         raise e

    # def find_all_work_info(self) -> Works:
    #     # TODO データ永続化処理で使用する
    #     works = Works()
    #     per_page = 50  # limit_count
    #     page = 1  # init_page
    #     while page is not None:
    #         params = WorkRequestParams(per_page=per_page, page=page).to_dict()
    #         res = self.api.works(params=params)
    #         page = res["next_page"]
    #         for work in res["works"]:
    #             works.append(Work.from_dict(work))
    #     return works

    # def find_work_info_by_season(self, year: int, cours: Cours) -> Works:
    #     # TODO データ永続化処理で使用する
    #     works = Works()
    #     per_page = 50  # limit_count
    #     page = 1  # init_page
    #     filter_season = create_season_by_year_and_cours(year, cours)
    #     while page is not None:
    #         params = WorkRequestParams(
    #             per_page=per_page, page=page, filter_season=filter_season
    #         ).to_dict()
    #         res = self.api.works(params=params)
    #         page = res["next_page"]
    #         for work in tqdm(res["works"]):
    #             works.append(Work.from_dict(work))
    #     return works
