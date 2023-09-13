import qrcode
from datetime import datetime

print("QRCode Generate Program")
print("Please type 'exit' to exit program")

while True:
    data = input("Please enter your qrcode data: ")
    if data == "exit":
        break
    else:
        img = qrcode.make(f'{data}')
        type(img)  # qrcode.image.pil.PilImage
        img.save(f"qrcodeimg/{datetime.today().strftime('%Y%m%d%H%M%S')}.png")
        print("QRCode image saved")
