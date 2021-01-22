import dataclasses

from annict.model.episode import Episode
from annict.request import AnnictApiClient
from annict.request_filter import EpisodeRequestParams


@dataclasses.dataclass
class EpisodeService:
    api: AnnictApiClient

    def find_episode_info(self, episode_id: int) -> Episode:
        params = EpisodeRequestParams(filter_ids=episode_id).to_dict()
        res = self.api.episodes(params=params)
        try:
            return Episode.from_dict(res["episodes"][0])
        except Exception as e:
            raise e
