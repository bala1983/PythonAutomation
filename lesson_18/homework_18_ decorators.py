import functools
import logging

logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger('log')

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Виклик: {func.__name__} з аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Результат: {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(5, 7)


def catch_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка у функції {func.__name__}: {e}")
            return None
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))
