# Import your BasePage class so we can inherit from it
from pages.base_page import BasePage

class SauceDemoPage(BasePage):
    def __init__(self, page):
        """
        Constructor. 
        Passes the browser page up to the parent BasePage, 
        and defines the specific UI elements for SauceDemo.
        """
        # Super initializes the parent BasePage class
        super().__init__(page)
        
        # --- UI LOCATORS ---
        self.username_field = "#user-name"
        self.password_field = "#password"
        self.login_button = "#login-button"

        self.hamburger_menu_button = "#react-burger-menu-btn"
        self.logout_button = "text=Logout"
        
        # This is the title text of the first product displayed on the dashboard after logging in
        self.first_product_title = ".inventory_item_name"

        # Login error
        self.login_error = "h3[data-test='error']"

    
    def login_to_application(self, username: str, password: str):
        """
        Combines our base actions to execute a complete login transaction.
        """
        # We call the methods we wrote in BasePage using self.method_name
        self.fill_field(self.username_field, username)
        self.fill_field(self.password_field, password)
        self.click_element(self.login_button)

    def get_dashboard_product_title(self) -> str:
        """
        Extracts the name of the first available item on the store page 
        to prove we logged in successfully.
        """
        return self.get_text(self.first_product_title)
    
    def logout_of_application(self) -> str:
        self.click_element(self.hamburger_menu_button)
        self.click_element(self.logout_button)
        return self.page.url.rstrip("/")  # Return the current URL to verify we logged out successfully
    
    def login_with_invalid_credentials(self) -> str:
        """
        Attempts to log in with invalid credentials and returns the error message text.
        """
        self.fill_field(self.username_field, "username")
        self.fill_field(self.password_field, "password")
        self.click_element(self.login_button)
        return self.get_text(self.login_error)