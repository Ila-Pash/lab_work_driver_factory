import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver: WebDriver, prod_id: int):
        # вводим новый парам-тр, котор не нужен BasePage
        # super - это обращение к род.классу класса ComparePage
        # вызов констр-ра BasePage
        super(ProductPage, self).__init__(driver)
        # сохраняем в памяти параметр, чтоб далее работаь с этим парм-ром
        self.prod_id = prod_id

    def get_url(self) -> str:
        return f'{self.base_url}/index.php?route=product/product&product_id={self.prod_id}'

    def get_name(self) -> str:
        """получение наименования продукта"""
        name_field = self.driver.find_element(By.TAG_NAME, 'h1')
        return name_field.text

    def get_brand(self) -> str:
        """получение бренда продукта"""
        brand_field = self.driver.find_element(By.LINK_TEXT, 'Apple')
        return brand_field.text

    def get_product_code(self) -> str:
        product_code_field = self.driver.find_element(By.CSS_SELECTOR, '#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(3) > li:nth-child(2)')
        return product_code_field.text

    def get_price(self) -> str:
        """получение цены продукта"""
        price_field = self.driver.find_element(By.CSS_SELECTOR, 'li > h2')
        return price_field.text

    def get_description(self) -> str:
        """получение описания продукта"""
        description_field = self.driver.find_element(By.ID, 'tab-description')
        return description_field.text

    def get_review_tab(self) -> WebElement:
        """поиск вкладки review"""
        review_tab = self.driver.find_element(By.CSS_SELECTOR, '.nav-tabs a[href="#tab-review"]')
        return review_tab

    def get_compare_button(self) -> WebElement:
        """поиск кнопки Compare this Product"""
        compare_button = self.driver.find_element(By.CSS_SELECTOR, '.col-sm-4 button[data-original-title="Compare this Product"]')
        return compare_button

    def add_to_compare(self, alert_text: str) -> None:
        """клик по кнопке Compare this Product"""
        compare_button = self.get_compare_button()
        compare_button.click()
        self.alert_is_present(alert_text)

    def alert_is_present(self, text: str) -> bool:
        WebDriverWait(self.driver, timeout=10).until(text_to_be_present_in_element((By.CLASS_NAME, 'alert-dismissible'), text))
        return True

    def get_alert(self, text: str) -> WebElement:
        """поиск уведомления"""
        alert = self.driver.find_element(By.CLASS_NAME, 'alert-dismissible')
        return alert

    def get_alert_text(self, text: str) -> str:
        """получение текста уведомления"""
        alert = self.get_alert(text)
        return alert.text.split("\n")[0]

    def comparison_link_is_present(self) -> bool:
        WebDriverWait(self.driver, timeout=10).until(
            visibility_of_element_located((By.LINK_TEXT, 'product comparison')))
        return True

    def get_link(self) -> WebElement:
        """поиск ссылки “product comparison” """
        self.comparison_link_is_present()
        link = self.driver.find_element(By.LINK_TEXT, 'product comparison')
        return link

    def compare(self) -> None:
        """переход по ссылке “product comparison” """
        link = self.get_link()
        link.click()

    def open_review_tab(self) -> None:
        """открыть вкалдку review"""
        review_tab = self.get_review_tab()
        review_tab.click()
        self.continue_button_is_present()

    def continue_button_is_present(self) -> bool:
        """ожидание сущ-я кнопки continue"""
        WebDriverWait(self.driver, timeout=10).until(visibility_of_element_located((By.ID, 'button-review')))
        return True

    def get_continue_button(self) -> WebElement:
        """поиск кнопки continue"""
        continue_button = self.driver.find_element(By.ID, 'button-review')
        return continue_button

    def continue_button_click(self, alert_text: str) -> None:
        """нажатие кнопки continue"""
        continue_button = self.get_continue_button()
        continue_button.click()
        self.alert_is_present(alert_text)

    def get_rating_button(self, value: str) -> WebElement:
        """поиск кнопки рейтинга по выбранному значению"""
        rating_button = self.driver.find_element(By.CSS_SELECTOR, f'input[value = "{value}"]')
        return rating_button

    def set_rating(self, rating: str) -> None:
        """выбор оценки"""
        rating_button = self.get_rating_button(rating)
        rating_button.click()

    def get_your_name_field(self) -> WebElement:
        """поиск поля your_name"""
        your_name_field = self.driver.find_element(By.ID, 'input-name')
        return your_name_field

    def enter_name(self, name: str) -> None:
        """ввод имени с параметром"""
        name_field = self.get_your_name_field()
        name_field.send_keys(name)

    def get_your_review_field(self) -> WebElement:
        """поиск поля your_review"""
        your_review_field = self.driver.find_element(By.ID, 'input-review')
        return your_review_field

    def enter_review(self, review: str) -> None:
        """ввод отзыва с параметром"""
        review_field = self.get_your_review_field()
        review_field.send_keys(review)

    def get_qty_field(self) -> WebElement:
        """поиск поля qty """
        qty_field = self.driver.find_element(By.ID, 'input-quantity')
        return qty_field

    def clear_qty(self) -> None:
        """очистка поля qty """
        qty = self.get_qty_field()
        qty.clear()

    def enter_qty(self, numer: int) -> None:
        """заполнение поля qty """
        qty = self.get_qty_field()
        qty.send_keys(numer)

    def get_add_button(self) -> WebElement:
        """поиск кнопки add to cart """
        add_button = self.driver.find_element(By.ID, 'button-cart')
        return add_button

    def click_add_button(self, alert_text: str) -> None:
        add_button = self.get_add_button()
        add_button.click()
        self.alert_is_present(alert_text)


