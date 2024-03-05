import os,art,sys
import corefiles as cf
import modulos as md
import modulos.personal as per
import modulos.reportes as rep
import modulos.movimiento_de_activos as ma
import modulos.asignacion_de_activos as asc
#datainventario={}

def mostrar_menu(inventario):
    
    global datainventario
    datainventario = inventario
    def wrapper(func):
        cf.borrar_pantalla()
        func()
        mostrar_menu(datainventario)
    cf.borrar_pantalla()
    print("SISTEMA G&C DE INVENTARIO CAMPUSLAND\n")

    cf.borrar_pantalla
    titulo =("""
        ++++++++++++++++++++++
        +   Menú Principal   +
        ++++++++++++++++++++++
    """)
    print(titulo)
    menu=('\n   1. ACTIVOS\n   2. PERSONAL\n   3. ZONAS\n   4. ASIGNACION DE ACTIVOS \n   5. REPORTES\n   6. MOVIMIENTO DE ACTIVOS\n   7. SALIR')
    print(menu)
    opcion = input("\nIngrese una de las opciones mostradas anteriormente: ")
    while opcion < "1" or opcion > "7":
        opcion= input(print('opcion no valida, por favor intentelo nuevamente:'))
        
    if opcion == "1":
        wrapper(mostrar_menu_activos)
    elif opcion == "2":
        wrapper(mostrar_menu_personal)

    elif opcion == "3":
        wrapper(mostrar_menu_zonas)
    elif opcion == "4":
        wrapper(mostrar_menu_asignacion_de_activos)
    elif opcion == "5":
        wrapper(mostrar_menu_reportes)
    elif opcion == "6":
        wrapper(mostrar_menu_movimiento_de_activos)
    elif opcion == "7":
        os.system('cls')
        art.tprint("¡Vuelva pronto!")
        sys.exit()

def mostrar_menu_activos():
    import modulos.activos as act
    print("""
        +++++++++++
        + ACTIVOS +
        +++++++++++
        1. AGREGAR
        2. EDITAR
        3. ELIMINAR
        4. BUSCAR
        5. REGRESAR AL MENU PRINCIPAL
    """)
    opcion = input("\nIngrese una de las opciones mostradas anteriormente: ")
    while opcion < '1' or opcion > '5':
        opcion= input(print('opcion no valida, por favor intentelo nuevamente:'))
    
    if opcion == "1":
        act.agregar_activo()
    elif opcion == "2":
        act.editar_activo()
    elif opcion == "3":
        act.eliminar_activo()
    elif opcion == "4":
        act.buscar_activo()
    elif opcion == "5":
        return mostrar_menu

def mostrar_menu_personal():
    print("""
        ++++++++++++
        + PERSONAL +
        ++++++++++++
        1. AGREGAR
        2. EDITAR
        3. ELIMINAR
        4. BUSCAR
        5. REGRESAR AL MENU PRINCIPAL
    """)  
    opcion = input("\nIngrese una de las opciones mostradas anteriormente: ")
    while opcion < '1' or opcion > '5':
        opcion= input(print('opcion no valida, por favor intentelo nuevamente:'))
    
    if opcion == "1":
        per.toto()
    elif opcion == "2":
        per.editar_personal()
    elif opcion == "3":
        per.eliminar_personal()
    elif opcion == "4":
        per.buscar_personal()
    elif opcion == "5":
        return mostrar_menu

def mostrar_menu_zonas():
    import modulos.zonas as zon
    print("""
        +++++++++
        + ZONAS +
        +++++++++
        1. AGREGAR
        2. EDITAR
        3. ELIMINAR
        4. BUSCAR
        5. REGRESAR AL MENU PRINCIPAL
    """)
    opcion = input("\nIngrese una de las opciones mostradas anteriormente: ")
    while opcion < '1' or opcion > '5':
        opcion= input(print('opcion no valida, por favor intentelo nuevamente:'))
    
    if opcion == "1":
        zon.agregar_zonas()
    elif opcion == "2":
        zon.editar_zonas()
    elif opcion == "3":
        zon.eliminar_zonas()
    elif opcion == "4":
        zon.buscar_zonas()
    elif opcion == "5":
        return mostrar_menu

def mostrar_menu_asignacion_de_activos():
    print("""
        +++++++++++++++++++++++++
        + ASIGNACION DE ACTIVOS +
        +++++++++++++++++++++++++
        1. CREAR ASIGNACION
        2. BUSCAR ASIGNACION
        3. REGRESAR AL MENU PRINCIPAL
    """)
    opcion = input("\nIngrese una de las opciones mostradas anteriormente: ")
    while opcion < '1' or opcion > '3':
        opcion= input(print('opcion no valida, por favor intentelo nuevamente:'))
    if opcion == "1":
        asc.crear_asignacion()
    elif opcion == "2":
        pass
        #asig.buscar_asignacion()
    elif opcion == "3":
        return mostrar_menu

def mostrar_menu_reportes():
    print("""
        ++++++++++++
        + REPORTES +
        ++++++++++++
        
    1. LISTAR TODOS LOS ACTIVOS
    2. LISTAR ACTIVOS POR CATEGORIA
    3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO
    4. LISTAR ACTIVOS Y ASIGNACION
    5. LISTAR HISTORIAL DE MOVIMIENTO DE ACTIVO
    6. REGRESAR AL MENU PRINCIPAL
    """)
    opcion = input("\nIngrese una de las opciones mostradas anteriormente: ")
    # while opcion < "1" or opcion > "6":
    #     opcion= input(print('opcion no valida, por favor intentelo nuevamente:'))
    if opcion == "1":
        rep.listar_todos_los_activos()
    elif opcion == "2":
        rep.listar_activos_por_categoria()
    elif opcion == "3":
        rep.listar_activos_dados_de_baja_por_daño()
    elif opcion == "4":
        rep.listar_activos_y_asignacion()
    elif opcion=='5':
        rep.listar_historial_por_campus()
    elif opcion == "6":
        return mostrar_menu

def mostrar_menu_movimiento_de_activos():
    print("""
        +++++++++++++++++++++++++
        + MOVIMIENTO DE ACTIVOS +
        +++++++++++++++++++++++++
        1. RETORNO DE ACTIVO
        2. DAR DE BAJA ACTIVO
        3. CAMBIAR ASIGNACION DE ACTIVO
        4. ENVIAR A GARANTIA ACTIVO
        5. REGRESAR AL MENU PRINCIPAL
    """)
    opcion = input("\nIngrese una de las opciones mostradas anteriormente: ")
    while opcion < '1' or opcion > '5':
        opcion= input(print('opcion no valida, por favor intentelo nuevamente:'))
    if opcion == "1":
        ma.retorno_de_activo()
    elif opcion == "2":
        ma.dar_de_baja_activo()
    elif opcion == "3":
        ma.cambiar_asignacion_de_activo()
    elif opcion == "4":
        ma.enviar_a_garantia_activo()
    elif opcion == "5":
        return mostrar_menu