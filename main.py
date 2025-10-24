from playwright.sync_api import sync_playwright
from PIL import Image

# URL za scraping
url = "https://sip.elfak.ni.ac.rs/"

# Željena širina i visina finalne slike (možeš menjati)
final_width = 500
final_height = 200

with sync_playwright() as p:
    # Start Chromium headless
    browser = p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-dev-shm-usage"]
    )
    page = browser.new_page()

    # Blokiraj nepotrebne resurse radi brzine
    page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "font", "media"] else route.continue_())

    # Otvori stranicu
    page.goto(url)
    novosti_element = page.wait_for_selector("#novosti", timeout=10000)

    if novosti_element:
        # Snimi tekst u novosti.md
        with open("novosti.md", "w", encoding="utf-8") as f:
            f.write(novosti_element.inner_text())

        # Screenshot cele stranice
        page.screenshot(path="full_page.png")

        # Dobij bounding box elementa
        box = novosti_element.bounding_box()
        if box:
            # Crop element iz full_page.png
            im = Image.open("full_page.png")
            crop_box = (
                int(box["x"]),
                int(box["y"]),
                int(box["x"] + box["width"]),
                int(box["y"] + box["height"])
            )
            im = im.crop(crop_box)

            # Opcionalno resize na željene dimenzije
            im = im.resize((final_width, final_height))
            im.save("sip-nova-obavestenja.png")

            print("Scraping complete: novosti.md and sip-nova-obavestenja.png updated.")
        else:
            print("Ne mogu da dobijem dimenzije elementa!")
    else:
        print("Element #novosti nije pronađen!")

    browser.close()
