from playwright.sync_api import sync_playwright

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

        # Dobij dimenzije elementa
        box = novosti_element.bounding_box()
        if box:
            # Prilagodi veličinu kao u Selenium primeru
            width = max(box["width"], 1200)
            height = min(box["height"], 1000)

            # Screenshot elementa preko page.screenshot sa clip
            page.screenshot(path="sip-nova-obavestenja.png", clip={
                "x": box["x"],
                "y": box["y"],
                "width": width,
                "height": height
            })

            print("Scraping complete. novosti.md and sip-nova-obavestenja.png updated.")
        else:
            print("Ne mogu da dobijem dimenzije elementa!")
    else:
        print("Element #novosti nije pronađen!")

    browser.close()
