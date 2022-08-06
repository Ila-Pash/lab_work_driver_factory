import unittest

from pageobject.product_page import ProductPage
from webdriver_factory import WebDriverFactory


class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.driver = WebDriverFactory.get_driver()

    def tearDown(self) -> None:
        """Действия после теста"""
        self.driver.close()

    def test_find_info(self):
        product_page = ProductPage(self.driver, 42)

        product_page.open()

        name = product_page.get_name()
        self.assertEqual('Apple Cinema 30"', name)

        brand = product_page.get_brand()
        self.assertEqual('Apple', brand)

        product_code = product_page.get_product_code()
        self.assertEqual('Product Code: Product 15', product_code)

        price = product_page.get_price()
        self.assertEqual('$110.00', price)

        description = product_page.get_description()
        self.assertTrue('The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution' in description)
