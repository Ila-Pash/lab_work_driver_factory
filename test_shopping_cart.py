import unittest

from pageobject.product_page import ProductPage
from pageobject.shop_cart_page import ShopCartPage
from webdriver_factory import WebDriverFactory


class ShoppingCartTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.driver = WebDriverFactory.get_driver()

    def tearDown(self) -> None:
        """Действия после теста"""
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_ShoppingCartTes(self):
        # Аллоцируем page obj для страницы review. Передаем объекту в конструкторе ссылку на Selenium WebDriver
        # 33 это prod_id
        product_page = ProductPage(self.driver, 33)

        # открытие страницы товара_1
        product_page.open()

        qty: int = 2

        # очистка поля qty
        product_page.clear_qty()

        # заполнение поля qty
        product_page.enter_qty(qty)

        # сравнение текста уведомления
        expected_alert_text = 'Success: You have added Samsung SyncMaster 941BW to your shopping cart!'

        # положить в корзину
        product_page.click_add_button(expected_alert_text)

        # ожидаем конкретный текст в уведомлении
        alert_text = product_page.get_alert_text(expected_alert_text)
        self.assertEqual(expected_alert_text, alert_text)

        # 47 это prod_id
        product_page = ProductPage(self.driver, 47)

        # открытие страницы товара_2
        product_page.open()

        # сравнение текста уведомления
        expected_alert_text = 'Success: You have added HP LP3065 to your shopping cart!'

        # положить в корзину
        product_page.click_add_button(expected_alert_text)

        # ожидаем конкретный текст в уведомлении
        alert_text = product_page.get_alert_text(expected_alert_text)
        self.assertEqual(expected_alert_text, alert_text)

        # Аллоцируем page obj для страницы корзина
        shopcart_page = ShopCartPage(self.driver)

        shopcart_page.open()

        # подсчёт кол-ва товаров в корзине
        expected_count: int = 2
        count = shopcart_page.get_product_count()
        self.assertEqual(expected_count, count)

        # проверка названия продуктов, имеющихся в корзине
        expected_names = ['Samsung SyncMaster 941BW', 'HP LP3065']
        product_names = shopcart_page.get_product_names()
        self.assertEqual(expected_names, product_names)

        # проверка итоговой стоимости
        expected_total_price: str = '$606.00'
        total_price = shopcart_page.total_price()
        self.assertEqual(expected_total_price, total_price)

        # удаление продукта из корзины
        product_to_remove: str = 'Samsung SyncMaster 941BW'
        shopcart_page.remove_product(product_to_remove)

        # подсчёт кол-ва товаров в корзине
        expected_count: int = 1
        count = shopcart_page.get_product_count()
        self.assertEqual(expected_count, count)

        # проверка названия продуктов, имеющихся в корзине
        expected_names = ['HP LP3065']
        product_names = shopcart_page.get_product_names()
        self.assertEqual(expected_names, product_names)

        # удаление продукта из корзины
        product_to_remove: str = 'HP LP3065'
        shopcart_page.remove_product(product_to_remove)

        # сравнение уведомления
        expected_allert: str = 'Your shopping cart is empty!'
        alert = shopcart_page.get_alert_text()
        self.assertEqual(expected_allert, alert)
