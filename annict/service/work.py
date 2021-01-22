import dataclasses

from annict.model.work import Cool
from annict.model.work import Work
from annict.model.work import Works
from annict.request import AnnictApiClient
from annict.request_filter import WorkRequestParams
from annict.utils import create_season_by_year_and_cool
from tqdm import tqdm


@dataclasses.dataclass
class WorkService:
    api: AnnictApiClient

    def find_work_info(self, work_id: int) -> Work:
        params = WorkRequestParams(filter_ids=work_id).to_dict()
        res = self.api.works(params=params)
        try:
            return Work.from_dict(res["works"][0])
        except Exception as e:
            raise e

    def find_all_work_info(self) -> Works:
        # TODO データ永続化処理で使用する
        works = Works()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = WorkRequestParams(per_page=per_page, page=page).to_dict()
            res = self.api.works(params=params)
            page = res["next_page"]
            for work in res["works"]:
                works.append(Work.from_dict(work))
        return works

    def find_work_info_by_season(self, year: int, cool: Cool) -> Works:
        # TODO データ永続化処理で使用する
        works = Works()
        per_page = 50  # limit_count
        page = 1  # init_page
        filter_season = create_season_by_year_and_cool(year, cool)
        while page is not None:
            params = WorkRequestParams(
                per_page=per_page, page=page, filter_season=filter_season
            ).to_dict()
            res = self.api.works(params=params)
            page = res["next_page"]
            for work in tqdm(res["works"]):
                works.append(Work.from_dict(work))
        return works
