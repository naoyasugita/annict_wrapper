import pytest

from annict_wrapper.model.character import Character
from annict_wrapper.model.character import Characters


class TestCharacterModel:
    def test_to_dict(self, fixture_character):
        character_dict = fixture_character["character_dict"]
        assert Character(**character_dict).to_dict() == character_dict


class TestCharactersModel:
    def test_characters_append_when_type_ok(self, fixture_character):
        characters = Characters()
        character = fixture_character["character"]
        character_2 = fixture_character["character"]
        characters.append(character)
        characters.append(character_2)
        assert len(characters._list) == 2

    def test_characters_append_when_type_error(self):
        characters = Characters()
        with pytest.raises(TypeError):
            characters.append("dammy")

    def test_characters_to_dict(self, fixture_character):
        characters = Characters()
        character = fixture_character["character"]
        character_dict = fixture_character["character_dict"]
        characters.append(character)
        assert characters.to_dict() == [character_dict]
