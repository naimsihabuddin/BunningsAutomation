from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from pageObjects.HeaderBar import HeaderBar
from pageObjects.SearchResultPage import SearchResultPage
from selenium.common.exceptions import NoSuchElementException


class Test02SearchNoResults:
    baseURL = ReadConfig.get_application_url()
    search_data = "asdfghjkl"

    logger = LogGeneration.log_generation()

    def test_search_no_results(self, setup):
        try:
            self.logger.info("* TEST 02 | Search - No Results")
            self.logger.info("** SUMMARY: Verifying no search results when searching for unavailable products")

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
            if total_results_text == "We found 0 results for":
                assert True
                self.logger.info("** No Search Results text is displayed as expected")
                self.logger.info(f"*** ACTUAL RESULT = [{total_results_text}]")
            else:
                self.driver.save_screenshot("./Screenshots/" + "test_02_no_search_defect.png")
                self.logger.error(f"** No Search Results text is NOT displayed as expected")
                assert False

        except NoSuchElementException as e:
            self.driver.save_screenshot("./Screenshots/" + "test_02_element_not_found.png")
            self.logger.error(f"ERROR: {e}")
            assert False

        finally:
            self.driver.close()
            self.driver.quit()
