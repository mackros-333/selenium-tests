from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage:
    """
    Page Object для главной страницы books.toscrape.com.
    Этот класс знает, где находятся элементы на странице.
    """

    # URL страницы
    URL = "https://books.toscrape.com"

    def __init__(self, driver: WebDriver):
        """
        При создании страницы даём ей драйвер (браузер).
        """
        self.driver = driver

    def open(self):
        """
        Открывает страницу в браузере.
        """
        self.driver.get(self.URL)

    def get_all_book_titles(self):
        """
        Возвращает список названий всех книг на странице.
        Если дизайн изменится - править только здесь, а не в 10 тестах.
        """
        titles = []
        # Находим все элементы h3 a (заголовок → ссылка)
        book_elements = self.driver.find_elements(By.CSS_SELECTOR, "h3 a")

        for element in book_elements:
            title = element.get_attribute("title")
            if title:
                titles.append(title)

        return titles
    
    def get_book_count(self):
        """
        Возвращает количество книг на страницы.
        """
        titles = self.get_all_book_titles()
        return len(titles)