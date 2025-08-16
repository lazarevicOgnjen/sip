from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"

# Chrome driver setup
browser_driver = Service('/usr/bin/chromedriver')

# Start the browser
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Step 1: Navigate to the page
    page_to_scrape.get("https://sip.elfak.ni.ac.rs/")

    responseT = page_to_scrape.find_element(By.ID, 'novosti')
    novosti_markdown = responseT.text

    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

finally:
    # Close the browser
    page_to_scrape.quit()
