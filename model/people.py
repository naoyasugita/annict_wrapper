import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union


@dataclasses.dataclass
class People:
    id: int
    name: str
    name_kana: str
    name_en: str
    nickname: str
    nickname_en: str
    gender_text: str
    url: str
    url_en: str
    wikipedia_url: str
    wikipedia_url_en: str
    twitter_username: str
    twitter_username_en: str
    birthday: str
    blood_type: str
    height: int
    favorite_people_count: int
    casts_count: int
    staffs_count: int
    prefecture: Optional[Dict[str, Union[int, str]]]

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Peoples:
    _list: List[People] = dataclasses.field(default_factory=list)

    def append(self, people: People) -> None:
        if isinstance(people, People):
            self._list.append(people)
        else:
            raise TypeError("data is not people")

    def to_dict(self) -> list:
        return [dataclasses.asdict(l) for l in self._list]
