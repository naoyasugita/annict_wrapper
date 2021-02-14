import pytest
from annict.anticorruption.character import CharacterTranslator
from annict.model.character import Character
from annict.model.character import Characters


class TestCharacterModel:
    def test_to_dict(self, fixture_character):
        actual = fixture_character["to_dict"]

        character = fixture_character["character"]
        expected = character.to_dict()

        assert actual == expected

    def test_from_dict(self, fixture_character):
        actual = fixture_character["character"]

        translated_dict = CharacterTranslator().translate(fixture_character["character_dict"])
        expected = Character.from_dict(translated_dict)

        assert actual == expected


class TestCharactersModel:
    def test_characters_append_when_type_ok(self, fixture_character):
        characters = Characters()
        character = fixture_character["character"]
        character_2 = fixture_character["character"]
        characters.append(character)
        characters.append(character_2)
        expected = len(characters._list)

        actual = 2

        assert actual == expected

    def test_characters_append_when_type_error(self):
        characters = Characters()
        with pytest.raises(TypeError):
            characters.append("dammy")

    def test_characters_to_dict(self, fixture_character):
        characters = Characters()
        character = fixture_character["character"]
        characters.append(character)
        expected = characters.to_dict()

        character_dict = fixture_character["to_dict"]
        actual = [character_dict]

        assert actual == expected
