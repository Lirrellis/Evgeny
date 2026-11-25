from playwright.sync_api import Page, expect

class SearchPage:
    def __init__(self, page: Page):
        self.page = page

    def search_articles(self, query: str):
        self.page.get_by_test_id("search-input").fill(query)
        self.page.get_by_test_id("search-button").click()

        count = self.page.get_by_test_id("search-summary-count")
        expected_count = int(count.inner_text())
        prices = self.page.locator('[data-testid^="search-result-price-"]')
        expect(prices).to_have_count(expected_count)


    def set_sort(self, sort_type: str):
        with self.page.expect_response(
                lambda response: "/search/results" in response.url
                and f"sort={sort_type}" in response.url
                and response.status == 200):
            self.page.get_by_test_id("filter-sort").select_option(sort_type)

    def get_first_n_prices(self, n: int):
        prices = self.page.locator('[data-testid^="search-result-price-"]')
        result_prices = []
        for i in range(n):
            cost = int(prices.nth(i).get_attribute("data-price"))
            result_prices.append(cost)
        return result_prices

    def wait_sorted_prices(self, n: int, expected_prices: list[int]):
        prices = self.page.locator('[data-testid^="search-result-price-"]')
        for i in range(n):
            expect(prices.nth(i)).to_have_attribute("data-price", str(expected_prices[i]))

    def get_total_prices_count(self):
        prices = self.page.locator('[data-testid^="search-result-price-"]')
        total_prices = prices.count()
        return total_prices