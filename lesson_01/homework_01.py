# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f"периметр фігури: {perimetery}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
yabluku = 4
grushi = yabluku + 5
slivu = yabluku - 2
usi_dereva = yabluku + grushi + slivu
print(f"всього дерев: {usi_dereva}")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
do_obeda = 5
pislya_odeda = do_obeda - 10
nadvechir = pislya_odeda + 4
print(f"температура надвечір: {nadvechir}")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
hlopchyky = 24
divchata = hlopchyky // 2  # можно також використовувати /
sogodni_hlopchyky = hlopchyky - 1
sogodni_divchata = divchata -2
usi = sogodni_hlopchyky + sogodni_divchata
print(f"сьогодні дітей: {usi}")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
persha_knuga = 8
druga_knuga = persha_knuga + 2
tretya_knuga = (persha_knuga + druga_knuga) // 2
usi_knugu = persha_knuga + druga_knuga + tretya_knuga
print(f"усі книги коштують: {usi_knugu}")