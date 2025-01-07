from PIL import Image

def cortar_imagen_en_4(imagen_path):
    # Abrir la imagen
    imagen = Image.open(imagen_path)
    
    # Obtener las dimensiones de la imagen
    ancho, alto = imagen.size
    
    # Calcular las dimensiones de cada parte
    mitad_ancho = ancho // 2
    mitad_alto = alto // 2
    
    # Cortar la imagen en 4 partes
    parte1 = imagen.crop((0, 0, mitad_ancho, mitad_alto))
    parte2 = imagen.crop((mitad_ancho, 0, ancho, mitad_alto))
    parte3 = imagen.crop((0, mitad_alto, mitad_ancho, alto))
    parte4 = imagen.crop((mitad_ancho, mitad_alto, ancho, alto))
    
    # Guardar las partes en archivos separados
    parte1.save("parte1.jpg")
    parte2.save("parte2.jpg")
    parte3.save("parte3.jpg")
    parte4.save("parte4.jpg")
    
    print("La imagen ha sido cortada en 4 partes y guardada como parte1.jpg, parte2.jpg, parte3.jpg y parte4.jpg")

# Ejemplo de uso
cortar_imagen_en_4("imagen.jpg")
