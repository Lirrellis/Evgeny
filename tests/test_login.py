from playwright.sync_api import Page, expect
import pytest
import uuid

random_username = [
    uuid.uuid4().hex[:8]
    for _ in range(3)
]
random_password = [
    uuid.uuid4().hex[:8]
    for _ in range(3)
]
@pytest.mark.parametrize("username, password", [
    (random_username[0], random_password[0]),
    (random_username[1], random_password[1]),
    (random_username[2], random_password[2]),
])

def test_invalid_login_and_error(page: Page, username: str, password: str, web_url: str):

    page.goto(f"{web_url}/")

    page.get_by_role("link", name="Login").click()
    expect(page).to_have_url(f"{web_url}/login")


    page.get_by_test_id("login-username").fill(username)
    page.get_by_test_id("login-password").fill(password)
    page.get_by_test_id("login-submit").click()

    spinner = page.get_by_test_id("login-submit-spinner")
    expect(spinner).to_be_visible()
    expect(spinner).to_be_hidden(timeout=15000)


    error_text = page.get_by_test_id("login-error-inline")
    expect(error_text).to_be_visible()
    expect(error_text).to_have_text("Invalid login or password.")