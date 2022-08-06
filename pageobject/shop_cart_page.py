from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, any_of, \
    invisibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.base_page import BasePage


class ShopCartPage(BasePage):

    def get_url(self) -> str:
        return f'{self.base_url}/index.php?route=checkout/cart'

    def get_products(self) -> list[WebElement]:
        """поиск строк в гриде с продуктами"""
        products = self.driver.find_elements(By.CSS_SELECTOR, '.table-responsive tbody > tr')
        return products

    def get_product_count(self) -> int:
        """получить кол-во продуктов (строк) в корзине"""
        products = self.get_products()
        count = len(products)
        return count

    def get_products_link(self) -> list[WebElement]:
        """получение ссылок на продукты в корзине"""
        products_link = self.driver.find_elements(By.CSS_SELECTOR, '.table-responsive tbody > tr > td:nth-child(2) > a')
        return products_link

    def get_product_names(self) -> list[str]:
        """получение имен продуктов в корзине"""
        product_names: list[WebElement] = self.get_products_link()
        result_names = []
        # пустой массив для сохранения рез-ов
        for p in product_names:
            result_names.append(p.text)
            # добавить в пустой массив текст каждого эл-та из product_names
        return result_names

    def get_total_price_field(self) -> WebElement:
        """поиск total_price"""
        total: list[WebElement] = self.driver.find_elements(By.CSS_SELECTOR, '.table-bordered > tbody')
        list_elem: list[WebElement] = total[-1].find_elements(By.CSS_SELECTOR, 'tr > td')
        price = list_elem[-1]
        return price

    def total_price(self) -> str:
        """получение значения total_price"""
        total_price = self.get_total_price_field()
        return total_price.text

    def get_remove_buttons(self) -> list[WebElement]:
        """поиск кнопок удаления"""
        remove_buttons: list[WebElement] = self.driver.find_elements(By.CSS_SELECTOR, '.input-group-btn > .btn-danger')
        return remove_buttons

    def remove_product(self, product_name: str) -> None:
        """удаление продукта из корзины"""

        # получить названия продуктов в корзине
        product_names = self.get_product_names()
        remove_product = self.get_remove_buttons()
        # получить индекс товара из массива
        product_index_to_remove = product_names.index(product_name)
        # удалить товар по индексу
        remove_product[product_index_to_remove].click()
        # дождаться удаления продукта
        self.wait_for_product_is_deleted(product_name)

    def wait_for_product_is_deleted(self, product_name: str) -> bool:
        """ожидание, что продукт отсутсвует в корзине"""
        WebDriverWait(self.driver, timeout=10).until(
            any_of(invisibility_of_element_located((By.LINK_TEXT, product_name)),
                   invisibility_of_element_located((By.CSS_SELECTOR, '.table-responsive tbody > tr'))))
        return True

    def get_alert(self) -> WebElement:
        alert: WebElement = self.driver.find_element(By.CSS_SELECTOR, '#content > p')
        return alert

    def get_alert_text(self) -> str:
        alert: WebElement = self.get_alert()
        return alert.text.split('\n')[0]
