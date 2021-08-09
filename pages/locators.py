from selenium.webdriver.common.by import By


class YandexMainLocators():
    STATIC_NEWS_STRINGS = (By.XPATH, '//ol[@class="list news__list"]//a')
    DINAMIC_NEWS_STRING = (By.XPATH, '//ol[@class="list news__list news__animation-list"]/li[contains(@class, "list__item_fade_in")]/a')

