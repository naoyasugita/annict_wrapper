import dataclasses


@dataclasses.dataclass
class Organizations:
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
