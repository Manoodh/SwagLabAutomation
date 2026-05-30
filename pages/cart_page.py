from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.checkout_button = "#checkout"

        self.first_name_field = "#first-name"
        self.last_name_field = "#last-name"
        self.postal_code_field = "#postal-code"
        self.continue_checkout_button = "#continue"

        self.finish_checkout_button = "#finish"
        self.order_confirmation_message = ".complete-header" 

    def complete_check_out_flow(self):
        self.click_element(self.checkout_button)

        self.fill_field(self.first_name_field,"A")
        self.fill_field(self.last_name_field,"A")
        self.fill_field(self.postal_code_field,"4444")

        self.click_element(self.continue_checkout_button)
        self.click_element(self.finish_checkout_button)

    def get_confirmation_message(self)->str:
        return self.get_text(self.order_confirmation_message)
        