import dataclasses
from enum import Enum
from enum import auto
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union


class Cool(Enum):
    spring = auto()
    summer = auto()
    autumn = auto()
    winter = auto()
    all = auto()


class Media(Enum):
    tv = auto()
    ova = auto()
    movie = auto()
    web = auto()
    other = auto()


@dataclasses.dataclass
class Work:
    id: int
    title: str
    title_kana: str
    media: str
    media_text: str
    released_on: str
    released_on_about: str
    official_site_url: str
    wikipedia_url: str
    twitter_username: str
    twitter_hashtag: str
    syobocal_tid: str
    mal_anime_id: str
    images: Dict[str, Union[str, Dict[str, str]]]
    episodes_count: int
    watchers_count: int
    reviews_count: int
    no_episodes: bool
    season_name: Optional[str] = None
    season_name_text: Optional[str] = None

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)

    def get_cool(self) -> Tuple[int, Cool]:
        release_year = int(self.season_name.split("-")[0])
        season = Cool[self.season_name.split("-")[1]]
        return (release_year, season)


@dataclasses.dataclass
class Works:
    _list: List[Work] = dataclasses.field(default_factory=list)

    def append(self, work: Work) -> None:
        if isinstance(work, Work):
            self._list.append(work)
        else:
            raise TypeError("data is not work")

    def to_dict(self) -> list:
        return [work.to_dict for work in self._list]

    def find_by_media(self, target_media: str = "tv") -> list:
        result: List[dict] = []
        for work in self._list:
            if work.media == target_media:
                result.append(work.title)
