# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(num1, num2):
    return num1 + num2
sum_of_two_numbers(1, 2)

print(sum_of_two_numbers(10, 20))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_sum(numbers):
    return int(sum(numbers) / len(numbers))

arithmetic_sum([1, 2, 3, 4, 5])
print(arithmetic_sum([1, 2, 3, 4, 5]))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_order(string):
    return string[::-1]
reverse_order("hello world")
print(reverse_order("hello world"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    words_array = [x.replace(",", "").strip() for x in words.split()]
    # print(words_array)
    longest_word = max(words_array, key=len)
    longest_words = []
    for word in words_array:
        if len(longest_word) == len(word):
            longest_words.append(word)
    return longest_words

print(longest_word("Написати функцію, яка приймає список слів та повертає найдовше слово у списку"))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

def total_area(area1, area2):
    area = area1 + area2
    return f"Площа Чорного та Азовського морів дорівнює: ,{area}, км²"
print(total_area(area1=436402, area2=37800))


def warehouses(total_warehouses, first_warehouse_and_second_warehouse, second_warehouse_and_third_warehouse):
    second = first_warehouse_and_second_warehouse + second_warehouse_and_third_warehouse - total_warehouses
    first = first_warehouse_and_second_warehouse - second
    third = second_warehouse_and_third_warehouse - second
    return f"Перший склад: {first}, Другий склад: {second}, Третій склад: {third}"
print(warehouses(375291, 250449,222950))


def pc_price(mouths, years, monthly_payment):
    mouths = mouths * years
    price = int(mouths * monthly_payment)
    return f"Вартість комп'ютера: {price} грн."
print(pc_price(12, 1.5,1179))


def number_of_pages_in_album(photos, per_page):
    all_pages = (photos + per_page -1) // per_page
    return f"Потрібно сторінок: {all_pages}"
print(number_of_pages_in_album(232,8))



