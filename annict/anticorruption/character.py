class CharacterTranslator:
    def translate(self, character_response: dict) -> dict:
        new_response = {}

        series = {}

        new_response["id"] = character_response.get("id")

        new_response["profile"] = self._create_profile(character_response)
        new_response["series"] = self._create_series(character_response)

        return new_response

    def _create_profile(self, data: dict) -> dict:
        profile_dict = {}

        profile_dict["name"] = data.get("name")
        profile_dict["birthday"] = data.get("birthday")
        profile_dict["age"] = data.get("age")
        profile_dict["blood_type"] = data.get("blood_type")
        profile_dict["height"] = data.get("height")
        profile_dict["weight"] = data.get("weight")
        profile_dict["nationality"] = data.get("nationality")
        profile_dict["occupation"] = data.get("occupation")
        profile_dict["description"] = data.get("description")
        profile_dict["description_source"] = data.get("description_source")

        return profile_dict

    def _create_series(self, data: dict) -> dict:
        series_dict = {}

        series_dict["id"] = data["series"].get("id")
        series_dict["name"] = data["series"].get("name")
        series_dict["name_ro"] = data["series"].get("name_ro")
        series_dict["name_en"] = data["series"].get("name_en")

        return series_dict
