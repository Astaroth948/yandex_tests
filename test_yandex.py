from pages.ya_main import YandexMain
import time
import allure


class TestYandex():

    @allure.story("Тестирование главной страницы Yandex")
    @allure.title("Проверка количества новостных строк")
    def test_quantity_news(self, driver):
        link = "https://www.yandex.ru"
        page = YandexMain(driver, link)
        page.open()
        page.check_quantity_news()
        time.sleep(5)

    @allure.story("Тестирование главной страницы Yandex")
    @allure.title("Проверка наличия определенного заголовка среди новостей")
    def test_title_news_item(self, driver):
        link = "https://www.yandex.ru"
        title = "Россия ввела санкции против ряда граждан Великобритании"
        page = YandexMain(driver, link)
        page.open()
        page.check_title_news_item(title)
        time.sleep(5)
