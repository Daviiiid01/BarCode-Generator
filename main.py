import barcode
from barcode.writer import ImageWriter

codigo = '8214982851151' #>12 digitos
codigo_de_barras = barcode.get('ean13', codigo, writer=ImageWriter())

nombre_archivo = 'codigo_de_barras.png'
codigo_de_barras.save(nombre_archivo)

print(f"Código de barras generado: {codigo}")
print(f"Archivo de imagen guardado: {nombre_archivo}")
