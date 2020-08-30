import dataclasses

from annict_wrapper.model.cast import Cast
from annict_wrapper.model.cast import Casts
from annict_wrapper.request import ApiRequests
from annict_wrapper.request_filter import CastRequestParams


@dataclasses.dataclass
class CastService:
    api: ApiRequests

    def find_cast_info(self, cast_id: int) -> Cast:
        params = CastRequestParams(filter_ids=cast_id).to_dict()
        res = self.api.casts(params=params)
        try:
            return Cast(**res["casts"][0])
        except Exception as e:
            raise e

    def find_all_cast_info(self) -> Casts:
        # TODO データ永続化処理で使用する
        casts = Casts()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = CastRequestParams(per_page=per_page, page=page).to_dict()
            res = self.api.casts(params=params)
            page = res["next_page"]
            for cast in res["casts"]:
                casts.append(Cast(**cast))
        return casts
