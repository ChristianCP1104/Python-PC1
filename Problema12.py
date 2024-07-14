def obtener_tipo_mime(nombre_archivo):
    nombre_archivo = nombre_archivo.lower()
    
    if nombre_archivo.endswith('.gif'):
        return 'image/gif'
    elif nombre_archivo.endswith('.jpg') or nombre_archivo.endswith('.jpeg'):
        return 'image/jpeg'
    elif nombre_archivo.endswith('.png'):
        return 'image/png'
    elif nombre_archivo.endswith('.pdf'):
        return 'application/pdf'
    elif nombre_archivo.endswith('.txt'):
        return 'text/plain'
    elif nombre_archivo.endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'

nombre_archivo = input("Ingrese el nombre del archivo: ")

tipo_mime = obtener_tipo_mime(nombre_archivo)

print(f"El tipo MIME para '{nombre_archivo}' es: {tipo_mime}")