import unittest

import sys
import pathlib

from PythonAutomation.lesson_09.homework_09_def import car_data_negative

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from homework_09_def import filter_cars, car_data, car_data_negative


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


if __name__ == "__main__":
    unittest.main()