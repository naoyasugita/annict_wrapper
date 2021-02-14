import pytest
from annict.anticorruption.character import CharacterTranslator
from annict.model.character import Character
from annict.model.character import Characters


class TestCharacterTranslator:
    def test_translate(self, fixture_character):
        actual = fixture_character["to_dict"]

        character_dict = fixture_character["character_dict"]
        expected = CharacterTranslator().translate(character_dict)

        assert actual == expected


    def test_create_profile(self, fixture_character):
        actual = fixture_character["to_dict"]

        character_dict = fixture_character["character_dict"]
        expected = CharacterTranslator()._create_profile(character_dict)

        assert actual["profile"] == expected


    def test_create_series(self, fixture_character):
        actual = fixture_character["to_dict"]

        character_dict = fixture_character["character_dict"]
        expected = CharacterTranslator()._create_series(character_dict)

        assert actual["series"] == expected
