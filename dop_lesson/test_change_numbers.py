import pytest


from PythonAutomation.dop_lesson.def_change_numbers import first_or_last_bigger

class TestChangeNumbersPositive:

    def test_first_or_last_bigger_positive(self):
        input_numbers = [17,5,9,17,28,68,95]
        expected_results = [95, 95, 95, 95, 95, 95, 95]
        actual_results = first_or_last_bigger(input_numbers)
        assert expected_results == actual_results