import unittest

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from homework_09_def import (total_area, filter_cars, car_data, car_data_negative,
                                                        sum_all_numbers)

class CarTest(unittest.TestCase):
    def test_filter_cars_positive(self):
        input_data = car_data
        actual_result = filter_cars(input_data, (2017, 1.6, 36000))
        expected_result = {'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
 'Kia': ('white', 2020, 2.0, 'sedan', 28000),
 'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
 'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
 'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000)}

        self.assertEqual( expected_result, actual_result)


    def test_filter_cars_negative(self):
        input_data = car_data_negative
        # actual_result = filter_cars(input_data, (2017, 1.6, 36000))
        # expected_result = {}
        with self.assertRaises(IndexError) as error:
            filter_cars(input_data, (2017, 1.6, 36000))
        actual_error = error.exception.args[0]
        expected_error = "Search criteria is invalid"
        self.assertEqual(expected_error, actual_error)


class AreaTest(unittest.TestCase):
    def test_total_area_positive(self):
        actual_result = total_area(436402,37800)
        expected_result = f"Площа Чорного та Азовського морів дорівнює: ,474202, км²"

        self.assertEqual(expected_result, actual_result)


    def test_total_area_negative(self):
        actual_result = total_area(436402,37800)
        expected_result = f"Площа Чорного та Азовського морів дорівнює: ,500000, км²"

        self.assertNotEqual(expected_result, actual_result)


class SumTest(unittest.TestCase):
    def test_sum_all_positive(self):
        input_data = ["1,2,3,4", "1,2,3,4,50"]
        actual_result = sum_all_numbers(input_data)
        expected_result = [10, 60]
        print(f"Input data: {input_data}")
        print(f"Actual result: {actual_result}", f"Expected result: {expected_result}")
        self.assertEqual(expected_result, actual_result)


    def test_sum_all_negative(self):
        input_data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
        actual_result = sum_all_numbers(input_data)
        expected_result = [10, 60, "Не можу це зробити!"]
        print(f"Input data: {input_data}")
        print(f"Actual result: {actual_result}", f"Expected result: {expected_result}")
        self.assertEqual(expected_result, actual_result)


    def test_sum_all_negative_with_two_arg(self):
        input_data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "5,5"]
        actual_result = sum_all_numbers(input_data)
        expected_result = [10, 60, "Не можу це зробити!", 10]
        print(f"Input data: {input_data}")
        print(f"Actual result: {actual_result}", f"Expected result: {expected_result}")
        self.assertEqual(expected_result, actual_result)


    def test_sum_all_negative_invalid_data(self):
        input_data = ["1,2,3,4", 2, "1,2,3,4,50"]
        actual_result = sum_all_numbers(input_data)
        expected_result = [10, 60]
        print(f"Input data: {input_data}")
        print(f"Actual result: {actual_result}", f"Expected result: {expected_result}")
        self.assertEqual(expected_result, actual_result)


    def test_sum_all_negative_positive_single_number(self):
        input_data = ["50"]
        actual_result = sum_all_numbers(input_data)
        expected_result = [50]
        print(f"Input data: {input_data}")
        print(f"Actual result: {actual_result}", f"Expected result: {expected_result}")
        self.assertEqual(expected_result, actual_result)


    def test_sum_all_negative_negative_none_input(self):
        input_data = []
        actual_result = sum_all_numbers(input_data)
        expected_result = []
        print(f"Input data: {input_data}")
        print(f"Actual result: {actual_result}", f"Expected result: {expected_result}")
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()