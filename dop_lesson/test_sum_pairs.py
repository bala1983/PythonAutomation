import pytest

from .def_sum_pairs import sum_pairs

class TestSumPairs:

    @pytest.mark.parametrize('list_of_integers, target_number, expected_result',[
        ([1, 2, 3, 4, 6], 7, [(1, 6), (3, 4), (4, 3), (6, 1)]),
        ([-1, -2, 3, -4, -6], -7, [(-1, -6), (-6, -1)]),
    ])
    def test_sum_pairs_positive(self, list_of_integers, target_number, expected_result):
        actual_result = sum_pairs(list_of_integers, target_number)
        assert actual_result == expected_result

    def test_sum_pairs_negative(self):
        with pytest.raises(ValueError):
            list_of_integers = [1, 2, 3, 4, 6]
            target_number = "7/"
            sum_pairs(list_of_integers, target_number)
