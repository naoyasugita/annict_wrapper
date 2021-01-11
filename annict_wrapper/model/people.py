import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict_wrapper.utils import from_bool
from annict_wrapper.utils import from_datetime
from annict_wrapper.utils import from_int
from annict_wrapper.utils import from_str
from annict_wrapper.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class PeopleId:
    """ 人物のID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class Name:
    """ 名前 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


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
class Nickname:
    """ ニックネーム """

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
class GenderText:
    """ 性別 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Url:
    """ 公式サイト等のURL """

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
class WikipediaUrl:
    """ WikipediaのURL """

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
class TwitterUsername:
    """ Twitterアカウントのusername """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class TwitterUsernameEn:
    """ Twitterアカウントのusername (英語圏向け) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


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
class People:
    people_id: PeopleId
    name: Name
    name_kana: NameKana
    name_en: NameEn
    nickname: Nickname
    nickname_en: NicknameEn
    gender_text: GenderText
    url: Url
    url_en: UrlEn
    wikipedia_url: WikipediaUrl
    wikipedia_url_en: WikipediaUrlEn
    twitter_username: TwitterUsername
    twitter_username_en: TwitterUsernameEn
    birthday: Birthday
    blood_type: BloodType
    height: Height
    favorite_people_count: FavoritePeopleCount
    casts_count: CastsCount
    staffs_count: StaffsCount
    prefecture: Optional[Prefecture] = None

    def __post_init__(self) -> None:
        if self.prefecture is not None:
            self.prefecture = Prefecture.from_dict(
                prefecture_dict={
                    "id": self.prefecture.id,
                    "name": self.prefecture.name,
                }
            )

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.people_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_kana": dataclasses.asdict(self.name_kana)["value"],
            "name_en": dataclasses.asdict(self.name_en)["value"],
            "nickname": dataclasses.asdict(self.nickname)["value"],
            "nickname_en": dataclasses.asdict(self.nickname_en)["value"],
            "gender_text": dataclasses.asdict(self.gender_text)["value"],
            "url": dataclasses.asdict(self.url)["value"],
            "url_en": dataclasses.asdict(self.url_en)["value"],
            "wikipedia_url": dataclasses.asdict(self.wikipedia_url)["value"],
            "wikipedia_url_en": dataclasses.asdict(self.wikipedia_url_en)["value"],
            "twitter_username": dataclasses.asdict(self.twitter_username)["value"],
            "twitter_username_en": dataclasses.asdict(self.twitter_username_en)[
                "value"
            ],
            "birthday": dataclasses.asdict(self.birthday)["value"],
            "blood_type": dataclasses.asdict(self.blood_type)["value"],
            "height": dataclasses.asdict(self.height)["value"],
            "favorite_people_count": dataclasses.asdict(self.favorite_people_count)[
                "value"
            ],
            "casts_count": dataclasses.asdict(self.casts_count)["value"],
            "staffs_count": dataclasses.asdict(self.staffs_count)["value"],
            "prefecture": to_class(Prefecture, self.prefecture)
            if self.prefecture is not None
            else None,
        }

    @staticmethod
    def from_dict(people_dict: dict) -> "People":
        assert isinstance(people_dict, dict)
        return People(
            people_id=PeopleId(people_dict["id"]),
            name=Name(people_dict["name"]),
            name_kana=NameKana(people_dict["name_kana"]),
            name_en=NameEn(people_dict["name_en"]),
            nickname=Nickname(people_dict["nickname"]),
            nickname_en=NicknameEn(people_dict["nickname_en"]),
            gender_text=GenderText(people_dict["gender_text"]),
            url=Url(people_dict["url"]),
            url_en=UrlEn(people_dict["url_en"]),
            wikipedia_url=WikipediaUrl(people_dict["wikipedia_url"]),
            wikipedia_url_en=WikipediaUrlEn(people_dict["wikipedia_url_en"]),
            twitter_username=TwitterUsername(people_dict["twitter_username"]),
            twitter_username_en=TwitterUsernameEn(people_dict["twitter_username_en"]),
            birthday=Birthday(people_dict["birthday"]),
            blood_type=BloodType(people_dict["blood_type"]),
            height=Height(people_dict["height"]),
            favorite_people_count=FavoritePeopleCount(
                people_dict["favorite_people_count"]
            ),
            casts_count=CastsCount(people_dict["casts_count"]),
            staffs_count=StaffsCount(people_dict["staffs_count"]),
            prefecture=Prefecture.from_dict(people_dict["prefecture"])
            if people_dict.get("prefecture") is not None
            else None,
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
