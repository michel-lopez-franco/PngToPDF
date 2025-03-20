import pngtopdf
import os

# Ejemplo de uso
if __name__ == "__main__":
    # Convertir una sola imagen
    #pngtopdf.convertir_png_a_pdf("imagen.png", "salida.pdf")

    # Convertir varias imágenes
    #lista_imagenes = ["imagen1.png", "imagen2.png", "imagen3.png"]
    # Cargar todos los nombres de archivos PNG de la carpeta imgs
    carpeta_imgs = "imgs"
    lista_imagenes = [os.path.join(carpeta_imgs, archivo) for archivo in os.listdir(carpeta_imgs) if archivo.endswith(".png")]
    
    pngtopdf.convertir_varias_imagenes_a_pdf(lista_imagenes, "salida_multiple.pdf")