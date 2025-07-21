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