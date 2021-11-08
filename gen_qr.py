# Import pyqrcode
import pyqrcode
# URL or string which will represent the QR code
url = "https://arjon.es/"
# Generate QR code
qr_code = pyqrcode.create(url)
qr_code.png("image.png", scale=8)