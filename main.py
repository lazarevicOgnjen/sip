from playwright.sync_api import sync_playwright

url = "https://sip.elfak.ni.ac.rs/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    page.wait_for_timeout(3000)

    # Nađi element #novosti
    novosti_element = page.query_selector("#novosti")

    if novosti_element:
        # Dobij dimenzije elementa
        box = novosti_element.bounding_box()  # vraća dict sa x, y, width, height
        width = max(box['width'], 1200)       # željena širina
        height = min(box['height'], 1000)     # željena visina

        # Screenshot samo tog elementa sa željenom veličinom
        novosti_element.screenshot(path="sip-nova-obavestenja.png", clip={
            "x": box['x'],
            "y": box['y'],
            "width": width,
            "height": height
        })

        print("Screenshot napravljen sa prilagođenom veličinom.")
    else:
        print("Element #novosti nije pronađen!")

    browser.close()
