from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import title_is, text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.base_page import BasePage


class ComparePage(BasePage):

    def get_url(self) -> str:
        return f'{self.base_url}/index.php?route=product/compare'

    def get_compare_result(self) -> list[str]:
        """поиск рез-ов сравнения"""
        results: list[WebElement] = self.driver.find_elements(By.CSS_SELECTOR, 'tbody strong')
        # созадние пустого списка в котором будут накапливаться рез-ты
        product_results: list[str] = []
        for result in results:
            # можно сразу брать текст от рез-та селектора
            # добавление в пустой список рез-ов
            product_results.append(result.text)
        return product_results

    def get_remove_buttons(self) -> list[WebElement]:
        """поиск кнопок удаления"""

        # в данном случае необходим клик (удаление одного продукта) по одному из эл-ов для этого можно задать массив эл-ов и кликнуть по
        # первому эл-ту из этого массива (никакие циклы в этом случае не нужны)
        remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.table-bordered tbody td > .btn-danger')
        return remove_buttons

    def remove_product(self, alert_text: str) -> None:
        """удаление первого эл-та"""
        remove_button: list[WebElement] = self.get_remove_buttons()
        remove_button[0].click()
        self.alert_is_present(alert_text)

    def get_info(self) -> WebElement:
        """поиск информационного текста"""
        info = self.driver.find_element(By.CSS_SELECTOR, '#content > p')
        return info

    def get_info_text(self) -> str:
        """получение содержимого текста"""
        info = self.get_info()
        return info.text

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
