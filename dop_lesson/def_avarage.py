#Повернути "центроване" середнє значення першочергового списку цілих чисел, яке є середнім значенням елементів,
# за винятком найбільшого та найменшого значень у списку.
# Якщо є кілька копій найменшого значення, ігнорувати лише одну копію, так само із найбільшим значенням.
# Використовуйте цілочисельне ділення для обчислення кінцевого середнього.
# Можна припускати, що довжина списку дорівнює 3 або більше.
# 0. прибрати найменьше та найбільше значення
# 1. рахуємо середнє значення (плюсуємо усі елементи і ділемо на кількість елементів)

list_of_numbers1 = [7,12,7,95,15,66]
list_of_numbers2 = [7,12,7,95,15,87]

def avarage_excluding(input_list) -> int:
    min_number = min(input_list)
    max_number = max(input_list)
    len_before_remove = len(input_list)
    input_list.remove(min_number)
    input_list.remove(max_number)
    avarage_result = sum(input_list)//len_before_remove

    return avarage_result

# avarage_excluding(list_of_numbers1) результат не записується нікуди
# avarage_excluding(list_of_numbers2)

result1 = avarage_excluding(list_of_numbers1)
result2 = avarage_excluding(list_of_numbers2)

print(result1, result2)