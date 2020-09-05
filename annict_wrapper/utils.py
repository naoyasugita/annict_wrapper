from datetime import datetime

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
