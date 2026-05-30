# Import page object interface layer
from pages.saucedemo import SauceDemoPage
# Import hardcoded static credentials module
from config.settings import TestConfig

def test_saucedemo_authentication_and_catalog(browser_page):
    
    sauce_store = SauceDemoPage(browser_page)
    
    print("\n[TEST] Commencing workflow automation...")
    
    sauce_store.navigate_to(TestConfig.BASE_URL)
    
    sauce_store.login_to_application(TestConfig.TEST_USER, TestConfig.TEST_PASSWORD)
    
    print("[TEST] Form submitted. Extracting dashboard catalog properties...")
    
    actual_product_title = sauce_store.get_dashboard_product_title()
    
    expected_product_title = "Sauce Labs Backpack"
    
    assert actual_product_title == expected_product_title, \
        f"QA Defect Detected: Expected item '{expected_product_title}' but found '{actual_product_title}'"
        

    assert sauce_store.logout_of_application() == TestConfig.BASE_URL, \
        "QA Defect Detected: Logout did not return to the expected landing page URL."