from typing import Any
from typing import Dict
from typing import List
from typing import Union

import requests


class SoraApiClient:
    # see: https://github.com/Project-ShangriLa/sora-playframework-scala
    base_url = "http://api.moemoe.tokyo/anime/v1"

    def cours(self) -> Dict[str, Dict[str, int]]:
        """ShangriLa API Serverが持っているアニメ情報のクールごとの情報のリストを返却します。"""
        # {
        # '1': {'id': 1, 'year': 2014, 'cours': 1},
        # '2': {'id': 2, 'year': 2014, 'cours': 2},
        # ...
        # }
        try:
            url = self.base_url + "/master/cours"
            res = requests.get(url)
            return res.json()
        except Exception as e:
            return e

    def year(self, year: int) -> List[Union[str, Dict[str, Any]]]:
        """yearで指定されたYYYY年のアニメ1クールから4クールまでの情報をすべて返却します"""
        # [
        # {'id': 1, 'title': 'hogehoge'},
        # {'id': 2, 'title': 'hugahuga'},
        # ]
        try:
            url = self.base_url + f"/master/{year}"
            res = requests.get(url)
            return res.json()
        except Exception as e:
            return e

    def year_cours(self, year: int, cours: int) -> List[Union[str, Dict[str, Any]]]:
        """yearで指定されたYYYY年アニメのcoursで指定されたクールの情報をすべて返します。"""
        # cours
        # 1: winter, 2:spring, 3: summer, 4: autumn
        try:
            url = self.base_url + f"/master/{year}/{cours}"
            res = requests.get(url)
            return res.json()
        except Exception as e:
            return e
