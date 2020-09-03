import pytest

from annict_wrapper.model.cast import Cast
from annict_wrapper.model.cast import Casts


class TestCastModel:
    def test_to_dict(self, fixture_cast):
        cast_dict = fixture_cast["cast_dict"]
        assert Cast(**cast_dict).to_dict() == cast_dict


class TestCastsModel:
    def test_casts_append_when_type_ok(self, fixture_cast, fixture_cast_2):
        casts = Casts()
        cast = fixture_cast["cast"]
        cast_2 = fixture_cast_2["cast"]
        casts.append(cast)
        casts.append(cast_2)
        assert len(casts._list) == 2

    def test_casts_append_when_type_error(self):
        casts = Casts()
        with pytest.raises(TypeError):
            casts.append("dammy")

    def test_casts_to_dict(self, fixture_cast):
        casts = Casts()
        cast = fixture_cast["cast"]
        cast_dict = fixture_cast["cast_dict"]
        casts.append(cast)
        assert casts.to_dict() == [cast_dict]
