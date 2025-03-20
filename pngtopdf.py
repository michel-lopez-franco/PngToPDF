import img2pdf
from PIL import Image
import os

def convertir_png_a_pdf(ruta_imagen, ruta_salida_pdf):
    """
    Convierte una imagen PNG a un archivo PDF.

    :param ruta_imagen: Ruta de la imagen PNG.
    :param ruta_salida_pdf: Ruta donde se guardará el PDF.
    """
    try:
        # Verifica si la imagen es PNG
        if not ruta_imagen.lower().endswith('.png'):
            print(f"Error: {ruta_imagen} no es un archivo PNG.")
            return

        # Abre la imagen para verificar su formato
        with Image.open(ruta_imagen) as img:
            img.verify()  # Verifica que la imagen sea válida

        # Convierte la imagen a PDF
        with open(ruta_salida_pdf, "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(ruta_imagen))

        print(f"PDF creado exitosamente: {ruta_salida_pdf}")

    except Exception as e:
        print(f"Error al convertir {ruta_imagen} a PDF: {e}")

def convertir_varias_imagenes_a_pdf(lista_imagenes, ruta_salida_pdf):
    """
    Convierte varias imágenes PNG a un único archivo PDF.

    :param lista_imagenes: Lista de rutas de imágenes PNG.
    :param ruta_salida_pdf: Ruta donde se guardará el PDF.
    """
    try:
        # Verifica que todas las imágenes sean PNG
        for imagen in lista_imagenes:
            if not imagen.lower().endswith('.png'):
                print(f"Error: {imagen} no es un archivo PNG.")
                return

        # Convierte las imágenes a PDF
        with open(ruta_salida_pdf, "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(lista_imagenes))

        print(f"PDF creado exitosamente: {ruta_salida_pdf}")

    except Exception as e:
        print(f"Error al convertir las imágenes a PDF: {e}")

