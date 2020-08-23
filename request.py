import os

import requests


class ApiRequests:
    base_url = "https://api.annict.com/v1/"
    access_token = os.environ["ACCESS_TOKEN"]

    def works(self, params: dict = {}) -> dict:
        """Annictに登録されている作品情報を取得することができます。"""
        try:
            url = self.base_url + f"works?access_token={self.access_token}"
            res = requests.get(url, params=params)
            return res.json()
        except Exception as e:
            return e

    def staffs(self, params: dict = {}) -> dict:
        """Annictに登録されているスタッフ情報を取得することができます。"""
        try:
            url = self.base_url + f"staffs?access_token={self.access_token}"
            res = requests.get(url, params=params)
            return res.json()
        except Exception as e:
            return e

    def series(self, params: dict = {}) -> dict:
        """Annictに登録されているシリーズ情報を取得することができます。"""
        try:
            url = self.base_url + f"series?access_token={self.access_token}"
            res = requests.get(url, params=params)
            return res.json()
        except Exception as e:
            return e

    def people(self, params: dict = {}) -> dict:
        """Annictに登録されている人物情報を取得することができます。"""
        try:
            url = self.base_url + f"people?access_token={self.access_token}"
            res = requests.get(url, params=params)
            return res.json()
        except Exception as e:
            return e

    def organizations(self, params: dict = {}) -> dict:
        """Annictに登録されている団体情報を取得することができます。"""
        try:
            url = self.base_url + f"organizations?access_token={self.access_token}"
            res = requests.get(url, params=params)
            return res.json()
        except Exception as e:
            return e

    def episodes(self, params: dict = {}) -> dict:
        """Annictに登録されているエピソード情報を取得することができます。"""
        try:
            url = self.base_url + f"episodes?access_token={self.access_token}"
            res = requests.get(url, params=params)
            return res.json()
        except Exception as e:
            return e
