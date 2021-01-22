import dataclasses

from annict.model.series import Series
from annict.request import AnnictApiClient
from annict.request_filter import SeriesRequestParams


@dataclasses.dataclass
class SeriesService:
    api: AnnictApiClient

    def find_series_info(self, series_id: int) -> Series:
        params = SeriesRequestParams(filter_ids=series_id).to_dict()
        res = self.api.series(params=params)
        try:
            return Series.from_dict(res["series"][0])
        except Exception as e:
            raise e
