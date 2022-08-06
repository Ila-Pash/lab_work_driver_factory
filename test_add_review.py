import unittest

from pageobject.product_page import ProductPage
from webdriver_factory import WebDriverFactory


class AddReviewTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.driver = WebDriverFactory.get_driver()

    def tearDown(self) -> None:
        """Действия после теста"""
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_ReviewPageTest(self):
        # Аллоцируем page obj для страницы review
        # Передаем объекту в конструкторе ссылку на Selenium WebDriver
        product_page = ProductPage(self.driver, 42)

        product_page.open()

        # открытие вкладки review
        product_page.open_review_tab()
        # сравнение текста предупреждения
        # передаём в continue_button текст после клика
        expected_warning_text = 'Warning: Please select a review rating!'

        # клик continue не заполняя поле
        product_page.continue_button_click(expected_warning_text)

        # ожидаем конкретный текст в предупреждении
        warning_text = product_page.get_alert_text(expected_warning_text)
        self.assertEqual(expected_warning_text, warning_text)

        # оценить
        rating: str = '2'
        product_page.set_rating(rating)

        # ввести имя
        your_name: str = 'John'
        product_page.enter_name(your_name)

        # ввести отзыв
        your_review: str = 'вавыалвоыраловыравлоарвы'
        product_page.enter_review(your_review)

        # сравнение текста предупреждения
        expected_warning_text = 'Warning: Review Text must be between 25 and 1000 characters!'

        # клик continue
        product_page.continue_button_click(expected_warning_text)

        # ожидаем конкретный текст в предупреждении
        warning_text = product_page.get_alert_text(expected_warning_text)
        self.assertEqual(expected_warning_text, warning_text)

        # ввести отзыв
        your_review: str = 'вавыалвоыраловыравлоарвы123'
        product_page.enter_review(your_review)

        # сравнение текста предупреждения
        expected_warning_text = 'Thank you for your review. It has been submitted to the webmaster for approval.'

        # клик continue
        product_page.continue_button_click(expected_warning_text)

        # ожидаем конкретный текст в предупреждении
        warning_text = product_page.get_alert_text(expected_warning_text)
        self.assertEqual(expected_warning_text, warning_text)
