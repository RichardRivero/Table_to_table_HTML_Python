from ast import expr


def leer(archivo) -> str:
    """ Lee el contenido del archivo y lo regresa como una variable str
        la funcion recibe un archivo a ruta a un archivo .txt para leerlo con en formato str
        ejemplo 
                'archivo.txt'
                './document/archivo.txt'
    """
    documento = open(archivo,'rt',encoding="utf-8")
    datos = documento.read()
    documento.close()
    return datos

def escribir(archivo,texto='',saltoLinea=0):
    """ Escribe en un archivo el contenido que se le pasa 
    se debe especificar 3 varaibles
        archivo: ruta o archivvo a escribir
        texto: texto a escribir 
        saltoLinea: 1 para hacer un salto de linea o 0 para que se colocoque seguido sin salto 
        no retorna nada solo scribe dentro del archivo  
    """
    documento = open(archivo,'at',encoding="utf-8")
    if saltoLinea == 0:
        documento.write(f"{texto}")
    else:
        documento.write(f"{texto}\n")
    documento.close()

if __name__ == "__main__":

    import os
    import etiquetas as et

    archivo = "archivo2.txt"
    textoP = "Prueba"
    textoP1 = "Prueba1"
    textoP2 = "Prueba2"
   
    leer(archivo)

    """
    escribir(archivo)
    escribir(archivo,textoP,1)
    escribir(archivo,leer(archivo))
    escribir(archivo,textoP1,1)
    escribir(archivo,textoP2,1)

    print(leer(archivo))


    escribir(archivo,et.etq_td(textoP2))
    """
#ejemplo de lectura y escritura de archivos


""""
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")     #borra un archivo 
    os.rmdir("myfolder")          #borra una carpeta

"""






