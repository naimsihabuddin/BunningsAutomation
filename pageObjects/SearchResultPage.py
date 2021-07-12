class SearchResultPage:
    text_totalresults_class = "totalResults"
    list_product_titles_class = "product-title"

    def __init__(self, driver):
        self.driver = driver

    def get_total_results_text(self):
        return self.driver.find_element_by_class_name(self.text_totalresults_class).text

    def get_products_str(self):
        products = self.driver.find_elements_by_class_name(self.list_product_titles_class)
        product_titles = []
        for product in products:
            product_titles.append(product.text.lower())
        return " ".join(product_titles)
