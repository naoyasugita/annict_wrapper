import dataclasses
from typing import List
from typing import Union

from sora.model.cours import Cours
from sora.model.cours import CoursList
from sora.request import SoraApiClient


@dataclasses.dataclass
class CoursService:
    api: SoraApiClient

    def fetch_all_cours_info(self) -> CoursList:
        try:
            cours_list = CoursList()
            res = self.api.cours()
            for _, cours in res.items():
                cours_list.append(Cours.from_dict(cours))
            return cours_list
        except Exception as e:
            raise e

    def get_latest_cours(self) -> Cours:
        try:
            res = self.api.cours()
            latest_index = str(max(map(int, list(res))))
            return Cours.from_dict(res[latest_index])
        except Exception as e:
            raise e

    def find_cours_by_year_season(self, year: int, season: str) -> Cours:
        try:
            cours_list = self.fetch_all_cours_info()
            return  cours_list.find_specific_cours(year, season)
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
