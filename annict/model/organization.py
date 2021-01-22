import dataclasses
from typing import List

from annict.utils import from_bool
from annict.utils import from_datetime
from annict.utils import from_int
from annict.utils import from_str
from annict.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class OrganizationId:
    """ 団体のID """

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
class Name:
    """ 名前 """

    value: str
    kana: NameKana
    english: NameEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.kana, NameKana)
        assert isinstance(self.english, NameEn)


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
    """ Wikipedia """

    url: WikipediaUrl

    def __post_init__(self) -> None:
        assert isinstance(self.url, WikipediaUrl)


@dataclasses.dataclass(frozen=True)
class Url:
    """ 公式サイト等のURL """

    value: str
    english: UrlEn

    def __post_init__(self) -> None:
        from_str(self.value)
        assert isinstance(self.english, UrlEn)


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
class FavoriteOrganizationsCount:
    """ お気に入りに入れている人の数 """

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
class Organization:
    organization_id: OrganizationId
    name: Name
    url: Url
    wikipedia: Wikipedia
    twitter: Twitter
    favorite_organizations_count: FavoriteOrganizationsCount
    staffs_count: StaffsCount

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.organization_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_kana": dataclasses.asdict(self.name.kana)["value"],
            "name_en": dataclasses.asdict(self.name.english)["value"],
            "url": dataclasses.asdict(self.url)["value"],
            "url_en": dataclasses.asdict(self.url.english)["value"],
            "wikipedia_url": dataclasses.asdict(self.wikipedia.url)["value"],
            "wikipedia_url_en": dataclasses.asdict(self.wikipedia.url.english)["value"],
            "twitter_username": dataclasses.asdict(self.twitter.username)["value"],
            "twitter_username_en": dataclasses.asdict(self.twitter.username.english)[
                "value"
            ],
            "favorite_organizations_count": dataclasses.asdict(
                self.favorite_organizations_count
            )["value"],
            "staffs_count": dataclasses.asdict(self.staffs_count)["value"],
        }

    @staticmethod
    def from_dict(organization_dict: dict) -> "Organization":
        assert isinstance(organization_dict, dict)
        return Organization(
            OrganizationId(organization_dict["id"]),
            Name(
                organization_dict["name"],
                NameKana(organization_dict["name_kana"]),
                NameEn(organization_dict["name_en"]),
            ),
            Url(
                organization_dict["url"],
                UrlEn(organization_dict["url_en"]),
            ),
            Wikipedia(
                WikipediaUrl(
                    organization_dict["wikipedia_url"],
                    WikipediaUrlEn(organization_dict["wikipedia_url_en"]),
                ),
            ),
            Twitter(
                TwitterUsername(
                    organization_dict["twitter_username"],
                    TwitterUsernameEn(organization_dict["twitter_username_en"]),
                ),
            ),
            FavoriteOrganizationsCount(
                organization_dict["favorite_organizations_count"]
            ),
            StaffsCount(organization_dict["staffs_count"]),
        )


@dataclasses.dataclass
class Organizations:
    _list: List[Organization] = dataclasses.field(default_factory=list)

    def append(self, organization: Organization) -> None:
        if isinstance(organization, Organization):
            self._list.append(organization)
        else:
            raise TypeError("data is not organization")

    def to_dict(self) -> list:
        return [l.to_dict() for l in self._list]
