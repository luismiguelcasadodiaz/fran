from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up WebDriver (replace with your preferred browser)
driver = webdriver.Chrome()

# Navigate to the page
driver.get("https://www.expowest.com/en/exhibitor-list/2025-Exhibitor-List.html")

# Scroll down to potentially load more content
# (You might need to adjust the scrolling behavior based on the website's loading mechanism)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.infinite-scroll-component__outerdiv")))  # Adjust selector as needed

# Get the HTML content
html_content = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Now you can search for the element using CSS selectors
infinite_scroll_div = soup.find('div', class_='infinite-scroll-component__outerdiv')

# Check if the element is found
if infinite_scroll_div:
    print(infinite_scroll_div)
else:
    print("Element not found")

# Close the browser
driver.quit()