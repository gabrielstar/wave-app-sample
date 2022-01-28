from playwright.sync_api import Page


def test_sanity(page: Page):
    page.goto("http://localhost:10101")
    page.wait_for_selector("text=Number is: 0")
    page.click("data-test=action_increment")
    page.wait_for_selector("text=Number is: 1")