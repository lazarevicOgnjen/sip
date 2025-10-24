from playwright.sync_api import sync_playwright

# URL za scraping
url = "https://sip.elfak.ni.ac.rs/"

with sync_playwright() as p:
    # Start Chromium browser headless
    browser = p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-dev-shm-usage"]
    )
    page = browser.new_page()

    # Blokiraj nepotrebne resurse radi brzine
    page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "font", "media"] else route.continue_())

    # Otvori stranicu
    page.goto(url)
    # Čekaj #novosti element, do 10 sekundi
    novosti_element = page.wait_for_selector("#novosti", timeout=10000)

    if novosti_element:
        # Snimi tekst u novosti.md
        with open("novosti.md", "w", encoding="utf-8") as f:
            f.write(novosti_element.inner_text())

        # Dobij dimenzije elementa
        box = novosti_element.bounding_box()
        if box:
            # Podesi viewport da element stane i kontrolisana širina/visina
            viewport_width = max(int(box["width"]), 500)
            viewport_height = min(int(box["height"]), 200)
            page.set_viewport_size({"width": viewport_width, "height": viewport_height})

            # Screenshot elementa bez clip
            novosti_element.screenshot(path="sip-nova-obavestenja.png")
            print("Scraping complete: novosti.md and sip-nova-obavestenja.png updated.")
        else:
            print("Ne mogu da dobijem dimenzije elementa!")
    else:
        print("Element #novosti nije pronađen!")

    browser.close()
