import requests
from bs4 import BeautifulSoup
from html2image import Html2Image

# URL to scrape
url = "https://sip.elfak.ni.ac.rs/"

# Send GET request
response = requests.get(url)
response.raise_for_status()  # Raise error if request fails

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find the element with ID 'novosti'
novosti_element = soup.find(id="novosti")
novosti_text = novosti_element.get_text(strip=True) if novosti_element else "No content found."

# Save text to Markdown file
with open("novosti.md", "w") as novosti_file:
    novosti_file.write(novosti_text)

# Save screenshot of the element
hti = Html2Image(output_path='.', size=(800, 600))  # Width x Height
html_content = f"""
<html>
<head>
  <style>
    body {{ font-family: Arial, sans-serif; background: white; padding: 20px; }}
    #novosti {{ border: 1px solid #ddd; padding: 10px; }}
  </style>
</head>
<body>
  <div id="novosti">{novosti_element}</div>
</body>
</html>
"""
hti.screenshot(html_str=html_content, save_as='sip-nova-obavestenja.png')

