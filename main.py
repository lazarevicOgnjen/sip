from playwright.sync_api import sync_playwright

url = "https://sip.elfak.ni.ac.rs/"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-dev-shm-usage"]
    )
    page = browser.new_page()

    # Blokiraj nepotrebne resurse (font, media, images)
    page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "font", "media"] else route.continue_())

    page.goto(url)
    # Čekaj samo #novosti element
    novosti_element = page.wait_for_selector("#novosti", timeout=10000)

    # Snimi tekst
    with open("novosti.md", "w", encoding="utf-8") as f:
        f.write(novosti_element.inner_text())

    # Screenshot elementa sa kontrolisanom veličinom
    box = novosti_element.bounding_box()
    if box:
        width = max(box["width"], 1200)
        height = min(box["height"], 1000)
        page.screenshot(path="sip-nova-obavestenja.png", clip={
            "x": box["x"],
            "y": box["y"],
            "width": width,
            "height": height
        })

    browser.close()
