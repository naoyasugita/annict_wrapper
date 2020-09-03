import pytest

from annict_wrapper.model.program import Program
from annict_wrapper.model.program import Programs


class TestProgramModel:
    def test_to_dict(self, fixture_program):
        program_dict = fixture_program["program_dict"]
        assert Program(**program_dict).to_dict() == program_dict


class TestProgramsModel:
    def test_programs_append_when_type_ok(self, fixture_program):
        programs = Programs()
        program = fixture_program["program"]
        program_2 = fixture_program["program"]
        programs.append(program)
        programs.append(program_2)
        assert len(programs._list) == 2

    def test_programs_append_when_type_error(self):
        programs = Programs()
        with pytest.raises(TypeError):
            programs.append("dammy")

    def test_programs_to_dict(self, fixture_program):
        programs = Programs()
        program = fixture_program["program"]
        program_dict = fixture_program["program_dict"]
        programs.append(program)
        assert programs.to_dict() == [program_dict]
