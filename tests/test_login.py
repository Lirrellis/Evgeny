from playwright.sync_api import Page, expect
from faker import Faker



def test_invalid_login_and_error(page: Page, web_url: str):
    fake = Faker()
    page.goto(f"{web_url}/")

    page.get_by_test_id("nav-login").click()
    expect(page).to_have_url(f"{web_url}/login")

    expect(page.get_by_test_id("login-title")).to_have_text("Authorization")


    page.get_by_test_id("login-username").fill(fake.user_name())
    page.get_by_test_id("login-password").fill(fake.password())
    page.get_by_test_id("login-submit").click()

    spinner = page.get_by_test_id("login-submit-spinner")
    expect(spinner).to_be_visible()
    expect(spinner).to_be_hidden()


    error_text = page.get_by_test_id("login-error-inline")
    expect(error_text).to_be_visible()
    expect(error_text).not_to_be_empty()
    actual_error_text = error_text.inner_text()
    expected_error_text = "Invalid login or password."

    assert actual_error_text == expected_error_text, (
        f"Expected: '{expected_error_text}', "
        f"Actual: '{actual_error_text}'"
    )