import os
from dhooks import Webhook, Embed, File

image2_path = 'sip-nova-obavestenja.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[SIP link - click here -](https://sip.elfak.ni.ac.rs/)**",
        color=0x3498DB
    )
    
    embed.set_image(url="attachment://sip-nova-obavestenja.png")
    file = File(image2_path, name="sip-nova-obavestenja.png")
    hook.send("@everyone 📢 SIP", embed=embed, file=file)
