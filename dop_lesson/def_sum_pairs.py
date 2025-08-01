# Дано список цілих чисел та цільове число. Поверніть усі унікальні пари чисел зі списку, які утворюють цю суму.
# [1,2,3,4,6] - 7
# (1,6), (3,4) (4,3) (6,1)
import logging


def sum_pairs(list_of_integers, target_number):
    result_list_of_pairs = []
    target_number = int(target_number)
    for first_addition in list_of_integers:
        for second_addition in list_of_integers:
            if first_addition + second_addition == target_number:
                result_list_of_pairs.append((first_addition, second_addition))
                logging.info(f"Result success: {first_addition} + {second_addition} = {target_number}")
            else:
                logging.warning(f"Pay attention: {first_addition} + {second_addition} Not equal to {target_number}")

    return result_list_of_pairs





