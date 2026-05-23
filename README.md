# Автотесты на Selenium

Разработчик: Смирнов Илья | Python, Selenium, PyTest

---

## Что это за проект

Автоматизированные тесты веб-интерфейса с использованием Selenium WebDriver. Проект создан для демонстрации навыков автоматизации тестирования.

---

## Что проект умеет

- Запускает браузер Chrome и выполняет действия как реальный пользователь
- Ищет элементы на странице по CSS-селекторам
- Проверяет наличие данных (книг) на странице
- Использует PyTest для запуска тестов

---

## Технологии

| Категория | Инструменты |
|-----------|-------------|
| Язык | Python 3.13 |
| Браузерная автоматизация | Selenium WebDriver |
| Браузер | Google Chrome |
| Тестовый фреймворк | PyTest |
| Контроль версий | Git, GitHub |

---

## Как запустить

```
git clone https://github.com/mackros-333/selenium-tests.git
cd selenium-tests
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

---
## Структура проекта
~~~
selenium-tests/
├── tests/
│   └── test_google_search.py    # Поиск книги на books.toscrape.com
├── requirements.txt
└── README.md
~~~
---
## Связь
📫 email: zaraza.my@mail.ru