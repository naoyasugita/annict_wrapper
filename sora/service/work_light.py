import dataclasses
from typing import List
from typing import Union

from sora.model.work_light import MultiWorkLight
from sora.model.work_light import WorkLight
from sora.request import SoraApiClient


@dataclasses.dataclass
class MultiWorkLightService:
    api: SoraApiClient

    def fetch_work_light_by_year(self, year: int) -> List[Union[WorkLight]]:
        try:
            multi_work_light = MultiWorkLight()
            res = self.api.year(year)
            for work_light in res:
                multi_work_light.append(WorkLight.from_dict(work_light))
            return multi_work_light
        except Exception as e:
            raise e
