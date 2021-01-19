import dataclasses
from datetime import datetime
from enum import Enum
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from typing import cast

import dateutil.parser
# 循環インポートでエラーになる！？
# from annict_wrapper.utils import from_bool
# from annict_wrapper.utils import from_datetime
# from annict_wrapper.utils import from_int
# from annict_wrapper.utils import from_str
# from annict_wrapper.utils import to_class
from dacite.config import Config
from dacite.core import from_dict


class Cool(Enum):
    spring = auto()
    summer = auto()
    autumn = auto()
    winter = auto()
    all = auto()


@dataclasses.dataclass(frozen=True)
class WorkId:
    """ 作品のID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class TitleKana:
    """ 作品タイトルの読み仮名 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Title:
    """ 作品のタイトル """

    value: str
    kana: TitleKana

    def __post_init__(self) -> None:
        from_str(self.value)

    def to_kana(self) -> str:
        return self.kana.value

    def to_dict(self) -> dict:
        return {"value": self.value, "kana": self.kana.value}


class Media(Enum):
    """ リリース媒体 (表記用) """

    tv = "TV"
    ova = "OVA"
    movie = "映画"
    web = "web"
    other = "その他"


@dataclasses.dataclass(frozen=True)
class SeasonNameText:
    """ リリース時期 (表記用) """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class SeasonName:
    """ リリース時期 """

    value: str
    text: Optional[SeasonNameText]

    def __post_init__(self) -> None:
        from_str(self.value)

    def get_cool(self) -> Tuple[int, Cool]:
        try:
            release_year = int(self.value.split("-")[0])
            season = Cool[self.value.split("-")[1]]
            return (release_year, season)
        except Exception as e:
            raise e

    def to_text(self) -> str:
        return self.text.value

    def to_dict(self) -> dict:
        return {
            "value": self.value,
            "text": self.text.value if self.text is not None else None,
        }

    @staticmethod
    def from_dict(season_dict: dict) -> "SeasonName":
        return SeasonName(
            season_dict["season_name"],
            season_dict["season_name_text"]
            if season_dict["season_name_text"] is not None
            else None,
        )


@dataclasses.dataclass(frozen=True)
class releasedOnAbout:
    """ 未確定な大体のリリース日 """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class ReleasedOn:
    """ リリース日 """

    value: str
    about: releasedOnAbout

    def __post_init__(self) -> None:
        from_str(self.value)

    def to_about(self) -> str:
        return self.about.value

    def to_dict(self) -> dict:
        return {
            "value": self.value,
            "about": self.about.value,
        }


@dataclasses.dataclass(frozen=True)
class OfficialSiteUrl:
    """ 公式サイトのURL """

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
class Url:
    official_site: OfficialSiteUrl
    wikipedia: WikipediaUrl

    def __post_init__(self) -> None:
        assert isinstance(self.official_site, OfficialSiteUrl)
        assert isinstance(self.wikipedia, WikipediaUrl)

    def to_dict(self) -> dict:
        return {
            "official_site": self.official_site.value,
            "wikipedia": self.wikipedia.value,
        }


@dataclasses.dataclass(frozen=True)
class TwitterUsername:
    """ 公式Twitterアカウントのusername """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class TwitterHashtag:
    """ Twitterの作品に関するハッシュタグ """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class SyobocalTitleId:
    """ しょぼいカレンダーのタイトルID """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class MyAnimeListAnimeId:
    """ MyAnimeListの作品ID """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class MiniAvatarUrl:
    """
    Twitterアカウントのアバター画像。(mini)
    """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class NormalAvatarUrl:
    """
    Twitterアカウントのアバター画像。(normal)
    """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class BiggerAvatarUrl:
    """
    Twitterアカウントのアバター画像。(bigger)
    """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class OriginalAvatarUrl:
    """
    Twitterアカウントのアバター画像。(original)
    """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class ImageUrl:
    """
    イメージ画像
    """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class TwitterImage:
    """
    Twitterアカウントのアバター画像。
    mini, normal, bigger, original の4種類のサイズがあります
    """

    mini_avatar_url: MiniAvatarUrl
    normal_avatar_url: NormalAvatarUrl
    bigger_avatar_url: BiggerAvatarUrl
    original_avatar_url: OriginalAvatarUrl
    image_url: ImageUrl

    def __post_init__(self) -> None:
        assert isinstance(self.mini_avatar_url, MiniAvatarUrl)
        assert isinstance(self.normal_avatar_url, NormalAvatarUrl)
        assert isinstance(self.bigger_avatar_url, BiggerAvatarUrl)
        assert isinstance(self.original_avatar_url, OriginalAvatarUrl)
        assert isinstance(self.image_url, ImageUrl)

    def to_dict(self) -> dict:
        return {
            "mini_avatar_url": self.mini_avatar_url.value,
            "normal_avatar_url": self.normal_avatar_url.value,
            "bigger_avatar_url": self.bigger_avatar_url.value,
            "original_avatar_url": self.original_avatar_url.value,
            "image_url": self.image_url.value,
        }

    @staticmethod
    def from_dict(twitter_dict: dict) -> "TwitterImage":
        assert isinstance(twitter_dict, dict)
        return TwitterImage(
            MiniAvatarUrl(twitter_dict["mini_avatar_url"]),
            NormalAvatarUrl(twitter_dict["normal_avatar_url"]),
            BiggerAvatarUrl(twitter_dict["bigger_avatar_url"]),
            OriginalAvatarUrl(twitter_dict["original_avatar_url"]),
            ImageUrl(twitter_dict["image_url"]),
        )


@dataclasses.dataclass(frozen=True)
class OgImageUrl:
    """
    official_site_url のページで取得できる og:image のURL
    """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Facebook:
    """
    official_site_url のページで取得できる og:image のURL
    """

    og_image_url: OgImageUrl

    def __post_init__(self) -> None:
        assert isinstance(self.og_image_url, OgImageUrl)

    def to_dict(self) -> dict:
        return {"og_image_url": self.og_image_url.value}

    @staticmethod
    def from_dict(facebook_dict: dict) -> "Facebook":
        assert isinstance(facebook_dict, dict)
        return Facebook(
            OgImageUrl(facebook_dict["og_image_url"]),
        )


@dataclasses.dataclass(frozen=True)
class RecommendedUrl:
    """
    facebook.og_image_url, twitter.bigger_avatar_url, twitter.image_url のうち、
    解像度が一番大きい画像のURL。扱いやすい画像のURLが高確率で格納されるプロパティになります
    """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class Images:
    """ 画像 """

    twitter: TwitterImage
    facebook: Facebook
    recommended_url: RecommendedUrl

    def __post_init__(self) -> None:
        assert isinstance(self.twitter, TwitterImage)
        assert isinstance(self.facebook, Facebook)
        assert isinstance(self.recommended_url, RecommendedUrl)

    def to_dict(self) -> dict:
        return {
            "twitter": to_class(TwitterImage, self.twitter),
            "facebook": to_class(Facebook, self.facebook),
            "recommended_url": self.recommended_url.value,
        }

    @staticmethod
    def from_dict(images_dict: dict) -> "Images":
        assert isinstance(images_dict, dict)
        return Images(
            TwitterImage.from_dict(images_dict["twitter"]),
            Facebook.from_dict(images_dict["facebook"]),
            RecommendedUrl(images_dict["recommended_url"]),
        )


@dataclasses.dataclass(frozen=True)
class Twitter:
    """ 公式Twitterアカウントのusername """

    username: TwitterUsername
    hashtag: TwitterHashtag
    image: TwitterImage

    def __post_init__(self) -> None:
        assert isinstance(self.username, TwitterUsername)
        assert isinstance(self.hashtag, TwitterHashtag)
        assert isinstance(self.image, TwitterImage)

    def to_dict(self) -> dict:
        return {
            "username": self.username.value,
            "hashtag": self.hashtag.value,
            "image": self.image.to_dict(),
        }

    @staticmethod
    def from_dict(twitter_dict: dict) -> "Twitter":
        return Twitter(
            TwitterUsername(twitter_dict["username"]),
            TwitterHashtag(twitter_dict["hashtag"]),
            TwitterImage.from_dict(twitter_dict["image"]),
        )


@dataclasses.dataclass(frozen=True)
class MyAnimeListAnimeId:
    """ MyAnimeListの作品ID """

    value: str

    def __post_init__(self) -> None:
        from_str(self.value)


@dataclasses.dataclass(frozen=True)
class EpisodesCount:
    """ エピソード数 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class WatchersCount:
    """ 見てる / 見たい / 見た人の数 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class ReleaseYear:
    """ 放送された年 """

    value: int

    def __post_init__(self) -> None:
        from_int(self.value)


@dataclasses.dataclass(frozen=True)
class ReleaseCool:
    """ 放送されたクール """

    value: str

    def __post_init__(self) -> None:
        assert self.value in Cool.__members__


@dataclasses.dataclass(frozen=True)
class Release:
    """ リリース時期 """

    year: ReleaseYear
    cool: ReleaseCool

    def __post_init__(self) -> None:
        assert isinstance(self.year, ReleaseYear)
        assert isinstance(self.cool, ReleaseCool)

    def to_dict(self) -> dict:
        return {
            "year": self.year.value,
            "cool": self.cool.value,
        }

    @staticmethod
    def from_dict(release_dict: dict) -> "Release":
        year, cool = Release.parse_season_dict(release_dict)
        return Release(
            ReleaseYear(year),
            ReleaseCool(cool),
        )

    @staticmethod
    def parse_season_dict(release_dict: dict) -> Tuple[int, str]:
        year, cool = release_dict.split("-")
        return (int(year), cool)

    def to_year(self) -> int:
        return self.year.value

    def to_cool(self) -> str:
        return self.cool.value


@dataclasses.dataclass
class Work:
    word_id: WorkId
    title: Title
    media: str
    media_text: str
    released_on: ReleasedOn
    url: Url
    twitter: Twitter
    episodes_count: EpisodesCount
    watchers_count: WatchersCount
    # release: Release
    no_episodes: Optional[bool] = None
    reviews_count: Optional[int] = None
    syobocal_tid: Optional[SyobocalTitleId] = None
    mal_anime_id: Optional[MyAnimeListAnimeId] = None
    images: Optional[Images] = None
    season_name: Optional[SeasonName] = None
    season_name_text: Optional[SeasonNameText] = None

    def to_dict(self) -> dict:
        return {
            "id": dataclasses.asdict(self.word_id)["value"],
            "title": dataclasses.asdict(self.title)["value"],
            "title_kana": dataclasses.asdict(self.title.kana)["value"],
            "media": self.media,
            "media_text": self.media_text,
            "released_on": dataclasses.asdict(self.released_on)["value"],
            "released_on_about": dataclasses.asdict(self.released_on.about)["value"],
            "official_site_url": dataclasses.asdict(self.url.official_site)["value"],
            "wikipedia_url": dataclasses.asdict(self.url.wikipedia)["value"],
            "twitter_username": dataclasses.asdict(self.twitter.username)["value"],
            "twitter_hashtag": dataclasses.asdict(self.twitter.hashtag)["value"],
            "episodes_count": dataclasses.asdict(self.episodes_count)["value"],
            "watchers_count": dataclasses.asdict(self.watchers_count)["value"],
            # "release": to_class(Release, self.release),
            "no_episodes": self.no_episodes if self.no_episodes is not None else None,
            "reviews_count": self.reviews_count
            if self.reviews_count is not None
            else None,
            "syobocal_tid": dataclasses.asdict(self.syobocal_tid)["value"]
            if dataclasses.asdict(self.syobocal_tid)["value"] is not None
            else None,
            "mal_anime_id": dataclasses.asdict(self.mal_anime_id)["value"]
            if dataclasses.asdict(self.mal_anime_id)["value"] is not None
            else None,
            "images": to_class(Images, self.images)
            if dataclasses.asdict(self.images) is not None
            else None,
            "season_name": dataclasses.asdict(self.season_name)["value"]
            if dataclasses.asdict(self.season_name)["value"] is not None
            else None,
            "season_name_text": dataclasses.asdict(self.season_name.text)["value"]
            if dataclasses.asdict(self.season_name.text)["value"] is not None
            else None,
        }

    @staticmethod
    def from_dict(work_dict: dict) -> "Work":
        assert isinstance(work_dict, dict)
        return Work(
            WorkId(work_dict["id"]),
            Title(
                work_dict["title"],
                TitleKana(work_dict["title_kana"]),
            ),
            Media[work_dict["media"]].name,
            Media[work_dict["media"]].value,
            ReleasedOn(
                work_dict["released_on"],
                releasedOnAbout(work_dict["released_on_about"]),
            ),
            Url(
                OfficialSiteUrl(work_dict["official_site_url"]),
                WikipediaUrl(work_dict["wikipedia_url"]),
            ),
            Twitter(
                TwitterUsername(work_dict["twitter_username"]),
                TwitterHashtag(work_dict["twitter_hashtag"]),
                TwitterImage.from_dict(work_dict["images"]["twitter"]),
            ),
            EpisodesCount(work_dict["episodes_count"]),
            WatchersCount(work_dict["watchers_count"]),
            # Release.from_dict(work_dict["season_name"])
            # if work_dict.get("season_name") is not None
            # else None,
            work_dict["no_episodes"]
            if work_dict.get("no_episodes") is not None
            else None,
            work_dict["reviews_count"]
            if work_dict.get("reviews_count") is not None
            else None,
            SyobocalTitleId(work_dict["syobocal_tid"])
            if work_dict.get("syobocal_tid") is not None
            else None,
            MyAnimeListAnimeId(work_dict["mal_anime_id"])
            if work_dict.get("mal_anime_id") is not None
            else None,
            Images(
                TwitterImage.from_dict(work_dict["images"]["twitter"]),
                Facebook.from_dict(work_dict["images"]["facebook"]),
                RecommendedUrl(work_dict["images"]["recommended_url"]),
            )
            if work_dict.get("images") is not None
            else None,
            SeasonName(
                work_dict["season_name"]
                if work_dict.get("season_name") is not None
                else None,
                SeasonNameText(work_dict["season_name_text"])
                if work_dict.get("season_name_text") is not None
                else None,
            ),
        )

    def get_cool(self) -> Tuple[int, Cool]:
        return self.season_name.get_cool()


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

    def find_by_media(self, target_media: str = "tv") -> list:
        result: List[dict] = []
        for work in self._list:
            if work.media == target_media:
                result.append(work.title)
        return result


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x
