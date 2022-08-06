from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.base_page import BasePage
from utils.price_helper import extract_price


class SearchPage(BasePage):

    def get_url(self) -> str:
        return f'{self.base_url}/index.php?route=product/search'

    def get_product_field(self) -> WebElement:
        """идентификация эл-та "поиск продукта"""
        # единственное место, где задаем как будем искать эл-т
        return self.driver.find_element(By.CSS_SELECTOR, '#search > input')

    def enter_product(self, product: str) -> None:
        """ввода названия продукта"""
        search_field = self.get_product_field()
        search_field.send_keys(product)

    def clear_product(self) -> None:
        """очистка поля ввода названия продукта"""
        search_field = self.get_product_field()
        search_field.clear()

    def get_search_button(self) -> WebElement:
        """идентификация эл-та "кнопка поиска"""
        return self.driver.find_element(By.CLASS_NAME, 'btn-default')

    def search(self,product: str) -> None:
        """клик по кнопке search"""
        search_button = self.get_search_button()
        search_button.click()
        self.title_is_present(product)

    def title_is_present(self, product: str) -> bool:
        """проверка, что страница сущетсвует"""
        WebDriverWait(self.driver, timeout=10).until(title_is('Search - ' + product))
        return True

    def get_product_name_field(self) -> WebElement:
        """поиск поля "имя товара"""
        name_field: WebElement = self.driver.find_element(By.TAG_NAME, 'h4')
        return name_field

    def get_product_name(self) -> str:
        """получение значения из поля "имя товара"""
        product_name_field: WebElement = self.get_product_name_field()
        return product_name_field.text

    def get_product_price_field(self) -> WebElement:
        """поиск поля "цена товара"""
        price_field: WebElement = self.driver.find_element(By.CLASS_NAME, 'price')
        return price_field

    def get_product_price(self) -> str:
        """получение значения из поля "цена товара"""
        product_price_field: WebElement = self.get_product_price_field()
        return extract_price(product_price_field.text)

    def get_message_field(self) -> WebElement:
        """поиск поля сообщения"""
        message_field = self.driver.find_element(By.ID, 'content')
        return message_field

    def get_message(self) -> str:
        """получение текста сообщения"""
        message = self.get_message_field()
        return message.text

    def get_search_criteria_field(self) -> WebElement:
        """поиск поля "search criteria"""
        search_criteria_field = self.driver.find_element(By.ID, 'input-search')
        return search_criteria_field

    def enter_search_criteria(self, criteria: str) -> None:
        """метод для ввода значения в поле search_criteria"""

        # в методе enter_search_criteria принимаем параметр criteria(переменная - продукт для поиска)
        # в переменной search_criteria сохраняем рез-т выполнения метода get_search_criteria_field()
        search_criteria = self.get_search_criteria_field()
        search_criteria.send_keys(criteria)

    def clear_search_criteria(self) -> None:
        """очистка поля "search criteria"""
        search_criteria = self.get_search_criteria_field()
        search_criteria.clear()

    def get_check_box_button(self) -> WebElement:
        """поиск чек-бокса "Search in product descriptions"""
        check_box_button = self.driver.find_element(By.ID, 'description')
        return check_box_button

    def check_box(self) -> None:
        """установка чек-бокса "Search in product descriptions" """
        check_box = self.get_check_box_button()
        check_box.click()

    def get_bottom_search_button(self) -> WebElement:
        """поиск кнопки поиска внизу страницы"""
        bottom_search_button = self.driver.find_element(By.ID, 'button-search')
        return bottom_search_button

    def click_bottom_search_button(self, criteria: str) -> None:
        """клика по кнопке поиска внизу страницы"""
        bottom_search_button = self.get_bottom_search_button()
        bottom_search_button.click()
        self.title_is_present(criteria)

    def get_results(self) -> list[str]:
        """рез-т поиска"""
        results: list[WebElement] = self.driver.find_elements(By.CLASS_NAME, 'product-thumb')
        name_results: list[str] = []
        for result in results:
            name: str = result.find_element(By.TAG_NAME, 'h4').text
            name_results.append(name)
        return name_results
