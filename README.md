# API-сервер для работы с пациентами
Структура репозитория

my_project/
├── code/                   # Исходный код приложения
│   ├── api/                # Приложение API
│   ├── manage.py           # Скрипт для управления проектом
│   ├── settings.py         # Настройки Django проекта
│   └── urls.py             # URL-ы проекта
├── docker/                 # Docker-файлы
│   ├── Dockerfile          # Dockerfile для приложения
│   └── docker-compose.yml  # Docker Compose файл для запуска контейнера
├── migrations/             # Миграции базы данных
├── tests/                  # Тесты
│   ├── test_api.py         # Тесты для API
├── requirements.txt        # Зависимости проекта
└── README.md               # Этот файл
