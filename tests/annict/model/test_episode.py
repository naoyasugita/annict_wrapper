from annict.model.episode import Episode
from annict.model.episode import NextEpisode
from annict.model.episode import PrevEpisode


class TestPrevEpisodeModel:
    def test_to_dict(self, fixture_prev_episode):
        actual = fixture_prev_episode["prev_episode_dict"]

        episode = fixture_prev_episode["prev_episode"]
        expected = episode.to_dict()

        assert actual == expected

    def test_from_dict(self, fixture_prev_episode):
        actual = fixture_prev_episode["prev_episode"]

        prev_episode_dict = fixture_prev_episode["prev_episode_dict"]
        expected = PrevEpisode.from_dict(prev_episode_dict)

        assert actual == expected


class TestNextEpisodeModel:
    def test_to_dict(self, fixture_next_episode):
        actual = fixture_next_episode["next_episode_dict"]

        episode = fixture_next_episode["next_episode"]
        expected = episode.to_dict()

        assert actual == expected

    def test_from_dict(self, fixture_next_episode):
        actual = fixture_next_episode["next_episode"]

        next_episode_dict = fixture_next_episode["next_episode_dict"]
        expected = NextEpisode.from_dict(next_episode_dict)

        assert actual == expected


class TestEpisodeModel:
    def test_to_dict(self, fixture_episode):
        actual = fixture_episode["to_dict"]

        episode = fixture_episode["episode"]
        expected = episode.to_dict()

        assert actual == expected

    def test_from_dict(self, fixture_episode):
        actual = fixture_episode["episode"]

        episode_dict = fixture_episode["episode_dict"]
        expected = Episode.from_dict(episode_dict)

        assert actual == expected
