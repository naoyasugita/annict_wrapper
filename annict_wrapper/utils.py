from datetime import datetime
from typing import Any
from typing import Type
from typing import TypeVar
from typing import cast

import dateutil.parser

from annict_wrapper.model.work import Cool


def delete_none_for_dict(dic: dict):
    new_dic = {}
    for k, v in dic.items():
        if v is not None:
            new_dic[k] = v
    return new_dic


def create_season_by_year_and_cool(year: int, cool: Cool) -> str:
    return str(year) + "-" + cool.name


def check_date_format(d: str) -> bool:
    try:
        datetime.strptime(d, "%Y/%m/%d %H:%M")
        return True
    except ValueError:
        return False

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
