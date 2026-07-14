# By Raj Shekhar Aryal
# Simple Qr Code Generator in python

import qrcode


def qr_generator(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save("QrCode.png")
    print("QR Code generated successfully as 'QrCode.png'!")


text = input("Please enter your text: ")
qr_generator(text)