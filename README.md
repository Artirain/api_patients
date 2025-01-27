# Проект API-сервера с JWT-авторизацией и Docker

Этот проект представляет собой сервер на Django с двумя основными эндпоинтами: `/login` для получения JWT-токенов и `/patients` для получения списка пациентов, доступного только для пользователей с ролью `doctor`.

## Структура репозитория

1. **`tests/`** — папка с тестами.
2. **`api/`** — папка с кодом (Приложение API).
3. **`api_server/`** — папка с кодом (settings).
4. **`Dockerfile, docker-compose.yml`** — файлы конфигурации для Docker.

## Инструкции по локальному запуску

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/Artirain/api_patients
   cd api_server

2. Создание виртуального окружения
   ```
   python -m venv venv
   .\venv\Scripts\activate

3. Установка зависимостей
Установите все необходимые зависимости из requirements.txt:
   ```
   pip install -r requirements.txt

4. Применение миграций
   ```
   python manage.py migrate

5. Запуск локального сервера
   ```
   python manage.py runserver

6. Тесты
   ```
   pytest --cov=api tests/

Инструкции по запуску в Docker
   1. Построение и запуск контейнеров
      ```
      docker-compose build
      docker-compose up

   2. Остановка контейнеров
   Для остановки контейнеров выполните команду:
   ```
   docker-compose down
   ```
#Проверка эндпоинтов
Используйте инструмент для тестирования API, например, Postman или curl.

Эндпоинт /login
   Метод: POST
   URL: http://127.0.0.1:8000/login
   Параметры запроса:
   ```
   {
     "username": "имя_пользователя",
     "password": "пароль"
   }
   ```
   Ответ:
   ```{
     "access": "jwt_access_token",
     "refresh": "jwt_refresh_token"
   }
   ```

Эндпоинт /patients
   Метод: GET
   URL: http://127.0.0.1:8000/patients
   Заголовок авторизации:
   ```
   Authorization: Bearer jwt_access_token
   ```
