import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict_wrapper.model.series import Series


@dataclasses.dataclass(frozen=True)
class CharacterId:
    """ キャラクターID """

    value: int


@dataclasses.dataclass(frozen=True)
class Name:
    """ 名前 """

    value: str


@dataclasses.dataclass(frozen=True)
class NameKana:
    """ 名前 (かな表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class NameEn:
    """ 名前 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class Nickname:
    """ ニックネーム """

    value: str


@dataclasses.dataclass(frozen=True)
class NicknameEn:
    """ ニックネーム (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class Birthday:
    """ 誕生日 """

    value: str


@dataclasses.dataclass(frozen=True)
class BirthdayEn:
    """ 誕生日 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class Age:
    """ 年齢 """

    value: str


@dataclasses.dataclass(frozen=True)
class AgeEn:
    """ 年齢 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class BloodType:
    """ 血液型 """

    value: str


@dataclasses.dataclass(frozen=True)
class BloodTypeEn:
    """ 血液型 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class Height:
    """ 身長 """

    value: str


@dataclasses.dataclass(frozen=True)
class HeightEn:
    """ 身長 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class Weight:
    """ 体重 """

    value: str


@dataclasses.dataclass(frozen=True)
class WeightEn:
    """ 体重 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class Nationality:
    """ 国籍 """

    value: str


@dataclasses.dataclass(frozen=True)
class NationalityEn:
    """ 国籍 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class Occupation:
    """ 肩書き """

    value: str


@dataclasses.dataclass(frozen=True)
class OccupationEn:
    """ 肩書き (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class Description:
    """ キャラ紹介 """

    value: str


@dataclasses.dataclass(frozen=True)
class DescriptionEn:
    """ キャラ紹介 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class DescriptionSource:
    """ キャラ紹介の引用元 """

    value: str


@dataclasses.dataclass(frozen=True)
class DescriptionSourceEn:
    """ キャラ紹介の引用元 (英語表記) """

    value: str


@dataclasses.dataclass(frozen=True)
class FavoriteCharactersCount:
    """ お気に入りに入れている人の数 """

    value: int


@dataclasses.dataclass(frozen=True)
class Kind:
    """ 作品の種類 """

    value: str


@dataclasses.dataclass
class Character:
    character_id: CharacterId
    name: Name
    name_kana: NameKana
    name_en: NameEn
    nickname: Nickname
    nickname_en: NicknameEn
    birthday: Birthday
    birthday_en: BirthdayEn
    age: Age
    age_en: AgeEn
    blood_type: BloodType
    blood_type_en: BloodTypeEn
    height: Height
    height_en: HeightEn
    weight: Weight
    weight_en: WeightEn
    nationality: Nationality
    nationality_en: NationalityEn
    occupation: Occupation
    occupation_en: OccupationEn
    description: Description
    description_en: DescriptionEn
    description_source: DescriptionSource
    description_source_en: DescriptionSourceEn
    favorite_characters_count: FavoriteCharactersCount
    kind: Optional[Kind] = None
    series: Optional[Series] = None

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.character_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_kana": dataclasses.asdict(self.name_kana)["value"],
            "name_en": dataclasses.asdict(self.name_en)["value"],
            "nickname": dataclasses.asdict(self.nickname)["value"],
            "nickname_en": dataclasses.asdict(self.nickname_en)["value"],
            "birthday": dataclasses.asdict(self.birthday)["value"],
            "birthday_en": dataclasses.asdict(self.birthday_en)["value"],
            "age": dataclasses.asdict(self.age)["value"],
            "age_en": dataclasses.asdict(self.age_en)["value"],
            "blood_type": dataclasses.asdict(self.blood_type)["value"],
            "blood_type_en": dataclasses.asdict(self.blood_type_en)["value"],
            "height": dataclasses.asdict(self.height)["value"],
            "height_en": dataclasses.asdict(self.height_en)["value"],
            "weight": dataclasses.asdict(self.weight)["value"],
            "weight_en": dataclasses.asdict(self.weight_en)["value"],
            "nationality": dataclasses.asdict(self.nationality)["value"],
            "nationality_en": dataclasses.asdict(self.nationality_en)["value"],
            "occupation": dataclasses.asdict(self.occupation)["value"],
            "occupation_en": dataclasses.asdict(self.occupation_en)["value"],
            "description": dataclasses.asdict(self.description)["value"],
            "description_en": dataclasses.asdict(self.description_en)["value"],
            "description_source": dataclasses.asdict(self.description_source)["value"],
            "description_source_en": dataclasses.asdict(self.description_source_en)[
                "value"
            ],
            "description_source_en": dataclasses.asdict(self.description_source_en)[
                "value"
            ],
            "favorite_characters_count": dataclasses.asdict(
                self.favorite_characters_count
            )["value"],
            "kind": dataclasses.asdict(self.kind)["value"]
            if self.kind is not None
            else None,
            "series": self.series.to_dict() if self.series is not None else None,
        }

    @staticmethod
    def from_dict(character_dict: dict) -> "Character":
        return Character(
            character_id=CharacterId(character_dict["id"]),
            name=Name(character_dict["name"]),
            name_kana=NameKana(character_dict["name_kana"]),
            name_en=NameEn(character_dict["name_en"]),
            nickname=Nickname(character_dict["nickname"]),
            nickname_en=NicknameEn(character_dict["nickname_en"]),
            birthday=Birthday(character_dict["birthday"]),
            birthday_en=BirthdayEn(character_dict["birthday_en"]),
            age=Age(character_dict["age"]),
            age_en=AgeEn(character_dict["age_en"]),
            blood_type=BloodType(character_dict["blood_type"]),
            blood_type_en=BloodTypeEn(character_dict["blood_type_en"]),
            height=Height(character_dict["height"]),
            height_en=HeightEn(character_dict["height_en"]),
            weight=Weight(character_dict["weight"]),
            weight_en=WeightEn(character_dict["weight_en"]),
            nationality=Nationality(character_dict["nationality"]),
            nationality_en=NationalityEn(character_dict["nationality_en"]),
            occupation=Occupation(character_dict["occupation"]),
            occupation_en=OccupationEn(character_dict["occupation_en"]),
            description=Description(character_dict["description"]),
            description_en=DescriptionEn(character_dict["description_en"]),
            description_source=DescriptionSource(character_dict["description_source"]),
            description_source_en=DescriptionSourceEn(
                character_dict["description_source_en"]
            ),
            favorite_characters_count=FavoriteCharactersCount(
                character_dict["favorite_characters_count"]
            ),
            kind=Kind(character_dict["kind"])
            if character_dict.get("kind") is not None
            else None,
            series=Series.from_dict(character_dict["series"])
            if character_dict.get("series") is not None
            else None,
        )


@dataclasses.dataclass
class Characters:
    _list: List[Character] = dataclasses.field(default_factory=list)

    def append(self, character: Character) -> None:
        if isinstance(character, Character):
            self._list.append(character)
        else:
            raise TypeError("data is not character")

    def to_dict(self) -> list:
        return [l.to_dict() for l in self._list]
