import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

data = 'Lets make the change now'

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', black_color='white')

img.save('now.png')