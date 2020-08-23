from typing import Dict
from typing import Union
import dataclasses


@dataclasses.dataclass
class Staff:
    id: int
    name: str
    name_en: str
    role_text: str
    role_other: str
    role_other_en: str
    sort_number: int
    work: Dict[str, Union[int, str]]
    organization: Dict[str, Union[int, str]]

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
