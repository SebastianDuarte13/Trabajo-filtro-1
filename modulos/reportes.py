import json,os
from tabulate import tabulate 
import corefiles as cf

dictCampus = {}
ruta = "data/inventario.json"

def listar_todos_los_activos():
    ruta = 'data/inventario.json'
    os.system('cls')

    with open(ruta, "r") as archivo:
        data = json.load(archivo)

    lista_activos = []

    for clave, valor in data["activos"].items():
        activo = [
            clave,
            valor["nombre"],
            valor["marca"],
            valor["tipo"],
            valor["estado"]
        ]
        lista_activos.append(activo)

    cont = 0
    mostrar_mas = 's'
    while mostrar_mas.lower() == 's':
        activos_a_mostrar = lista_activos[cont:cont+30]
        print(tabulate(activos_a_mostrar, headers=["Código", "Nombre", "Marca", "Tipo", "Estado"], tablefmt="pretty"))

        cont += 30
        if cont >= len(lista_activos):
            break

        mostrar_mas = input('¿Desea mostrar más activos? (s para Sí, Enter para No): ')

    input('Presione cualquier tecla para salir...')



def listar_activos_por_categoria():
    ruta = 'data/inventario.json'
    os.system('cls')

    try:
        with open(ruta, "r") as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        print("El archivo de inventario no se ha encontrado.")
        return

    categorias = set()
    for activo in data.get("activos", {}).values():
        categorias.add(activo.get("categoria", ""))

    if not categorias:
        print("No hay categorías disponibles en el inventario.")
        return

    print("Categorías disponibles:")
    for idx, categoria in enumerate(categorias, start=1):
        print(f"{idx}. {categoria}")

    try:
        seleccion = int(input("Seleccione la categoría que desea ver: ")) - 1
        categoria_seleccionada = list(categorias)[seleccion]
    except (ValueError, IndexError):
        print("La selección no es válida.")
        return

    lista_activos_categoria = []

    for clave, valor in data.get("activos", {}).items():
        if valor.get("categoria", "") == categoria_seleccionada:
            activo = [
                clave,
                valor.get("nombre", ""),
                valor.get("marca", ""),
                valor.get("tipo", ""),
                valor.get("estado", "")
            ]
            lista_activos_categoria.append(activo)

    if not lista_activos_categoria:
        print(f"No hay activos en la categoría '{categoria_seleccionada}'.")
        return

    cont = 0
    mostrar_mas = 's'
    while mostrar_mas.lower() == 's':
        activos_a_mostrar = lista_activos_categoria[cont:cont+30]
        print(tabulate(activos_a_mostrar, headers=["Código", "Nombre", "Marca", "Tipo", "Estado"], tablefmt="pretty"))

        cont += 30
        if cont >= len(lista_activos_categoria):
            break

        mostrar_mas = input('¿Desea mostrar más activos? (s para Sí, Enter para No): ')

    input('Presione cualquier tecla para salir...')




def listar_todos_los_activos():
    #Lista los activos disponibles en el archivo JSON `data/activos.json` por categoría.

    #La función muestra un menú con las categorías disponibles y solicita al usuario que ingrese el número de la categoría a mostrar.
    #Luego, se carga el archivo JSON y se llama a la función `listar_por_categoria()` con la categoría seleccionada.
    #Si el usuario ingresa un número inválido, se muestra un mensaje de error.
    #Si el usuario no ingresa ningún número, se muestra un mensaje de error y se regresa al menú anterior.
    #Finalmente, se pausa la pantalla y se regresa al menú anterior.
    
    categorias_disponibles = ['Equipo de computo', 'Electrodomestico', 'Juego']
    
    print("Categorías disponibles:")
    for idx, categoria in enumerate(categorias_disponibles, 1):
        print(f"{idx}. {categoria}")

    seleccion = input("Por favor ingrese el número de la categoría que desea ver: ")

    try:
        seleccion_idx = int(seleccion)
        if seleccion_idx < 1 or seleccion_idx > len(categorias_disponibles):
            print("Selección inválida.")
            return
        categoria_seleccionada = categorias_disponibles[seleccion_idx - 1]
        listar_activos_por_categoria(categoria_seleccionada)
    except ValueError:
        print("Por favor ingrese un número válido.")

    input('Presione Enter para salir...')

def listar_activos_por_categoria():
    listar_todos_los_activos()




def listar_por_estado(estado):
    pass


    os.system('clear')
    with open(ruta, "r") as archivo:
        dictCampus = json.load(archivo)
    
    activos_estado = []

    # Filtrar activos por estado
    for clave, valor in dictCampus.items():
        if valor["estado"] == estado:
            activos_estado.append([
                clave,
                valor["nombre"],
                valor["marca"],
                valor["tipo"],
                valor["categoria"]
            ])

    # Tabular los activos del estado seleccionado
    if activos_estado:
        print(f"== Activos con estado {estado} ==")
        print(tabulate(activos_estado, headers=["Código", "Nombre", "Marca", "Tipo", "Categoría"], tablefmt="pretty"))
    else:
        print(f"No se encontraron activos con estado {estado}.")

def listar_activos_dados_de_baja_por_daño():
    #Lista los activos dados de baja por daño.

    #La función muestra un menú de estados disponibles y solicita al usuario quese el número del estado que desea ver.
    #Si el usuario ingresa un número válido, se llama a la función `listar_por_estado()` con el estado seleccionado.
    
    estados_disponibles = ['2', '3']  

    print("Estados disponibles:")
    print("2. Dado de baja por daño 2")
    print("3. En reparación y/o Garantia 3")

    seleccion = input("Por favor ingrese el número del estado que desea ver: ")  

    try:
        seleccion_idx = int(seleccion)  
        if seleccion_idx < 2 or seleccion_idx > len(estados_disponibles) - 1:
            print("Selección inválida.")
            return
        estado_seleccionado = int(estados_disponibles[seleccion_idx])
        listar_por_estado(estado_seleccionado)  
    except ValueError:
        print("Por favor ingrese un número válido.")  

    input('Presione Enter para salir...')  

def listar_activos_y_asignacion():
    #Lista los activos por estado de asignación.

    #La función muestra un menú de estados disponibles y solicita al usuario que ingrese el número del estado que desea ver.
    #Si el usuario ingresa un número válido, se llama a la función `listar_por_estado()` con el estado seleccionado.
    
    estados_disponibles = ['0', '1']  

    print("Estados disponibles:")
    print("0. activo 0")
    print("1. asignado 1")

    seleccion = input("Por favor ingrese el número del estado que desea ver: ")  

    try:
        seleccion_idx = int(seleccion)  
        if seleccion_idx < 0 or seleccion_idx > len(estados_disponibles) - 1:
            print("Selección inválida.")
            return
        estado_seleccionado = int(estados_disponibles[seleccion_idx])
        listar_por_estado(estado_seleccionado)  
    except ValueError:
        print("Por favor ingrese un número válido.")  
    input('Presione Enter para salir...')  