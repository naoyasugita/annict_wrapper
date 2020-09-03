from annict_wrapper.model.series import Series


class TestSeriesModel:
    def test_to_dict(self, fixture_series):
        series_dict = fixture_series["series_dict"]
        assert Series(**series_dict).to_dict() == series_dict
