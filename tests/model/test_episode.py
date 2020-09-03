from annict_wrapper.model.episode import Episode
from annict_wrapper.model.episode import NextEpisode
from annict_wrapper.model.episode import PrevEpisode


class TestEpisodeModel:
    def test_to_dict(self, fixture_episode):
        episode_dict = fixture_episode["episode_dict"]
        assert Episode(**episode_dict).to_dict() == episode_dict


class TestPredEpisodeModel:
    def test_to_dict(self, fixture_prev_episode):
        prev_episode_dict = fixture_prev_episode["prev_episode_dict"]
        assert PrevEpisode(**prev_episode_dict).to_dict() == prev_episode_dict


class TestNextEpisodeModel:
    def test_to_dict(self, fixture_next_episode):
        next_episode_dict = fixture_next_episode["next_episode_dict"]
        assert NextEpisode(**next_episode_dict).to_dict() == next_episode_dict
