import dataclasses

from annict_wrapper.model.series import Series
from annict_wrapper.request import ApiRequests
from annict_wrapper.request_filter import SeriesRequestParams


@dataclasses.dataclass
class SeriesService:
    api: ApiRequests

    def find_series_info(self, series_id: int) -> Series:
        params = SeriesRequestParams(filter_ids=series_id).to_dict()
        res = self.api.series(params=params)
        try:
            return Series.from_dict(res["series"][0])
        except Exception as e:
            raise e
