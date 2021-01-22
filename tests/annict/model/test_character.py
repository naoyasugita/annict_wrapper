import pytest
from annict.model.character import Character
from annict.model.character import Characters


class TestCharacterModel:
    def test_to_dict(self, fixture_character):
        actual = fixture_character["character_dict"]

        character = fixture_character["character"]
        excepted = character.to_dict()

        assert actual == excepted


    def test_from_dict(self, fixture_character):
        actual = fixture_character["character"]

        character_dict = fixture_character["character_dict"]
        excepted = Character.from_dict(character_dict)

        assert actual == excepted

class TestCharactersModel:
    def test_characters_append_when_type_ok(self, fixture_character):
        characters = Characters()
        character = fixture_character["character"]
        character_2 = fixture_character["character"]
        characters.append(character)
        characters.append(character_2)
        excepted = len(characters._list)

        actual = 2

        assert actual == excepted

    def test_characters_append_when_type_error(self):
        characters = Characters()
        with pytest.raises(TypeError):
            characters.append("dammy")

    def test_characters_to_dict(self, fixture_character):
        characters = Characters()
        character = fixture_character["character"]
        characters.append(character)
        excepted = characters.to_dict()

        character_dict = fixture_character["character_dict"]
        actual = [character_dict]

        assert actual == excepted