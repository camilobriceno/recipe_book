import os, shutil
from os import system
from pathlib import Path



ruta_receta = Path(Path.home(),'Desktop','Python', 'Dia 6','Recetas')
cantidad_recetas = 0

print(f"*****Bienvenido al administrador de recetas*****")
print(f"Las recetas estan en {ruta_receta}")
for txt in Path(ruta_receta).glob("**/*.txt"):
    cantidad_recetas += 1

print(f"Tienes {cantidad_recetas} recetas")

menu = """
[1] - Leer receta
[2] - Crear receta
[3] - Crear categoria
[4] - Eliminar receta
[5] - Eliminar categoria
[6] - Finalizar programa
"""
def selecciona_categoria():
    os.chdir(ruta_receta)
    opc_usuario = input('\nIngrese el nombre de la categoria: ')
    os.chdir(opc_usuario)
    return opc_usuario

def crear_archivo():
    archivo = input("Escriba el nombre de la receta: ") + str('.txt')
    nuevo_archivo = open(archivo,'w')
    contenido = input("Escriba el contenido de la receta: ")
    nuevo_archivo.write(contenido)
    nuevo_archivo.close()
    print(f"Se ha creado correctamente la receta {archivo}")

def crear_categoria():
    nueva_categoria = input("Ingrese el nombre de la nueva categoria: ")
    os.mkdir(nueva_categoria)
    print(f"La categoria {nueva_categoria} se ha creado correctamente.")

def eliminar_receta():
    selecciona_categoria()
    lista_recetas = os.listdir()
    # print(os.getcwd())
    print(f"***** Estas son las recetas de la categoria : *****")
    for index, lista in enumerate(lista_recetas):
        print(f"-[{index}] {lista}")  # -muestra al usuario lista de recetas de esa categoria
    opcion_receta = int(input('Seleccione el numero de la receta a eliminar : '))
    os.remove(lista_recetas[opcion_receta])
    print("El archivo se ha eliminado")

def menu_recetas():
    os.chdir(ruta_receta)
    print(menu)
    opcion_usuario = input("Selecciona tu opcion: ")
    return opcion_usuario



while True:
    opcion_user = menu_recetas()
    if opcion_user == '6':
        break
    match opcion_user:
        case "1":
            selecciona_categoria()
            lista_recetas = os.listdir()
            # print(os.getcwd())
            print(f"***** Estas son las recetas de la categoria : *****")
            for index, lista in enumerate(lista_recetas):
                print(f"-[{index}] {lista}")  # -muestra al usuario lista de recetas de esa categoria
            total_lista = len(lista_recetas)
            opcion_receta = int(input('Seleccione el numero de la receta: '))
            if total_lista < opcion_receta :
                valor_receta = open(lista_recetas[opcion_receta])
                print(valor_receta.readlines())  # IMPRIME LA RECETA
            else:
                print("El numero de la receta no es correcta")
            input("Presiona Enter para volver al menú...")
        case "2":
            selecciona_categoria()
            crear_archivo()
            input("Presiona Enter para volver al menú...")
        case "3":
            crear_categoria()
            input("Presiona Enter para volver al menú...")

        case "4":
            eliminar_receta()
            input("Presiona Enter para volver al menú...")

        case "5":
            lista = os.listdir()
            lista = [archivo for archivo in lista if archivo != ".DS_Store"]
            for index, cat in enumerate(lista):
                print(f"{index} -> {cat}")
            valor_eliminar = int(input("Escoge el numero de la categoria a eliminar: "))
            cat_eliminar = os.getcwd() + '/' + lista[valor_eliminar]
            #print(cat_eliminar)
            shutil.rmtree(cat_eliminar)
            print('La categoria se ha eliminado correctamente')
            input("Presiona Enter para volver al menú...")








