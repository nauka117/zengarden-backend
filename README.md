# ZenGarden Backend

Backend-сервис для планирования и управления цветочным садом, построенный на FastAPI.

## 🚀 Возможности

- **FastAPI REST API** - современный и быстрый веб-фреймворк
- **SQLAlchemy ORM** с SQLite базой данных
- **JWT аутентификация** для безопасного доступа
- **CORS поддержка** для веб-приложений
- **Docker контейнеризация** для простого развертывания
- **Автоматическая документация API** (Swagger UI)

## 🛠 Быстрый старт

### Вариант 1: Docker (Рекомендуется)

1. **Сборка и запуск с Docker Compose:**
   ```bash
   docker-compose up --build
   ```

2. **Или сборка и запуск с Docker напрямую:**
   ```bash
   docker build -t zengarden-backend .
   docker run -p 8000:8000 zengarden-backend
   ```

3. **Доступ к API:**
   - API: http://localhost:8000
   - Документация: http://localhost:8000/docs
   - Проверка здоровья: http://localhost:8000/health

### Вариант 2: Локальная разработка

1. **Создание виртуального окружения:**
   ```bash
   # Для bash/zsh
   python -m venv .venv
   source .venv/bin/activate
   
   # Для fish shell
   python -m venv .venv
   source .venv/bin/activate.fish
   ```

2. **Установка зависимостей:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Запуск приложения:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## 🔧 Настройка разработки

1. **Установка зависимостей для разработки:**
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Запуск тестов:**
   ```bash
   pytest
   ```

3. **Форматирование кода:**
   ```bash
   black .
   ```

4. **Проверка кода:**
   ```bash
   flake8 .
   ```

## 📡 API Endpoints

- `GET /health` - Проверка состояния сервиса
- `GET /api/v1/` - Корень API
- `POST /api/v1/auth/login` - Авторизация пользователя
- `GET /api/v1/flowers` - Получение списка цветов
- `POST /api/v1/flowers` - Создание нового цветка

## 🔐 Переменные окружения

Приложение использует следующие переменные окружения (с значениями по умолчанию):

- `SECRET_KEY`: Секретный ключ для JWT (по умолчанию: "your-secret-key-keep-it-secret")
- `ALGORITHM`: Алгоритм JWT (по умолчанию: "HS256")
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Время жизни токена в минутах (по умолчанию: 30)
- `SQLALCHEMY_DATABASE_URL`: URL базы данных (по умолчанию: "sqlite:///./data/flowers.db")

## 🚀 Развертывание на сервере

### Подготовка сервера

1. Убедитесь, что на сервере установлен Docker и Docker Compose
2. Склонируйте репозиторий на сервер

### Процесс развертывания

1. **Остановите существующие контейнеры (если есть):**
   ```bash
   docker compose down
   ```

2. **Пересоберите образ без кэша:**
   ```bash
   docker compose build --no-cache
   ```

3. **Запустите приложение:**
   ```bash
   docker compose up -d
   ```

4. **Проверьте логи:**
   ```bash
   docker compose logs -f api
   ```

### Проверка работы

1. Проверьте health check: `curl http://localhost:8000/health`
2. Откройте SwaggerUI: `http://your-server-ip:8000/docs`
3. Попробуйте авторизоваться с пользователем `111` и паролем `111`

### Обновление приложения

Для обновления кода:
1. Остановите контейнеры: `docker compose down`
2. Обновите код в директории `./app`
3. Перезапустите: `docker compose up -d`

База данных сохранится в volume и не будет потеряна.

## 🐛 Устранение проблем

### Проблемы с IDE

Если IDE не может автоматически установить пакеты:

1. **Убедитесь, что используется правильный Python интерпретатор:**
   - Укажите IDE путь к `.venv/bin/python`
   - Для VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter" → Выберите `.venv/bin/python`

2. **Для пользователей fish shell:**
   - Используйте `source .venv/bin/activate.fish` вместо `source .venv/bin/activate`
   - Некоторые IDE могут требовать ручной настройки для fish shell

3. **Ручная установка:**
   ```bash
   source .venv/bin/activate.fish  # или activate для bash
   pip install -r requirements.txt
   ```

### Проблемы с Docker

1. **Ошибка сборки:**
   - Убедитесь, что Docker запущен
   - Проверьте наличие всех файлов (Dockerfile, requirements.txt)
   - Попробуйте `docker system prune` для очистки кэша

2. **Конфликты портов:**
   - Измените порт в docker-compose.yml, если 8000 уже занят
   - Используйте `docker-compose up -p 8001` для использования другого порта

3. **Проблемы с базой данных:**
   - Файл SQLite базы данных монтируется как volume
   - Убедитесь, что файл имеет правильные права доступа

### Проблема с правами доступа к базе данных

Если возникает ошибка "unable to open database file":
1. Остановите контейнеры: `docker compose down`
2. Удалите volume: `docker volume rm zengarden-backend_database_data`
3. Пересоберите и запустите заново

## 🏗 Структура проекта

```
zengarden-backend/
├── app/
│   ├── api/v1/          # API endpoints
│   ├── core/            # Конфигурация и безопасность
│   ├── db/              # Настройка базы данных
│   ├── models/          # SQLAlchemy модели
│   ├── schemas/         # Pydantic схемы
│   └── main.py          # FastAPI приложение
├── Dockerfile           # Docker конфигурация
├── docker-compose.yml   # Docker Compose настройка
├── requirements.txt     # Продакшн зависимости
├── requirements-dev.txt # Зависимости для разработки
└── README.md           # Этот файл
```

## 🔒 Продакшн настройки

Для продакшн развертывания:

1. **Используйте переменные окружения для секретов:**
   ```bash
   export SECRET_KEY="your-production-secret-key"
   export SQLALCHEMY_DATABASE_URL="postgresql://user:pass@host/db"
   ```

2. **Рассмотрите использование PostgreSQL вместо SQLite:**
   - Раскомментируйте postgres сервис в docker-compose.yml
   - Обновите URL базы данных

3. **Добавьте правильные CORS origins:**
   - Обновите CORS конфигурацию в `app/main.py`

4. **Используйте reverse proxy (nginx) для продакшна**

## 📝 Тестирование

### Быстрая проверка настройки

```bash
# 1. Убедитесь в правильном Python интерпретаторе
which python  # Должен указывать на .venv/bin/python

# 2. Переустановите пакеты при необходимости
source .venv/bin/activate.fish
pip install -r requirements.txt --upgrade

# 3. Протестируйте приложение
python -c "from app.main import app; print('✅ Успех')"
```

### Проверка Docker

```bash
# Установка Docker (Arch Linux)
sudo pacman -S docker docker-compose
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

# Сборка и запуск
docker-compose up --build
```

## 🆘 Поддержка

Если у вас продолжаются проблемы:

1. Проверьте логи в панели вывода вашей IDE
2. Запустите скрипт настройки: `./setup_dev.sh`
3. Проверьте путь к Python интерпретатору в вашей IDE
4. Протестируйте с помощью health check endpoint
