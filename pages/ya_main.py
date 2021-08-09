import pytest
from pages.base_page import BasePage
from pages.locators import YandexMainLocators
import allure


class YandexMain(BasePage):

    @allure.step("Проверить, что количество новостных строк = {news_strings}")
    def check_quantity_news(self, news_strings=5):
        news = len(self.find_elements(*YandexMainLocators.STATIC_NEWS_STRINGS))
        news += len(self.find_elements(*YandexMainLocators.DINAMIC_NEWS_STRING))
        if news_strings != news:
            pytest.fail(f"Количество новостей не равно {news_strings}")

    @allure.step("Проверить, что среди новостных строк присутствует заголовок {title}")
    def check_title_news_item(self, title):
        news = self.find_elements(*YandexMainLocators.STATIC_NEWS_STRINGS)
        news += self.find_elements(*YandexMainLocators.DINAMIC_NEWS_STRING)
        title_present = False
        for news_item in news:
            if news_item.get_attribute("aria-label") == title:
                title_present = True
                break
        if title_present == False:
            pytest.fail(f"Нет новости с заголовком '{title}'")
