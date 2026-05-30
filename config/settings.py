class TestConfig:
    
    BASE_URL = "https://www.saucedemo.com"
    
    # Global framework timing constraints (in milliseconds)
    DEFAULT_TIMEOUT = 10000 
    
    # Authentic static credentials accepted natively by SauceDemo
    TEST_USER = "standard_user"
    TEST_PASSWORD = "secret_sauce"
    
    # Interactive browser execution mechanics
    HEADLESS_MODE = True 
    SLOW_MO_DELAY = 200  # Slight delay so you can watch your page actions execute