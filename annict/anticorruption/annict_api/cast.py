from annict.model.cast import Cast
from annict.model.character import Character
from annict.model.people import People
from annict.model.work import Work


class CastTransfer:
    @staticmethod
    def transfer(annict_api_response: dict) -> Cast:
        return CastTransfer._create_cast(annict_api_response)

    @staticmethod
    def _create_cast(annict_api_response: dict) -> Cast:
        return Cast.from_dict(annict_api_response)
