import pytest
from .def_change_letters import change_letter

# @pytest.mark.positive
# class TestChangeLettersPositive:
#     def test_one_word(self):
#         input_data = "hello"
#         actual_result = change_letter(input_data)
#         expected_result = "HeLlO"
#         assert actual_result == expected_result
#
#     def test_big_sentence(self):
#         input_data = "Would you tell me, please, which way I ought to go from here?"
#         actual_result = change_letter(input_data)
#         expected_result = 'WoUlD yOu tElL mE, pLeAsE, wHiCh wAy i oUgHt tO gO fRoM hErE?'
#         assert actual_result == expected_result


@pytest.mark.positive
class TestChangeLettersPositive:

    @pytest.mark.parametrize('function_input, expected_result',[
        ("hello", "HeLlO"),
        ("Would you tell me, please, which way I ought to go from here?",
         'WoUlD yOu tElL mE, pLeAsE, wHiCh wAy i oUgHt tO gO fRoM hErE?'),
    ])
    def test_one_word_big_sentence(self, function_input, expected_result):
        assert change_letter(function_input) == expected_result


@pytest.mark.negative
class TestChangeLettersNegative:
    def test_empty_sentence(self):
        input_data = ''
        actual_result = change_letter(input_data)
        expected_result = ''
        assert actual_result == expected_result

    def test_int_argument_negative(self):
        with pytest.raises(TypeError) as error:
            change_letter(10)

    def test_int_as_string_negative(self):
        input_data = '-10292682681'
        actual_result = change_letter(input_data)
        expected_result = '-10292682681'
        assert actual_result == expected_result
