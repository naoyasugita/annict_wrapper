import dataclasses
from datetime import datetime
from typing import Any
from typing import List
from typing import Optional

import dateutil.parser
from sora.utils import from_bool
from sora.utils import from_datetime
from sora.utils import from_int
from sora.utils import from_str
from sora.utils import to_class


@dataclasses.dataclass(frozen=True)
class WorkId:
    """ APIで管理するアニメ作品に割り当てられているユニークなID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class TitleShortOne:
    """ アニメ作品名の略称1 """

    value: Optional[str]

    def __post_init__(self) -> None:
        if self.value is not None:
            from_str(self.value)
        else:
            from_none(self.value)


@dataclasses.dataclass(frozen=True)
class TitleShortTwo:
    """ アニメ作品名の略称2 """

    value: Optional[str]

    def __post_init__(self) -> None:
        if self.value is not None:
            from_str(self.value)
        else:
            from_none(self.value)


@dataclasses.dataclass(frozen=True)
class TitleShortThree:
    """ アニメ作品名の略称3 """

    value: Optional[str]

    def __post_init__(self) -> None:
        if self.value is not None:
            from_str(self.value)
        else:
            from_none(self.value)


@dataclasses.dataclass(frozen=True)
class TitleName:
    """ アニメ作品名 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Title:
    """ アニメ作品 """

    name: TitleName
    short_one: TitleShortOne
    short_two: TitleShortTwo
    short_three: TitleShortThree

    def __post_init__(self) -> None:
        assert isinstance(self.name, TitleName)
        assert isinstance(self.short_one, TitleShortOne)
        assert isinstance(self.short_two, TitleShortTwo)
        assert isinstance(self.short_three, TitleShortThree)

    def to_dict(self) -> dict:
        return {
            "name": self.name.value,
            "short_one": self.short_one.value,
            "short_two": self.short_two.value,
            "short_three": self.short_three.value,
        }

    @staticmethod
    def from_dict(title_dict: dict) -> "Title":
        assert isinstance(title_dict, dict)
        return Title(
            TitleName(title_dict.get("name")),
            TitleShortOne(title_dict.get("title_short1", None)),
            TitleShortTwo(title_dict.get("title_short2", None)),
            TitleShortThree(title_dict.get("title_short3", None)),
        )


@dataclasses.dataclass(frozen=True)
class PublicUrl:
    """ アニメ作品の公式URL """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class TwitterAccount:
    """ ツイッターアカウント """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class TwitterHashTag:
    """ ツイッターハッシュタグ """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Twitter:
    """ ツイッター """

    account: TwitterAccount
    hash_tag: TwitterHashTag

    def __post_init__(self) -> None:
        assert isinstance(self.account, TwitterAccount)
        assert isinstance(self.hash_tag, TwitterHashTag)

    def to_dict(self) -> dict:
        return {
            "account": self.account.value,
            "hash_tag": self.hash_tag.value,
        }

    @staticmethod
    def from_dict(twitter_dict: dict) -> "Twitter":
        assert isinstance(twitter_dict, dict)
        return Twitter(
            TwitterAccount(twitter_dict.get("account")),
            TwitterHashTag(twitter_dict.get("hash_tag")),
        )


@dataclasses.dataclass(frozen=True)
class CoursId:
    """ coursマスターのID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass()
class CreatedAt:
    """ データの作成日時 """

    # value: str
    value: datetime

    def __post_init__(self) -> None:
        self.value = from_datetime(self.value)


@dataclasses.dataclass()
class UpdatedAt:
    """ データの更新日時 """

    # value: str
    value: datetime

    def __post_init__(self) -> None:
        self.value = from_datetime(self.value)


@dataclasses.dataclass(frozen=True)
class Sex:
    """ 男性向け=0, 女性向け=1 """

    value: Optional[int]

    def __post_init__(self) -> None:
        if self.value is not None:
            from_int(self.value)
        else:
            from_none(self.value)


@dataclasses.dataclass(frozen=True)
class Sequel:
    """ 続編モノの場合は1以上の数値が入る """

    value: Optional[int]

    def __post_init__(self) -> None:
        if self.value is not None:
            from_int(self.value)
        else:
            from_none(self.value)


@dataclasses.dataclass(frozen=True)
class CityCode:
    """ 代表聖地地区の5桁の市区町村コード(RESAS APIなど地方自治体のオープンデータと連携する時に使用) """

    value: Optional[int]

    def __post_init__(self) -> None:
        if self.value is not None:
            from_int(self.value)
        else:
            from_none(self.value)


@dataclasses.dataclass(frozen=True)
class CityName:
    """ 代表聖地地区の市区町村名 """

    value: Optional[str]

    def __post_init__(self) -> None:
        if self.value is not None:
            from_str(self.value)
        else:
            from_none(self.value)


@dataclasses.dataclass(frozen=True)
class City:
    """ 代表聖地地区 """

    code: CityCode
    name: CityName

    def __post_init__(self) -> None:
        assert isinstance(self.code, CityCode)
        assert isinstance(self.name, CityName)

    def to_dict(self) -> dict:
        return {
            "code": self.code.value,
            "name": self.name.value,
        }

    @staticmethod
    def from_dict(city_dict: dict) -> "City":
        assert isinstance(city_dict, dict)
        return City(
            CityCode(city_dict.get("city_code", None)),
            CityName(city_dict.get("city_name", None)),
        )


@dataclasses.dataclass(frozen=True)
class ProductCompanies:
    """ 制作会社 """

    value: Optional[str]

    def __post_init__(self) -> None:
        if self.value is not None:
            from_str(self.value)
        else:
            from_none(self.value)


@dataclasses.dataclass(frozen=True)
class Work:
    work_id: WorkId
    title: Title
    public_url: PublicUrl
    twitter: Twitter
    cours_id: CoursId
    created_at: CreatedAt
    updated_at: UpdatedAt
    sex: Sex
    sequel: Sequel
    city: City
    product_companies: Optional[ProductCompanies] = None

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.work_id)["value"],
            "title": to_class(Title, self.title),
            "public_url": dataclasses.asdict(self.public_url)["value"],
            "twitter": to_class(Twitter, self.twitter),
            "cours_id": dataclasses.asdict(self.cours_id)["value"],
            "created_at": dataclasses.asdict(self.created_at)["value"].isoformat(),
            "updated_at": dataclasses.asdict(self.updated_at)["value"].isoformat(),
            "sex": dataclasses.asdict(self.sex)["value"],
            "sequel": dataclasses.asdict(self.sequel)["value"],
            "city": to_class(City, self.city),
            "product_companies": dataclasses.asdict(self.product_companies)["value"],
        }

    @staticmethod
    def from_dict(work_dict: dict) -> "Work":
        assert isinstance(work_dict, dict)
        return Work(
            WorkId(work_dict.get("id")),
            Title(
                TitleName(work_dict.get("title")),
                TitleShortOne(work_dict.get("title_short1", None)),
                TitleShortTwo(work_dict.get("title_short2", None)),
                TitleShortThree(work_dict.get("title_short3", None)),
            ),
            PublicUrl(work_dict.get("public_url")),
            Twitter(
                TwitterAccount(
                    work_dict.get("twitter_account"),
                ),
                TwitterHashTag(work_dict.get("twitter_hash_tag")),
            ),
            CoursId(work_dict.get("cours_id")),
            CreatedAt(work_dict.get("created_at")),
            UpdatedAt(work_dict.get("updated_at")),
            Sex(work_dict.get("sex", None)),
            Sequel(work_dict.get("sequel", None)),
            City(
                CityCode(work_dict.get("city_code", None)),
                CityName(work_dict.get("city_name", None)),
            ),
            ProductCompanies(work_dict.get("product_companies", None)),
        )


@dataclasses.dataclass
class Works:
    _list: List[Work] = dataclasses.field(default_factory=list)

    def append(self, work: Work) -> None:
        if isinstance(work, Work):
            self._list.append(work)
        else:
            raise TypeError("data is not work")

    def to_dict(self) -> list:
        return [work.to_dict() for work in self._list]
