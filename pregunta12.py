extensiones_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}


nombre_archivo = input("Ingrese el nombre del archivo: ")


punto_index = nombre_archivo.rfind(".")
if punto_index != -1:
    extension = nombre_archivo[punto_index:].lower()
else:
    extension = ""


tipo_mime = extensiones_mime.get(extension, "application/octet-stream")

print("Tipo MIME:", tipo_mime)