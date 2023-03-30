import qrcode 
from PIL import Image

cabeza=input("introduzca el texto para covertir a QR:")
ima=qrcode.make(cabeza)

nombre_imagen=input("intruzacale")+'png'
archivo_imagen=open(nombre_imagen,'mb')
image_save=(archivo_imagen)
archivo_imagen.close()
ruta_image='./'+nombre_imagen
Image.open(ruta_image).show()
