import pytest
from annict.model.program import Program
from annict.model.program import Programs


class TestProgramModel:
    def test_to_dict(self, fixture_program):
        actual = fixture_program["program_dict"]

        program = fixture_program["program"]
        excepted = program.to_dict()

        assert actual == excepted

    def test_from_dict(self, fixture_program):
        actual = fixture_program["program"]

        program_dict = fixture_program["program_dict"]
        excepted = Program.from_dict(program_dict)

        assert actual == excepted


class TestProgramsModel:
    def test_programs_append_when_type_ok(self, fixture_program):
        programs = Programs()
        program = fixture_program["program"]
        program_2 = fixture_program["program"]
        programs.append(program)
        programs.append(program_2)
        excepted = len(programs._list)

        actual = 2

        assert actual == excepted

    def test_programs_append_when_type_error(self):
        programs = Programs()
        with pytest.raises(TypeError):
            programs.append("dammy")

    def test_programs_to_dict(self, fixture_program):
        programs = Programs()
        program = fixture_program["program"]
        programs.append(program)
        excepted = programs.to_dict()

        program_dict = fixture_program["program_dict"]
        actual = [program_dict]

        assert actual == excepted
