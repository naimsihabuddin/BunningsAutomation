from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from pageObjects.HeaderBar import HeaderBar
from pageObjects.SearchResultPage import SearchResultPage
from selenium.common.exceptions import NoSuchElementException


class Test03RecentSearch:
    baseURL = ReadConfig.get_application_url()
    search_data = "scalex"

    logger = LogGeneration.log_generation()

    def test_recent_search(self, setup):
        try:
            self.logger.info("* TEST 01 | Search - Results")
            self.logger.info("** SUMMARY: Verifying Search Result is displayed after performing search")

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
                self.logger.warning("** Search Result text is not displayed")

            products = self.srp.get_products_str()
            if self.search_data.lower() in products:
                assert True
                self.logger.info("** Products are displayed as expected")
                self.logger.info(f"*** ACTUAL RESULT = [{products}]")
            else:
                self.logger.error("** Products are NOT displayed as expected")
                self.logger.info(f"*** ACTUAL RESULT = [{products}]")
                assert False

        except NoSuchElementException as e:
            self.driver.save_screenshot("./Screenshots/" + "test_01_element_not_found.png")
            self.logger.error(f"ERROR: {e}")
            assert False

        finally:
            self.driver.close()
            self.driver.quit()
