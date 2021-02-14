import dataclasses

from annict.dataaccess.aws.dynamodb import DynamoDBClient
from annict.model.character import Character
from annict.model.character import Characters
from annict.request import AnnictApiClient
from annict.request_filter import CharacterRequestParams
from tqdm import tqdm


@dataclasses.dataclass
class CharacterService:
    api: AnnictApiClient
    dynamo: DynamoDBClient = DynamoDBClient("dev-annict-character")

    def find_character_by_id(self, character_id: int) -> dict:
        return self.dynamo.get_item("id", character_id)

    def fetch_character_info(self, character_id: int) -> Character:
        params = CharacterRequestParams(filter_ids=character_id).to_dict()
        res: dict = self.api.characters(params=params)
        translated_response: dict = CharacterTranslator().translate(
            res["characters"][0]
        )

        try:
            response = Character.from_dict(translated_response)
            self.dynamo.put_item(response.to_dict())
        except Exception as e:
            raise e

    def fetch_all_character_info(self) -> Characters:
        characters = Characters()
        per_page = 50  # limit_count
        page = 1  # init_page
        # while page is not None:
        while page <= 20:
            params = CharacterRequestParams(per_page=per_page, page=page).to_dict()
            res = self.api.characters(params=params)
            page = res["next_page"]
            for character in tqdm(res["characters"]):
                translated_response: dict = CharacterTranslator().translate(character)
                characters.append(Character.from_dict(translated_response))

            if page % 10 == 0:
                try:
                    self.dynamo.batch_writer(characters.to_dict())
                except Exception as e:
                    raise e
                characters = Characters()

        try:
            self.dynamo.batch_writer(characters.to_dict())
        except Exception as e:
            raise e
