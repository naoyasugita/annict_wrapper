import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict.utils import from_bool
from annict.utils import from_datetime
from annict.utils import from_int
from annict.utils import from_str
from annict.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class PeopleId:
    """ 人物のID """

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
        assert isinstance(self.english, NicknameEn)

    def to_dict(self) -> dict:
        return {
            "nickname": self.value,
            "english": self.english.value,
        }

    @staticmethod
    def from_dict(nickname_dict: dict) -> "Nickname":
        assert isinstance(nickname_dict, dict)
        return Nickname(
            nickname_dict.get("nickname"),
            NicknameEn(nickname_dict.get("nickname_en")),
        )


@dataclasses.dataclass(frozen=True)
class Name:
    """ 名前 """

    value: str
    kana: NameKana
    english: NameEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.kana, NameKana)
        assert isinstance(self.english, NameEn)

    def to_dict(self) -> dict:
        return {
            "name": self.value,
            "kana": self.kana.value,
            "english": self.english.value,
        }

    def from_dict(name_dict: dict) -> "Name":
        assert isinstance(name_dict, dict)
        return Name(
            name_dict.get("name"),
            NameKana(name_dict.get("name_kana")),
            NameEn(name_dict.get("name_en")),
        )


@dataclasses.dataclass(frozen=True)
class GenderText:
    """ 性別 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class UrlEn:
    """ 公式サイト等のURL (英語圏向け) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class WikipediaUrlEn:
    """ WikipediaのURL(英語圏向け) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class WikipediaUrl:
    """ WikipediaのURL """

    value: str
    english: WikipediaUrlEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, WikipediaUrlEn)


@dataclasses.dataclass(frozen=True)
class Wikipedia:
    """ WikipediaのURL(英語圏向け) """

    url: WikipediaUrl

    def __post_init__(self) -> None:
        assert isinstance(self.url, WikipediaUrl)


@dataclasses.dataclass(frozen=True)
class Url:
    """ URL """

    value: str
    english: UrlEn
    wikipedia: Wikipedia

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, UrlEn)
        assert isinstance(self.wikipedia, Wikipedia)


@dataclasses.dataclass(frozen=True)
class TwitterUsernameEn:
    """ Twitterアカウントのusername (英語圏向け) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class TwitterUsername:
    """ Twitterアカウントのusername """

    value: str
    english: TwitterUsernameEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, TwitterUsernameEn)


@dataclasses.dataclass(frozen=True)
class Twitter:
    """ Twitter """

    username: TwitterUsername

    def __post_init__(self) -> None:
        assert isinstance(self.username, TwitterUsername)


@dataclasses.dataclass(frozen=True)
class Birthday:
    """ 誕生日 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class BloodType:
    """ 血液型 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Height:
    """ 身長 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class FavoritePeopleCount:
    """ お気に入りに入れている人の数 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class CastsCount:
    """ キャストとして登録されている作品の数 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class StaffsCount:
    """ スタッフとして登録されている作品の数 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass
class Prefecture:
    id: int
    name: str

    def __post_init__(self) -> None:
        from_int(self.id)
        from_str(self.name)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def from_dict(prefecture_dict: dict) -> "Prefecture":
        return Prefecture(
            id=prefecture_dict["id"],
            name=prefecture_dict["name"],
        )


@dataclasses.dataclass
class Profile:
    name: Name
    nickname: Nickname
    gender: GenderText
    birthday: Birthday
    blood_type: BloodType
    height: Height
    prefecture: Optional[Prefecture] = None

    def __post_init__(self) -> None:
        assert isinstance(self.name, Name)
        assert isinstance(self.nickname, Nickname)
        assert isinstance(self.gender, GenderText)
        assert isinstance(self.birthday, Birthday)
        assert isinstance(self.blood_type, BloodType)
        assert isinstance(self.height, Height)
        if self.prefecture is not None:
            assert isinstance(self.prefecture, Prefecture)

    def to_dict(self) -> dict:
        return {
            "name": to_class(Name, self.name),
            "nickname": to_class(Nickname, self.nickname),
            "gender": self.gender.value,
            "birthday": self.birthday.value,
            "blood_type": self.blood_type.value,
            "height": self.height.value,
            "prefecture": to_class(Prefecture, self.prefecture),
        }

    @staticmethod
    def from_dict(profile_dict: dict) -> "Profile":
        assert isinstance(profile_dict, dict)
        return Profile(
            Name.from_dict(profile_dict),
            Nickname.from_dict(profile_dict),
            GenderText(profile_dict.get("gender_text")),
            Birthday(profile_dict.get("birthday")),
            BloodType(profile_dict.get("blood_type")),
            Height(profile_dict.get("height")),
            Prefecture.from_dict(profile_dict),
        )


@dataclasses.dataclass
class People:
    people_id: PeopleId
    profile: Profile
    url: Url
    twitter: Twitter
    favorite_people_count: FavoritePeopleCount
    casts_count: CastsCount
    staffs_count: StaffsCount

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.people_id)["value"],
            "profile": to_class(Profile, self.profile),
            "url": dataclasses.asdict(self.url)["value"],
            "url_en": dataclasses.asdict(self.url.english)["value"],
            "wikipedia_url": dataclasses.asdict(self.url.wikipedia.url)["value"],
            "wikipedia_url_en": dataclasses.asdict(self.url.wikipedia.url.english)[
                "value"
            ],
            "twitter_username": dataclasses.asdict(self.twitter.username)["value"],
            "twitter_username_en": dataclasses.asdict(self.twitter.username.english)[
                "value"
            ],
            "favorite_people_count": dataclasses.asdict(self.favorite_people_count)[
                "value"
            ],
            "casts_count": dataclasses.asdict(self.casts_count)["value"],
            "staffs_count": dataclasses.asdict(self.staffs_count)["value"],
        }

    @staticmethod
    def from_dict(people_dict: dict) -> "People":
        assert isinstance(people_dict, dict)
        return People(
            PeopleId(people_dict["id"]),
            Profile.from_dict(people_dict),
            Url(
                people_dict["url"],
                UrlEn(people_dict["url_en"]),
                Wikipedia(
                    WikipediaUrl(
                        people_dict["wikipedia_url"],
                        WikipediaUrlEn(
                            people_dict["wikipedia_url_en"],
                        ),
                    ),
                ),
            ),
            Twitter(
                TwitterUsername(
                    people_dict["twitter_username"],
                    TwitterUsernameEn(
                        people_dict["twitter_username_en"],
                    ),
                ),
            ),
            FavoritePeopleCount(people_dict["favorite_people_count"]),
            CastsCount(people_dict["casts_count"]),
            StaffsCount(people_dict["staffs_count"]),
        )


@dataclasses.dataclass
class Peoples:
    _list: List[People] = dataclasses.field(default_factory=list)

    def append(self, people: People) -> None:
        if isinstance(people, People):
            self._list.append(people)
        else:
            raise TypeError("data is not people")

    def to_dict(self) -> list:
        return [l.to_dict() for l in self._list]
