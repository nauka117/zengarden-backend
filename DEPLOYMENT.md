# Развертывание ZenGarden Backend на сервере

## Подготовка сервера

1. Убедитесь, что на сервере установлен Docker и Docker Compose
2. Склонируйте репозиторий на сервер

## Развертывание

### 1. Остановите существующие контейнеры (если есть)
```bash
docker compose down
```

### 2. Пересоберите образ без кэша
```bash
docker compose build --no-cache
```

### 3. Запустите приложение
```bash
docker compose up -d
```

### 4. Проверьте логи
```bash
docker compose logs -f api
```

## Проверка работы

1. Проверьте health check: `curl http://localhost:8000/health`
2. Откройте SwaggerUI: `http://your-server-ip:8000/docs`
3. Попробуйте авторизоваться с пользователем `111` и паролем `111`

## Устранение проблем

### Проблема с правами доступа к базе данных
Если возникает ошибка "unable to open database file":
1. Остановите контейнеры: `docker compose down`
2. Удалите volume: `docker volume rm zengarden-backend_database_data`
3. Пересоберите и запустите заново

### Проблема с портами
Если порт 8000 занят, измените его в `docker-compose.yml`:
```yaml
ports:
  - "8001:8000"  # Внешний порт 8001, внутренний 8000
```

## Структура данных

- База данных SQLite хранится в Docker volume `database_data`
- Файлы приложения монтируются из локальной директории `./app`
- Логи доступны через `docker compose logs api`

## Обновление приложения

Для обновления кода:
1. Остановите контейнеры: `docker compose down`
2. Обновите код в директории `./app`
3. Перезапустите: `docker compose up -d`

База данных сохранится в volume и не будет потеряна. 