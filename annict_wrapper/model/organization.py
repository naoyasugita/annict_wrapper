import dataclasses
from typing import List


@dataclasses.dataclass
class Organization:
    id: int
    name: str
    name_kana: str
    name_en: str
    url: str
    url_en: str
    wikipedia_url: str
    wikipedia_url_en: str
    twitter_username: str
    twitter_username_en: str
    favorite_organizations_count: int
    staffs_count: int

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


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
