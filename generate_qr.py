import qrcode
from PIL import Image

# URL del menú
url = "https://uluru92.github.io/Guarumo-static-menu/"

# Configuración del QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Alta corrección de errores
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Crear imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar
filename = "guarumo_menu_qr.png"
img.save(filename)
print(f"QR generado exitosamente: {filename}")
