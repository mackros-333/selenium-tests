import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_find_book_on_page():
    """
    Тест: открыть books.toscrape.com и найти книгу по названию.
    """

    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Шаг 1: Открыть сайт
        driver.get("https://books.toscrape.com")
        driver.implicitly_wait(2)

        # Шаг 2: Найти все заголовки книг (теги h3, внутри — ссылка с названием)
        # Ищем все теги <h3>, внутри них <a> с атрибутом title
        book_titles = []
        book_elements = driver.find_elements(By.CSS_SELECTOR, "h3 a")

        for element in book_elements:
            title = element.get_attribute("title")
            if title:
                book_titles.append(title)

        print(f"Найдено книг на странице: {len(book_titles)}")

        # Шаг 3: Проверить, что нужная книга есть в списке
        target_book = "A Light in the Attic"
        assert target_book in book_titles, (
            f"Книга '{target_book}' не найдена! Книги на странице: {book_titles[:5]}..."
        )

        print(f"ТЕСТ ПРОЙДЕН: Книга '{target_book}' найдена на странице!")

    finally:
        driver.quit()