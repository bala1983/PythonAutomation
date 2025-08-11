# Дано список цілих чисел.
# Визначити, який елемент більший: перший чи останній у списку,
# і встановити всі інші елементи списку на це значення.
# Повернути змінений список.
# first = 100
# last = 20
#
# if first < last:
#     bigger = last
# else:
#     bigger = first
# print(bigger)

# input_numbers = [17,5,9,17,28,68,95]

def first_or_last_bigger(our_list):
    result_list = []
#     if our_list[0] < our_list[-1]: # це озназачає що останній більшій за перший
#         result_list = [our_list[-1] for x in range(len(our_list))]
#     else:
#         result_list = [our_list[0] for x in range(len(our_list))]
#     return result_list
# print(first_or_last_bigger(input_numbers))

    if our_list[0] < our_list[-1]:
        bigger_number = our_list[-1]
    else:
        bigger_number = our_list[0]

    for index, number in enumerate(our_list):
        our_list[index] = bigger_number
    return our_list
# print(first_or_last_bigger(input_numbers))



