from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        """Navigates the active browser tab to any given web address."""
        self.page.goto(url)

    def fill_field(self, selector: str, text: str):
        """
        Finds an input box using its CSS selector, clears it, 
        and types the text into it.
        """
        # 1. Locate the element
        element = self.page.locator(selector)
        
        # 2. Make sure it's visible on screen before typing
        element.wait_for(state="visible")
        
        # 3. Simulate real typing
        element.fill(text)

    def click_element(self, selector: str):
        """
        Finds a button or link using its CSS selector and clicks it.
        """
        element = self.page.locator(selector)
        element.wait_for(state="visible")
        element.click()

    def get_text(self, selector: str) -> str:
        """
        Extracts the visible text inside a specific web element.
        """
        element = self.page.locator(selector).first
        element.wait_for(state="visible")
        return element.inner_text()