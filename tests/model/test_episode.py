from annict_wrapper.model.episode import Episode
from annict_wrapper.model.episode import NextEpisode
from annict_wrapper.model.episode import PrevEpisode


class TestEpisodeModel:
    def test_to_dict(self, fixture_episode):
        actual = fixture_episode["episode_dict"]

        excepted = Episode(**actual).to_dict()

        assert actual == excepted


class TestPredEpisodeModel:
    def test_to_dict(self, fixture_prev_episode):
        actual = fixture_prev_episode["prev_episode_dict"]

        excepted = PrevEpisode(**actual).to_dict()

        assert actual == excepted


class TestNextEpisodeModel:
    def test_to_dict(self, fixture_next_episode):
        actual = fixture_next_episode["next_episode_dict"]

        excepted = NextEpisode(**actual).to_dict()

        assert actual == excepted
