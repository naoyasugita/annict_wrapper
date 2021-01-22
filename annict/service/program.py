import dataclasses

from annict.model.program import Program
from annict.model.program import Programs
from annict.request import ApiRequests
from annict.request_filter import ProgramRequestParams


@dataclasses.dataclass
class ProgramService:
    api: ApiRequests

    def find_program_info(self, program_id: int) -> Program:
        params = ProgramRequestParams(filter_ids=program_id).to_dict()
        res = self.api.programs(params=params)
        try:
            return Program.from_dict(res["programs"][0])
        except Exception as e:
            raise e

    def find_all_program_info(self) -> Programs:
        # TODO データ永続化処理で使用する
        programs = Programs()
        per_page = 50  # limit_count
        page = 1  # init_page
        while page is not None:
            params = ProgramRequestParams(per_page=per_page, page=page).to_dict()
            res = self.api.programs(params=params)
            page = res["next_page"]
            for program in res["programs"]:
                programs.append(Program(**program))
        return programs

    def find_program_info_by_work_id(self, word_id: int) -> Program:
        params = ProgramRequestParams(filter_work_ids=word_id).to_dict()
        res = self.api.programs(params=params)
        try:
            return Program.from_dict(res["programs"][0])
        except Exception as e:
            raise e
