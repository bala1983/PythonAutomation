alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?" \n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that, said the Cat, "if you only walk long enough."')

print (alice_in_wonderland)
print("Кількість одинарних лапок:", alice_in_wonderland.count("'"))

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print("Площа Чорного та Азовського морів дорівнює:" ,total_area, "км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
usi_sklady = 375291
first_and_second = 250449
second_and_third = 222950

second = first_and_second + second_and_third - usi_sklady
first = first_and_second - second
third = second_and_third - second

print("Перший склад:", first)
print("Другий склад:", second)
print("Третій склад:", third)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = 12 * 1.5
monthly_payment = 1179
pc_price = int(months * monthly_payment)
print("Вартість комп'ютера:", pc_price, "грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("остача від діленя a дрівеює:", a)
print("остача від діленя b дрівеює:", b)
print("остача від діленя c дрівеює:", c)
print("остача від діленя d дрівеює:", d)
print("остача від діленя e дрівеює:", e)
print("остача від діленя f дрівеює:", f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_kilkist = 4
medium_pizza_kilkist = 2
sik_kilkist = 4
tort_kilkist = 1
voda_kilkist = 3

big_pizza = 274
medium_pizza = 218
sik = 35
tort = 350
voda = 21

big_pizza_total = big_pizza_kilkist * big_pizza
medium_pizza_total = medium_pizza_kilkist * medium_pizza
sik_total = sik_kilkist * sik
tort_total = tort_kilkist * tort
voda_total = voda_kilkist * voda

total_money = (big_pizza_total + medium_pizza_total + sik_total + tort_total + voda_total)

print("Загальна сума замовлення:", total_money, "грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
per_page = 8
all_pages = (photos + per_page - 1) // per_page # або такий варіант all_pages = photos / per_page
print("Потрібно сторінок:", all_pages)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
bak = 48
vidstan = 1600
kojni_100km = 9

total_gas = vidstan // 100 * kojni_100km
vidstan_1bak = (bak // kojni_100km) * 100
total_zapravok = vidstan // vidstan_1bak

print("Потрібно бензину:", total_gas, "л")
print("Мінімальна кількість заправок:", total_zapravok)