import pytest
from annict_wrapper.model.cast import Cast
from annict_wrapper.model.cast import Casts


class TestCastModel:
    def test_to_dict(self, fixture_cast):
        actual = fixture_cast["cast_dict"]

        cast = fixture_cast["cast"]
        excepted = cast.to_dict()

        assert actual == excepted

    def test_from_dict(self, fixture_cast):
        actual = fixture_cast["cast"]

        cast_dict = fixture_cast["cast_dict"]
        excepted = Cast.from_dict(cast_dict)

        assert actual == excepted

class TestCastsModel:
    def test_casts_append_when_type_ok(self, fixture_cast):
        casts = Casts()
        cast = fixture_cast["cast"]
        cast_2 = fixture_cast["cast"]
        casts.append(cast)
        casts.append(cast_2)
        excepted = len(casts._list)

        actual = 2

        assert actual == excepted

    def test_casts_append_when_type_error(self):
        casts = Casts()
        with pytest.raises(TypeError):
            casts.append("dammy")

    def test_casts_to_dict(self, fixture_cast):
        casts = Casts()
        cast = fixture_cast["cast"]
        casts.append(cast)
        excepted = casts.to_dict()

        cast_dict = fixture_cast["cast_dict"]
        actual = [cast_dict]

        assert actual == excepted
