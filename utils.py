from model.work import Cool


def delete_none_for_dict(dic: dict):
    new_dic = {}
    for k, v in dic.items():
        if v is not None:
            new_dic[k] = v
    return new_dic


def create_season_by_year_and_cool(year: int, cool: Cool) -> str:
    return str(year) + "-" + cool.name
