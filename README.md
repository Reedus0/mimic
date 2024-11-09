# Установка

```
pip install -r requirements
```

# Запуск

```
python3 server.py
python3 main.py
```

Сначала запускаем сервер, а потом клиента. Перед запуском создать фалй config.json с параметрами конфигурации.
В веб-интерфейсе сервера по пути / есть возможность установить полезную нагрузку на бота.

# Тестовая конфигурация 

```
{
    "c2_address": "127.0.0.1",
    "c2_port": 80,
    "c2_url": "/c2.php",
    "c2_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'",
    "c2_content_type": "text/*",
    "username": "VladPC",
    "privileges": "Admin",
    "os_version": "Windows 10"
}
```