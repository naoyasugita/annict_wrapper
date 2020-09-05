import pytest

from annict_wrapper.model.started_at import StartedAt


class TestStartedAt:
    def test_create_instance(self):
        dt = StartedAt("2016/05/06 21:10")
        assert isinstance(dt, StartedAt) is True

    def test_create_instance_when_missed_format_1(self):
        with pytest.raises(ValueError):
            StartedAt("2016-05-06 21:10")

    def test_create_instance_when_missed_format_2(self):
        with pytest.raises(ValueError):
            StartedAt("2016/05/06 21:10:12")

    def test_create_instance_when_missed_format_3(self):
        with pytest.raises(ValueError):
            StartedAt("2016年05月06日 21時10分")

    def test_create_instance_when_value_is_none(self):
        with pytest.raises(TypeError):
            StartedAt(None)
