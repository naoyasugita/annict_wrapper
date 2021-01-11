import dataclasses

from annict_wrapper.model.episode import Episode
from annict_wrapper.request import ApiRequests
from annict_wrapper.request_filter import EpisodeRequestParams


@dataclasses.dataclass
class EpisodeService:
    api: ApiRequests

    def find_episode_info(self, episode_id: int) -> Episode:
        params = EpisodeRequestParams(filter_ids=episode_id).to_dict()
        res = self.api.episodes(params=params)
        try:
            return Episode.from_dict(res["episodes"][0])
        except Exception as e:
            raise e
