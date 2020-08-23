from typing import Dict
from typing import Optional
from typing import Union
import dataclasses


@dataclasses.dataclass
class Episodes:
    id: int
    number: Optional[int]
    number_text: str
    sort_number: int
    title: str
    records_count: int
    record_comments_count: int
    work: Dict[str, Union[int, str]]
    prev_episode: Dict[str, Optional[Union[int, str]]]
    next_episode: Optional[int]
    prefecture: Optional[Dict[str, Union[int, str]]]

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
