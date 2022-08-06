import os

from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    """Базовый (родительский) класс PageObject,
    который содержит общие для всех страниц методы."""

    def __init__(self, driver: WebDriver):
        # http://54.183.112.233 берем из переменной окружения
        self.base_url: str = os.getenv('BASE_URL')
        self.driver = driver

    def get_url(self) -> str:
        # Обязательно реализовать в дочерних классах.
        raise NotImplementedError

    def open(self):
        """Открыть страницу account."""
        self.driver.get(self.get_url())

    def save_screenshot(self):
        pass
