from annict_wrapper.model.series import Series


class TestSeriesModel:
    def test_to_dict(self, fixture_series):
        actual = fixture_series["series_dict"]

        excepted = Series(**actual).to_dict()

        assert actual == excepted
