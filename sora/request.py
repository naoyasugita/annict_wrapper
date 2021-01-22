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


api = SoraApiClient()
# print(api.cours())
print(api.year_cours(2021, 1))


# def staffs(self, params: dict = {}) -> dict:
#     """Annictに登録されているスタッフ情報を取得することができます。"""
#     try:
#         url = self.base_url + f"staffs?access_token={self.access_token}"
#         res = requests.get(url, params=params)
#         return res.json()
#     except Exception as e:
#         return e

# def series(self, params: dict = {}) -> dict:
#     """Annictに登録されているシリーズ情報を取得することができます。"""
#     try:
#         url = self.base_url + f"series?access_token={self.access_token}"
#         res = requests.get(url, params=params)
#         return res.json()
#     except Exception as e:
#         return e

# def people(self, params: dict = {}) -> dict:
#     """Annictに登録されている人物情報を取得することができます。"""
#     try:
#         url = self.base_url + f"people?access_token={self.access_token}"
#         res = requests.get(url, params=params)
#         return res.json()
#     except Exception as e:
#         return e

# def organizations(self, params: dict = {}) -> dict:
#     """Annictに登録されている団体情報を取得することができます。"""
#     try:
#         url = self.base_url + f"organizations?access_token={self.access_token}"
#         res = requests.get(url, params=params)
#         return res.json()
#     except Exception as e:
#         return e

# def episodes(self, params: dict = {}) -> dict:
#     """Annictに登録されているエピソード情報を取得することができます。"""
#     try:
#         url = self.base_url + f"episodes?access_token={self.access_token}"
#         res = requests.get(url, params=params)
#         return res.json()
#     except Exception as e:
#         return e

# def programs(self, params: dict = {}) -> dict:
#     """放送予定を取得することができます"""
#     # NOTE 今はレスポンスが無いみたい。。。
#     try:
#         url = self.base_url + f"me/programs?access_token={self.access_token}"
#         res = requests.get(url, params=params)
#         return res.json()
#     except Exception as e:
#         return e

# def casts(self, params: dict = {}) -> dict:
#     """Annictに登録されているキャスト情報を取得することができます。"""
#     try:
#         url = self.base_url + f"casts?access_token={self.access_token}"
#         res = requests.get(url, params=params)
#         return res.json()
#     except Exception as e:
#         return e

# def characters(self, params: dict = {}) -> dict:
#     """Annictに登録されているキャラクター情報を取得することができます。"""
#     try:
#         url = self.base_url + f"characters?access_token={self.access_token}"
#         res = requests.get(url, params=params)
#         return res.json()
#     except Exception as e:
#         return e
