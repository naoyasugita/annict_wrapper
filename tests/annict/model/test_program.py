import pytest
from annict.model.program import Program
from annict.model.program import Programs


class TestProgramModel:
    def test_to_dict(self, fixture_program):
        actual = fixture_program["to_dict"]

        program = fixture_program["program"]
        expected = program.to_dict()

        assert actual == expected

    def test_from_dict(self, fixture_program):
        actual = fixture_program["program"]

        program_dict = fixture_program["program_dict"]
        expected = Program.from_dict(program_dict)

        assert actual == expected


class TestProgramsModel:
    def test_programs_append_when_type_ok(self, fixture_program):
        programs = Programs()
        program = fixture_program["program"]
        program_2 = fixture_program["program"]
        programs.append(program)
        programs.append(program_2)
        expected = len(programs._list)

        actual = 2

        assert actual == expected

    def test_programs_append_when_type_error(self):
        programs = Programs()
        with pytest.raises(TypeError):
            programs.append("dammy")

    def test_programs_to_dict(self, fixture_program):
        programs = Programs()
        program = fixture_program["program"]
        programs.append(program)
        expected = programs.to_dict()

        program_dict = fixture_program["to_dict"]
        actual = [program_dict]

        assert actual == expected
