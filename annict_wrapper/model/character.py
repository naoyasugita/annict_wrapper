import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict_wrapper.model.series import Series
from annict_wrapper.utils import from_bool
from annict_wrapper.utils import from_datetime
from annict_wrapper.utils import from_int
from annict_wrapper.utils import from_str
from annict_wrapper.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class CharacterId:
    """ キャラクターID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class NameKana:
    """ 名前 (かな表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class NameEn:
    """ 名前 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class NicknameEn:
    """ ニックネーム (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Nickname:
    """ ニックネーム """

    value: str
    english: NicknameEn

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Name:
    """ 名前 """

    value: str
    kana: NameKana
    english: NameEn
    nickname: Nickname

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.kana, NameKana)
        assert isinstance(self.english, NameEn)
        assert isinstance(self.nickname, Nickname)


@dataclasses.dataclass(frozen=True)
class BirthdayEn:
    """ 誕生日 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Birthday:
    """ 誕生日 """

    value: str
    english: BirthdayEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, BirthdayEn)


@dataclasses.dataclass(frozen=True)
class AgeEn:
    """ 年齢 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Age:
    """ 年齢 """

    value: str
    english: AgeEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, AgeEn)


@dataclasses.dataclass(frozen=True)
class BloodTypeEn:
    """ 血液型 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class BloodType:
    """ 血液型 """

    value: str
    english: BloodTypeEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, BloodTypeEn)


@dataclasses.dataclass(frozen=True)
class HeightEn:
    """ 身長 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Height:
    """ 身長 """

    value: str
    english: HeightEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, HeightEn)


@dataclasses.dataclass(frozen=True)
class WeightEn:
    """ 体重 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Weight:
    """ 体重 """

    value: str
    english: WeightEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, WeightEn)


@dataclasses.dataclass(frozen=True)
class NationalityEn:
    """ 国籍 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Nationality:
    """ 国籍 """

    value: str
    english: NationalityEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, NationalityEn)


@dataclasses.dataclass(frozen=True)
class OccupationEn:
    """ 肩書き (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Occupation:
    """ 肩書き """

    value: str
    english: OccupationEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, OccupationEn)


@dataclasses.dataclass(frozen=True)
class DescriptionSourceEn:
    """ キャラ紹介の引用元 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class DescriptionSource:
    """ キャラ紹介の引用元 """

    value: str
    english: DescriptionSourceEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, DescriptionSourceEn)


@dataclasses.dataclass(frozen=True)
class DescriptionEn:
    """ キャラ紹介 (英語表記) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Description:
    """ キャラ紹介 """

    value: str
    english: DescriptionEn
    source: DescriptionSource

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, DescriptionEn)
        assert isinstance(self.source, DescriptionSource)


@dataclasses.dataclass(frozen=True)
class Profile:
    """ キャラクタープロフィール """

    name: Name
    birthday: Birthday
    age: Age
    blood_type: BloodType
    height: Height
    weight: Weight
    nationality: Nationality
    occupation: Occupation
    description: Description

    def __post_init__(self) -> None:
        assert isinstance(self.name, Name)
        assert isinstance(self.birthday, Birthday)
        assert isinstance(self.age, Age)
        assert isinstance(self.blood_type, BloodType)
        assert isinstance(self.height, Height)
        assert isinstance(self.weight, Weight)
        assert isinstance(self.nationality, Nationality)
        assert isinstance(self.occupation, Occupation)
        assert isinstance(self.description, Description)

    # def to_dict(self) -> dict:
    #     return {
    #     }


@dataclasses.dataclass(frozen=True)
class FavoriteCharactersCount:
    """ お気に入りに入れている人の数 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class Kind:
    """ 作品の種類 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass
class Character:
    character_id: CharacterId
    profile: Profile
    # name: Name
    # name_kana: NameKana
    # name_en: NameEn
    # nickname: Nickname
    # nickname_en: NicknameEn
    # birthday: Birthday
    # birthday_en: BirthdayEn
    # age: Age
    # age_en: AgeEn
    # blood_type: BloodType
    # blood_type_en: BloodTypeEn
    # height: Height
    # height_en: HeightEn
    # weight: Weight
    # weight_en: WeightEn
    # nationality: Nationality
    # nationality_en: NationalityEn
    # occupation: Occupation
    # occupation_en: OccupationEn
    # description: Description
    # description_en: DescriptionEn
    # description_source: DescriptionSource
    # description_source_en: DescriptionSourceEn
    favorite_characters_count: FavoriteCharactersCount
    kind: Optional[Kind] = None
    series: Optional[Series] = None

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.character_id)["value"],
            "name": dataclasses.asdict(self.profile.name)["value"],
            "name_kana": dataclasses.asdict(self.profile.name.kana)["value"],
            "name_en": dataclasses.asdict(self.profile.name.english)["value"],
            "nickname": dataclasses.asdict(self.profile.name.nickname)["value"],
            "nickname_en": dataclasses.asdict(self.profile.name.nickname.english)["value"],
            "birthday": dataclasses.asdict(self.profile.birthday)["value"],
            "birthday_en": dataclasses.asdict(self.profile.birthday.english)["value"],
            "age": dataclasses.asdict(self.profile.age)["value"],
            "age_en": dataclasses.asdict(self.profile.age.english)["value"],
            "blood_type": dataclasses.asdict(self.profile.blood_type)["value"],
            "blood_type_en": dataclasses.asdict(self.profile.blood_type.english)["value"],
            "height": dataclasses.asdict(self.profile.height)["value"],
            "height_en": dataclasses.asdict(self.profile.height.english)["value"],
            "weight": dataclasses.asdict(self.profile.weight)["value"],
            "weight_en": dataclasses.asdict(self.profile.weight.english)["value"],
            "nationality": dataclasses.asdict(self.profile.nationality)["value"],
            "nationality_en": dataclasses.asdict(self.profile.nationality.english)["value"],
            "occupation": dataclasses.asdict(self.profile.occupation)["value"],
            "occupation_en": dataclasses.asdict(self.profile.occupation.english)["value"],
            "description": dataclasses.asdict(self.profile.description)["value"],
            "description_en": dataclasses.asdict(self.profile.description.english)["value"],
            "description_source": dataclasses.asdict(self.profile.description.source)["value"],
            "description_source_en": dataclasses.asdict(
                self.profile.description.source.english
            )["value"],
            "favorite_characters_count": dataclasses.asdict(
                self.favorite_characters_count
            )["value"],
            "kind": dataclasses.asdict(self.kind)["value"]
            if self.kind is not None
            else None,
            "series": to_class(Series, self.series)
            if self.series is not None
            else None,
        }

    @staticmethod
    def from_dict(character_dict: dict) -> "Character":
        assert isinstance(character_dict, dict)
        return Character(
            CharacterId(character_dict["id"]),
            Profile(
                Name(
                    character_dict["name"],
                    NameKana(character_dict["name_kana"]),
                    NameEn(character_dict["name_en"]),
                    Nickname(
                        character_dict["nickname"],
                        NicknameEn(character_dict["nickname_en"]),
                    ),
                ),
                Birthday(
                    character_dict["birthday"],
                    BirthdayEn(character_dict["birthday_en"]),
                ),
                Age(
                    character_dict["age"],
                    AgeEn(character_dict["age_en"]),
                ),
                BloodType(
                    character_dict["blood_type"],
                    BloodTypeEn(character_dict["blood_type_en"]),
                ),
                Height(
                    character_dict["height"],
                    HeightEn(character_dict["height_en"]),
                ),
                Weight(
                    character_dict["weight"],
                    WeightEn(character_dict["weight_en"]),
                ),
                Nationality(
                    character_dict["nationality"],
                    NationalityEn(character_dict["nationality_en"]),
                ),
                Occupation(
                    character_dict["occupation"],
                    OccupationEn(character_dict["occupation_en"]),
                ),
                Description(
                    character_dict["description"],
                    DescriptionEn(
                        character_dict["description_en"],
                    ),
                    DescriptionSource(
                            character_dict["description_source"],
                            DescriptionSourceEn(
                                character_dict["description_source_en"]
                            ),
                        ),
                ),
            ),
            FavoriteCharactersCount(character_dict["favorite_characters_count"]),
            Kind(character_dict["kind"])
            if character_dict.get("kind") is not None
            else None,
            Series.from_dict(character_dict["series"])
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
