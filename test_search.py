import unittest

from pageobject.search_page import SearchPage
from webdriver_factory import WebDriverFactory


class SearchPageTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.driver = WebDriverFactory.get_driver()

    def tearDown(self) -> None:
        """Действия после теста"""
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_SearchPageTest(self):

        # Аллоцируем page obj для страницы Поиска
        # Передаем объекту в конструкторе ссылку на Selenium WebDriver
        search_page = SearchPage(self.driver)

        search_page.open()

        # объявление переменной - продукта для поиска
        product: str = 'apple'

        # ввод в поле поиска "apple"
        search_page.enter_product(product)

        # поиск + провкерка того, что после поиска заголовок страницы содержит "Search - apple"
        search_page.search(product)

        # проверка соответствия имени товара
        name_1: str = search_page.get_product_name()
        self.assertEqual('Apple Cinema 30"', name_1)

        # проверка соответствия цены товара
        price_1: str = search_page.get_product_price()
        self.assertEqual('$110.00', price_1)

        # очистить поле поиска
        search_page.clear_product()

        # переприсваивание переменной - продукта для поиска
        product = 'sony'

        # ввод в поле поиска "sony"
        search_page.enter_product(product)

        # поиск + провкерка того, что после поиска заголовок страницы содержит "Search - sony"
        search_page.search(product)

        # проверка соответствия имени товара
        name_2: str = search_page.get_product_name()
        self.assertEqual('Sony VAIO', name_2)

        # проверка соответствия цены товара
        price_2: str = search_page.get_product_price()
        self.assertEqual('$1,202.00', price_2)

        # очистить поле поиска
        search_page.clear_product()

        # переприсваивание переменной - продукта для поиска
        product = 'nokia'

        # ввод в поле поиска "sony"
        search_page.enter_product(product)

        # поиск + проверка того, что после поиска заголовок страницы содержит "Search - nokia"
        search_page.search(product)

        # проверка отсутствующего товара
        result: str = search_page.get_message()
        self.assertTrue('There is no product that matches the search criteria.' in result)

        # очистить поле "search criteria"
        search_page.clear_search_criteria()

        # задать критерий поиска
        criteria = 'stunning'

        # ввод в поле search_criteria значения "stunning"
        search_page.enter_search_criteria(criteria)

        # выбор опции “Search in productdescriptions”
        search_page.check_box()

        # поиск_2 + проверка того, что после поиска заголовок страницы содержит "Search - stunning", но в параметре уже переменная "criteria"
        search_page.click_bottom_search_button(criteria)

        results: list[str] = search_page.get_results()
        self.assertEqual(['HP LP3065', 'iMac'], results)

