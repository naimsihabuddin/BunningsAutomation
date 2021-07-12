import time
from selenium.webdriver.common.keys import Keys


class HeaderBar:
    textbox_search_name = "q"
    link_bunnings_home_xpath = ".//a[@data-locator='logo-Bunnings']"
    text_recent_searches_xpath = ".//p[@data-locator='Recent searches']"
    link_recent_search_xpath = ".//span[@data-locator='recentSearches-0']"

    def __init__(self, driver):
        self.driver = driver

    def set_search_text(self, search_data):
        self.driver.find_element_by_name(self.textbox_search_name).clear()
        self.driver.find_element_by_name(self.textbox_search_name).send_keys(search_data)
        self.driver.find_element_by_name(self.textbox_search_name).send_keys(Keys.ENTER)
        time.sleep(3)

    def click_bunnings_home(self):
        self.driver.find_element_by_xpath(self.link_bunnings_home_xpath).click()
        time.sleep(3)

    def click_search_box(self):
        self.driver.find_element_by_name(self.textbox_search_name).click()
        time.sleep(1)

    def get_recent_search_text(self):
        return self.driver.find_element_by_xpath(self.link_recent_search_xpath).text
