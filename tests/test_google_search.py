import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage



def test_find_book_via_page_object():
    """
    Тот же тест, но через Page Object Model.
    Тест не знает как устроена страница - он использует класс MainPage.
    """

    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Создаём объект страницы
        main_page = MainPage(driver)
        
        # Открываем страницу
        main_page.open()

        # Ждём загрузки
        driver.implicitly_wait(2)

        # Получаем названия книг через Page Object (а не напрямую)
        book_titles = main_page.get_all_book_titles()
        book_count = main_page.get_book_count()

        print(f"Найдено книг на странице: {book_count}")


        # Проверяем, что книга есть
        target_book = "A Light in the Attic"
        assert target_book in book_titles, (
            f"Книга '{target_book}' не найдена!"
        )

        print(f"ТЕСТ ПРОЙДЕН: Книга '{target_book}' найдена через Page Object!")

    finally:
        driver.quit()