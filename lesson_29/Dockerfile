# Використовуємо офіційний образ Python версії 3.9
FROM python:3.11

# Встановлюємо залежності для тестування
RUN pip install --no-cache-dir sqlalchemy psycopg2-binary pytest

# Копіюємо файли з локальної директорії в контейнер

# Задаємо робочу директорію контейнера
WORKDIR /app
ENV PYTHONPATH=/app
COPY . /app

# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["pytest", "-m","db_test"]