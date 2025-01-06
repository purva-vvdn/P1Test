import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup for Selenium WebDriver
@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service("path/to/chromedriver")  # Update with the correct path to ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)  # Implicit wait for elements
    yield driver
    driver.quit()

# Test case: Verify login functionality
def test_login(browser):
    browser.get("https://www.amazon.com")
    browser.find_element(By.ID, "nav-link-accountList").click()  # Click 'Sign In'
    browser.find_element(By.ID, "ap_email").send_keys("test_user@example.com")  # Enter email
    browser.find_element(By.ID, "continue").click()
    browser.find_element(By.ID, "ap_password").send_keys("test_password")  # Enter password
    browser.find_element(By.ID, "signInSubmit").click()
    
    # Verify login by checking if the user's name is displayed
    assert "Hello, Test" in browser.page_source, "Login failed or incorrect username displayed."

# Test case: Verify search functionality
def test_search(browser):
    browser.get("https://www.amazon.com")
    search_box = browser.find_element(By.ID, "twotabsearchtextbox")  # Locate search box
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)  # Perform search

    # Verify that results are displayed
    results = browser.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
    assert len(results) > 0, "No search results found."

# Test case: Verify add to cart functionality
def test_add_to_cart(browser):
    browser.get("https://www.amazon.com")
    search_box = browser.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    # Click the first search result
    first_product = browser.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")[0]
    first_product.click()

    # Add to cart
    add_to_cart_button = browser.find_element(By.ID, "add-to-cart-button")
    add_to_cart_button.click()

    # Verify the cart by checking confirmation message
    assert "Added to Cart" in browser.page_source, "Product was not added to the cart."

