import dataclasses

from model.episode import Episode
from request import ApiRequests
from request_filter import EpisodeRequestParams


@dataclasses.dataclass
class EpisodeService:
    def find_episode_info(self, episode_id: int) -> Episode:
        api = ApiRequests()
        params = EpisodeRequestParams(filter_ids=episode_id).to_dict()
        res = api.episodes(params=params)
        try:
            return Episode(**res["episodes"][0])
        except Exception as e:
            raise e
