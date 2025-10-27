import os
from dhooks import Webhook, Embed, File

image2_path = 'sip.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[website link - click here -](https://sip.elfak.ni.ac.rs/)**",
        color=0x3498DB
    )
    
    embed.set_image(url="attachment://sip.png")
    file = File(image2_path, name="sip.png")
    hook.send("@everyone", embed=embed, file=file)
