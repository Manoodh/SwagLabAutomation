import pytest
from playwright.sync_api import sync_playwright
# Import your centralized configurations
from config.settings import TestConfig

@pytest.fixture(scope="function")
def browser_page():
    """
    Setup and Teardown Engine for Playwright Browser Contexts.
    This runs automatically before and after each individual test function.
    """
    # 1. SETUP: Start the Playwright driver manager
    with sync_playwright() as p:
        
        # 2. Launch the physical browser using parameters from your settings file
        browser = p.chromium.launch(
            headless=TestConfig.HEADLESS_MODE, 
            slow_mo=TestConfig.SLOW_MO_DELAY
        )
        
        # 3. Open a completely isolated, clean browser tab instance
        context = browser.new_context()
        page = context.new_page()
        
        # Set the safety timing threshold
        page.set_default_timeout(TestConfig.DEFAULT_TIMEOUT)
        
        print("\n[SETUP] Browser context successfully spawned. Handing over to test...")
        
        # 4. YIELD: This pauses execution right here and hands the 'page' variable
        # directly over to whatever test function requested it.
        yield page
        
        # 5. TEARDOWN: Once the test function completes its assertions, control 
        # snaps back right here to clean up memory.
        print("\n[TEARDOWN] Test execution complete. Destroying browser session...")
        context.close()
        browser.close()