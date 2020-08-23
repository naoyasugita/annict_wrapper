import dataclasses

from model.series import Series
from request import ApiRequests
from request_filter import SeriesRequestParams


@dataclasses.dataclass
class SeriesService:
    api: ApiRequests

    def find_series_info(self, series_id: int) -> Series:
        params = SeriesRequestParams(filter_ids=series_id).to_dict()
        res = self.api.series(params=params)
        try:
            return Series(**res["series"][0])
        except Exception as e:
            raise e
