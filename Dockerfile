# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Применяем миграции базы данных и запускаем сервер Django
CMD ["sh", "-c", "python manage.py migrate && gunicorn api_server.wsgi:application --bind 0.0.0.0:8000"]
