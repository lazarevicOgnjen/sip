from playwright.sync_api import sync_playwright
import time

# URL za scraping
url = "https://sip.elfak.ni.ac.rs/"

with sync_playwright() as p:
    # Start Chromium browser
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Otvori stranicu
    page.goto(url)
    page.wait_for_timeout(3000)  # 3 sekunde da se stranica učita

    # Nađi element #novosti
    novosti_element = page.query_selector("#novosti")

    if novosti_element:
        # Sačuvaj tekst u novosti.md
        novosti_text = novosti_element.inner_text()
        with open("novosti.md", "w", encoding="utf-8") as f:
            f.write(novosti_text)

        # Screenshot elementa
        novosti_element.screenshot(path="sip-nova-obavestenja.png")

        print("Scraping complete. novosti.md and sip-nova-obavestenja.png updated.")
    else:
        print("Element #novosti nije pronađen!")

    browser.close()
