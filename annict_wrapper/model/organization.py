import dataclasses
from typing import List

from annict_wrapper.utils import from_bool
from annict_wrapper.utils import from_datetime
from annict_wrapper.utils import from_int
from annict_wrapper.utils import from_str
from annict_wrapper.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


@dataclasses.dataclass(frozen=True)
class OrganizationId:
    """ 団体のID """

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
    name_kana: NameKana
    name_en: NameEn
    url: Url
    url_en: UrlEn
    wikipedia_url: WikipediaUrl
    wikipedia_url_en: WikipediaUrlEn
    twitter_username: TwitterUsername
    twitter_username_en: TwitterUsernameEn
    favorite_organizations_count: FavoriteOrganizationsCount
    staffs_count: StaffsCount

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.organization_id)["value"],
            "name": dataclasses.asdict(self.name)["value"],
            "name_kana": dataclasses.asdict(self.name_kana)["value"],
            "name_en": dataclasses.asdict(self.name_en)["value"],
            "url": dataclasses.asdict(self.url)["value"],
            "url_en": dataclasses.asdict(self.url_en)["value"],
            "wikipedia_url": dataclasses.asdict(self.wikipedia_url)["value"],
            "wikipedia_url_en": dataclasses.asdict(self.wikipedia_url_en)["value"],
            "twitter_username": dataclasses.asdict(self.twitter_username)["value"],
            "twitter_username_en": dataclasses.asdict(self.twitter_username_en)[
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
            Name(organization_dict["name"]),
            NameKana(organization_dict["name_kana"]),
            NameEn(organization_dict["name_en"]),
            Url(organization_dict["url"]),
            UrlEn(organization_dict["url_en"]),
            WikipediaUrl(organization_dict["wikipedia_url"]),
            WikipediaUrlEn(organization_dict["wikipedia_url_en"]),
            TwitterUsername(organization_dict["twitter_username"]),
            TwitterUsernameEn(organization_dict["twitter_username_en"]),
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
