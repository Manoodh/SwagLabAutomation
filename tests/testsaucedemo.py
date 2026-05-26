# 1. Import your page object interface layer
from pages.saucedemo import SauceDemoPage
# 2. Import your hardcoded static credentials module
from config.settings import TestConfig

def test_saucedemo_authentication_and_catalog(browser_page):
    """
    Scenario: Validate that a standard user can successfully pass 
    authentication and verify that the product inventory displays correctly.
    """
    
    # 3. INITIALIZE: Create the page interface object 
    # We pass the 'browser_page' fixture (the real tab from conftest) into our class
    sauce_store = SauceDemoPage(browser_page)
    
    print("\n[TEST] Commencing workflow automation...")
    
    # 4. ACTION: Navigate to the landing page
    sauce_store.navigate_to(TestConfig.BASE_URL)
    
    # 5. ACTION: Execute login steps using credentials from our configuration file
    sauce_store.login_to_application(TestConfig.TEST_USER, TestConfig.TEST_PASSWORD)
    
    print("[TEST] Form submitted. Extracting dashboard catalog properties...")
    
    # 6. EXTRACT: Read the name of the first product displayed on screen
    actual_product_title = sauce_store.get_dashboard_product_title()
    
    # 7. ASSERT: Verify the application state matches expectations
    # SauceDemo's first default item is always 'Sauce Labs Backpack'
    expected_product_title = "Sauce Labs Backpack"
    
    assert actual_product_title == expected_product_title, \
        f"QA Defect Detected: Expected item '{expected_product_title}' but found '{actual_product_title}'"
        
    print(f"[TEST] Success! Verified matching catalog element: '{actual_product_title}'")