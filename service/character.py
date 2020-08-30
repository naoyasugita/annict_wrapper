import dataclasses

from model.character import Character
from model.character import Characters
from request import ApiRequests
from request_filter import CharacterRequestParams


@dataclasses.dataclass
class CharacterService:
    api: ApiRequests

    def find_character_info(self, character_id: int) -> Character:
        params = CharacterRequestParams(filter_ids=character_id).to_dict()
        res = self.api.characters(params=params)
        print(res)
        try:
            return Character(**res["characters"][0])
        except Exception as e:
            raise e

    def find_all_character_info(self) -> Characters:
        # TODO データ永続化処理で使用する
        characters = Characters()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = CharacterRequestParams(per_page=per_page, page=page).to_dict()
            res = self.api.characters(params=params)
            page = res["next_page"]
            for character in res["characters"]:
                characters.append(Character(**character))
        return characters
