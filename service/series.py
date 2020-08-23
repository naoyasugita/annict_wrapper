import dataclasses

from model.series import Series
from request import ApiRequests
from request_filter import SeriesRequestParams


@dataclasses.dataclass
class SeriesService:
    def find_series_info(self, series_id: int) -> Series:
        api = ApiRequests()
        params = SeriesRequestParams(filter_ids=series_id).to_dict()
        res = api.series(params=params)
        try:
            return Series(**res["series"][0])
        except Exception as e:
            raise e
