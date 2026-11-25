from playwright.sync_api import Page
from pages.search_page import SearchPage
from config_reader import ConfigReader
import pytest


@pytest.mark.parametrize("query, n, sort_type", [
    ("city", 10, "price_asc"),
    ("city", 15, "price_desc"),
    ("habits", 10, "price_asc"),
    ("habits", 15, "price_desc")
])

def test_price_sorting(page: Page, query, n, sort_type):
    search_page = SearchPage(page)
    settings = ConfigReader()
    descending = sort_type == "price_desc"
    url = settings.config["base_url"]
    page.goto(url)
    search_page.search_articles(query)

    total = search_page.get_total_prices_count()
    all_prices = search_page.get_first_n_prices(total)
    expected_prices = sorted(all_prices, reverse=descending)[:n]

    search_page.set_sort(sort_type)
    search_page.wait_sorted_prices(n, expected_prices)

    actual_prices = search_page.get_first_n_prices(n)

    assert actual_prices == expected_prices, (
        f"Expected: '{expected_prices}', "
        f"Actual: '{actual_prices}'"
    )