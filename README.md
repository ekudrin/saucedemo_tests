# Saucedemo tests

Автоматизированные UI-тесты для проверки авторизации на сайте  
https://www.saucedemo.com/

## Используемые технологии
- Python 3.10
- Pytest
- Selenium WebDriver
- Allure Reports
- Docker

---


## Запуск тестов

В корне проекта выполнить команду:

```bash
docker-compose up --build
```

Для просмотра Allure-отчета:
```bash
cd allure-report
python -m http.server 8000
```
Открыть в браузере:
http://localhost:8000