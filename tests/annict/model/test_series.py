from annict.model.series import Series


class TestSeriesModel:
    def test_to_dict(self, fixture_series):
        actual = fixture_series["series_dict"]

        series = fixture_series["series"]
        excepted = series.to_dict()

        assert actual == excepted

    def test_from_dict(self, fixture_series):
        actual = fixture_series["series"]

        series_dict = fixture_series["series_dict"]
        excepted = Series.from_dict(series_dict)

        assert actual == excepted
