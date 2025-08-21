import pytest

from PythonAutomation.lesson_16.homework_16 import TeamLead

class TestTeamLeadPositeve:
    def test_attributes(self):
        team_lead = TeamLead('Oleg', '5000', 'QA', '7')
        expected_name = 'Oleg'
        expected_salary = '5000'
        expected_department = 'QA'
        expected_team_size = '7'
        assert team_lead.name == expected_name
        assert team_lead.salary == expected_salary
        assert team_lead.department == expected_department
        assert team_lead.team_size == expected_team_size

    def test_has_attributes(self):
        team_lead = TeamLead('Oleg', '5000', 'QA', '7')
        assert hasattr(team_lead, 'name')
        assert hasattr(team_lead, 'salary')
        assert hasattr(team_lead, 'department')
        assert hasattr(team_lead, 'team_size')


class TestTeamLeadNegative:
    def test_has_attributes(self):
        team_lead = TeamLead('Oleg', '5000', 'QA', '7')
        # assert hasattr(team_lead, 'name')
        # assert hasattr(team_lead, 'salary')
        # assert hasattr(team_lead, 'department')
        # assert hasattr(team_lead, 'team_size')
        assert hasattr(team_lead, 'programming_language') == False