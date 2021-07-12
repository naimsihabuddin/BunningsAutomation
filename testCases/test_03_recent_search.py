from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from pageObjects.HeaderBar import HeaderBar
from pageObjects.SearchResultPage import SearchResultPage
from selenium.common.exceptions import NoSuchElementException


class Test03RecentSearch:
    baseURL = ReadConfig.get_application_url()
    search_data = "helicopter"

    logger = LogGeneration.log_generation()

    def test_recent_search(self, setup):
        try:
            self.logger.info("* TEST 03 | Recent Search")
            self.logger.info("** SUMMARY: Verifying Recent Search functionality after performing search")

            self.driver = setup
            self.driver.get(self.baseURL)
            self.hb = HeaderBar(self.driver)
            self.hb.set_search_text(self.search_data)
            actual_title = self.driver.title
            if actual_title == "Search results - Bunnings Australia":
                self.logger.info("** Browser title is as expected")
            else:
                self.logger.warning("** Browser title is NOT as expected")
                self.logger.warning(f"*** ACTUAL RESULT = [{actual_title}]")

            self.srp = SearchResultPage(self.driver)
            total_results_text = self.srp.get_total_results_text()
            if total_results_text != "":
                self.logger.info("** Search Result text is displayed as expected")
                self.logger.info(f"*** ACTUAL RESULT = [{total_results_text}]")
            else:
                self.logger.warning(f"** Search Result text is not displayed")

            self.hb.click_bunnings_home()
            self.hb.click_search_box()
            recent_search_text = self.hb.get_recent_search_text()
            if recent_search_text == self.search_data:
                assert True
                self.logger.info("** Recent Search is displayed as expected")
                self.logger.info(f"*** ACTUAL RESULT = [{recent_search_text}]")
            else:
                self.driver.save_screenshot("./Screenshots/" + "test_03_recent_search_defect.png")
                self.logger.error(f"** Recent Search text is not displayed")
                self.logger.error(f"*** ACTUAL RESULT = [{recent_search_text}]")
                assert False

        except NoSuchElementException as e:
            self.driver.save_screenshot("./Screenshots/" + "test_03_element_not_found.png")
            self.logger.error(f"ERROR: {e}")
            assert False

        finally:
            self.driver.close()
            self.driver.quit()
