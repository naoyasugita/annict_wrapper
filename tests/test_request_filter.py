from annict_wrapper.request_filter import WorkRequestParams


class TestWorkRequestParams:
    def test_to_dict_not_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
            "filter_season": "2016-spring",
            "filter_title": "shirobako",
            "page": 2,
            "per_page": 30,
            "sort_id": "desc",
            "sort_season": "desc",
            "sort_watchers_count": "desc",
        }
        work_request_params = WorkRequestParams(**params)
        assert work_request_params.to_dict() == params

    def test_to_dict_in_none(self):
        params = {
            "fields": "id",
            "filter_ids": 123,
        }
        work_request_params = WorkRequestParams(**params)
        assert work_request_params.to_dict() == params

    def test_to_dict_when_empty(self):
        params = {}
        work_request_params = WorkRequestParams(**params)
        assert work_request_params.to_dict() == params
