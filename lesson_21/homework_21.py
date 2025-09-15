# Моніторингова система клєнта надсилає сигнал, що вона працездатна кожні 30-31 сек - наприкладTimestamp 05:45:40,
# а в наступному повідомлені — Timestamp 05:45:09 (тут різниця heartbeat в 31 секунду)
# Є декілька дублючих потоків, що шлють дані одночасно, тож ми можемо проаналізувати лише один потік - Key TSTFEED0300|7E3E|0400
# Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt
# відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
# Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
# для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
# для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
# 3.Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.
# Обов’язково включіть результат роботи — файл hb_test.log в PR.
# Підказка 1
# Прочитайте файл по строкам, якщо забули як - зверніться до 12 лекції.
# Виберіть строки з необхідним значенням:
# filtered_log = []
# if "key" in "long log string with key":
#     filtered_log.append("long log string with key")
# Підказка 2
# Пошук часу у строці можна зробити методом .find("Timestamp ") і повернути наступні 8 символів
# перетворити строку в час дозволяє метод .strptime("10:00:00", "%H:%M:%S")
# Значення слід аналізувати парами - від поточного відняти наступне і залогувати (або не залогувати) результат

from datetime import datetime
import logging

logger = logging.Logger('time analysis')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('new_log.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

key = 'TSTFEED0300|7E3E|0400'
log_file = 'hblog.txt'
new_log = 'new_log.log'

filtered_log = []
with open(log_file, "r") as file:
    lenes = file.readlines()

for line in lenes:
    if key in line:
        filtered_log.append(line)

timestamp_list = []

for fil_line in filtered_log:
    start_index = fil_line.find('Timestamp ') + len('Timestamp ')
    end_index = start_index + 8
    timestamp_string = fil_line[start_index:end_index]
    timestamp = datetime.strptime(timestamp_string, "%H:%M:%S")
    timestamp_list.append(timestamp)

for index in range(len(timestamp_list)-1):
    current_time = timestamp_list[index]
    next_time = timestamp_list[index + 1]
    difference_time = (current_time - next_time).total_seconds()
    if 33 > difference_time > 31:
        logger.warning(f"Heartbeat more 31 sec but less 33 sec, it happened in: {current_time.strftime("%H:%M:%S")}")
    elif difference_time >= 33:
        logger.error(f"Heartbeat more or equal 33 sec, it happened in: {current_time.strftime("%H:%M:%S")}")
