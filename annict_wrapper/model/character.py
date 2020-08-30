import dataclasses
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from annict_wrapper.model.series import Series


@dataclasses.dataclass
class Character:
    id: int
    name: str
    name_kana: str
    name_en: str
    nickname: str
    nickname_en: str
    birthday: str
    birthday_en: str
    age: str
    age_en: str
    blood_type: str
    blood_type_en: str
    height: str
    height_en: str
    weight: str
    weight_en: str
    nationality: str
    nationality_en: str
    occupation: str
    occupation_en: str
    description: str
    description_en: str
    description_source: str
    description_source_en: str
    favorite_characters_count: int
    series: Optional[Dict[str, Union[int, str]]] = None

    def __post_init__(self) -> None:
        if self.series is not None:
            self.series = Series(**self.series)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Characters:
    _list: List[Character] = dataclasses.field(default_factory=list)

    def append(self, character: Character) -> None:
        if isinstance(character, Character):
            self._list.append(character)
        else:
            raise TypeError("data is not character")

    def to_dict(self) -> list:
        return [l.to_dict() for l in self._list]
