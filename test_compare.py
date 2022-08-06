import unittest

from pageobject.compare_page import ComparePage
from pageobject.product_page import ProductPage
from webdriver_factory import WebDriverFactory


class CompareTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.driver = WebDriverFactory.get_driver()

    def tearDown(self) -> None:
        """Действия после теста"""
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_ComparePageTest(self):
        # Аллоцируем page obj для страницы review
        # Передаем объекту в конструкторе ссылку на Selenium WebDriver

        # 42 это prod_id
        product_page = ProductPage(self.driver, 42)

        # открытие страницы
        product_page.open()

        # сравнение текста уведомления
        expected_alert_text = 'Success: You have added Apple Cinema 30" to your product comparison!'

        product_page.add_to_compare(expected_alert_text)

        # ожидаем конкретный текст в предупреждении
        alert_text = product_page.get_alert_text(expected_alert_text)
        self.assertEqual(expected_alert_text, alert_text)

        # 33 это prod_id
        product_page = ProductPage(self.driver, 33)

        # открытие страницы
        product_page.open()

        # сравнение текста уведомления
        expected_alert_text = 'Success: You have added Samsung SyncMaster 941BW to your product comparison!'

        product_page.add_to_compare(expected_alert_text)

        # переход по ссылке “product comparison”
        product_page.compare()

        # Аллоцируем page obj для страницы review
        # Передаем объекту в конструкторе ссылку на Selenium WebDriver
        compare_page = ComparePage(self.driver)

        compare_page.open()

        # ожидаемый рез-т сравнения продуктов
        expected_compare_result: list[str] = ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']

        # сравнение продуктов
        compare_result = compare_page.get_compare_result()
        self.assertEqual(compare_result, expected_compare_result)

        # сравнение текста уведомления
        expected_alert_text = 'Success: You have modified your product comparison!'

        compare_page.remove_product(expected_alert_text)

        # ожидаем конкретный текст в предупреждении
        alert_text = compare_page.get_alert_text(expected_alert_text)
        self.assertEqual(expected_alert_text, alert_text)

        compare_page.remove_product(expected_alert_text)

        # ожидаем конкретный текст в предупреждении
        alert_text = compare_page.get_alert_text(expected_alert_text)
        self.assertEqual(expected_alert_text, alert_text)

        expected_info_text = 'You have not chosen any products to compare.'
        info_text = compare_page.get_info_text()
        self.assertEqual(expected_info_text, info_text)
