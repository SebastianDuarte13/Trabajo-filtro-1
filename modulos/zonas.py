import corefiles as cf
import json, os, tabulate
import menus as m

def cargar_zonas():
    try:
        with open('data/datos_zonas.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}

def guardar_zonas(zonas_dict):
    with open('data/datos_zonas.json', 'w') as json_file:
        json.dump(zonas_dict, json_file, indent=4)




    
def agregar_zonas():
    #Agrega una nueva zona al archivo JSON `data/zonas.json`.

    #La función borra la pantalla y muestra el título 'AGREGAR ZONAS'. Luego, carga las zonas desde el archivo JSON y solicita al usuario que ingrese el número de la zona a agregar.
    #Si el número de zona ya existe en el archivo JSON, se muestra un mensaje de error y se regresa al menú anterior.
    #Si el número de zona no existe en el archivo JSON, se solicita al usuario que ingrese el nombre y capacidad de la zona.
    #Luego, se crea un nuevo diccionario con el número, nombre, y capacidad de la zona y se agrega al archivo JSON utilizando la función `guardar_zonas()`.
    #Finalmente, se borra la pantalla, se muestra un mensaje de éxito, se pausa la pantalla y se regresa al menú anterior.
    try:
        cf.borrar_pantalla()
        print('AGREGAR ZONAS')
        zonas_dict = cargar_zonas()
        zona_numero = int(input('Ingrese el numero de la zona: '))
        if zona_numero in zonas_dict:
            print("La zona ya existe.")
            cf.pausar_pantalla()
            return
        zona_nombre = str(input('Ingrese el nombre de la zona: '))
        zona_capacidad = int(input(f'Que capacidad tiene {zona_nombre}?: '))

        zonas_dict[zona_numero] = {
            'numero': zona_numero,
            'nombre': zona_nombre,
            'capacidad': zona_capacidad,
        }

        if not os.path.exists('data'):
            os.makedirs('data')

        guardar_zonas(zonas_dict)    
        cf.borrar_pantalla()
        print('Zona Agregada Correctamente!')
        cf.pausar_pantalla()
        cf.borrar_pantalla()
        return m.mostrar_menu_zonas()
    except ValueError:
        print("Error: Ingrese un número válido para la zona y su capacidad.")
        cf.pausar_pantalla()
        cf.borrar_pantalla()
        return agregar_zonas()
    except Exception as e:
        print(f"Se ha producido un error: {str(e)}")
        cf.pausar_pantalla()
        cf.borrar_pantalla()


        

def editar_zonas():
    #Edita una zona en el archivo JSON `data/datos_zonas.json`.

    #La función borra la pantalla y muestra el título 'EDITAR ZONAS'. Luego, carga las zonas desde el archivo JSON y solicita al usuario que ingrese el número de la zona a editar.
    #Si el número de zona no existe en el archivo JSON, se muestra un mensaje de error y se regresa al menú de zonas.
    #Si el número de zona existe, se muestra un menú con las opciones disponibles para editar (nombre o capacidad) y se solicita al usuario que ingrese su selección.
    #Si la selección es '1', se solicita al usuario que ingrese el nuevo nombre y se actualiza el archivo JSON con el nuevo nombre.
    #Si la selección es '2', se solicita al usuario que ingrese la nueva capacidad y se actualiza el archivo JSON con la nueva capacidad.
    #Finalmente, se borra la pantalla y se regresa al menú de zonas.

    cf.borrar_pantalla()
    print('EDITAR ZONAS')
    zonas_dict = cargar_zonas()
    zona_numero = input('Por favor ingrese el número de la Zona: ')
    
    if zona_numero not in zonas_dict:
        cf.borrar_pantalla()
        print('El numero de zona no existe en la base de datos.')
        cf.pausar_pantalla()
        cf.borrar_pantalla
        return m.mostrar_menu_zonas()   
    elif zona_numero in zonas_dict:
        cf.borrar_pantalla()
        print(f'MODIFICANDO ZONA {zona_numero}')
        print('1. Nombre')
        print('2. Capacidad')
        print('3. Regresar al Menu de Zonas')
        res=input('Indique que es lo que desea modificar: ')
        while res < '1' or res > '3':
            res = input(print('Opción Inválida, intentelo nuevamente: '))
            
        if res=='1':
            with open('data/datos_zonas.json', 'r') as file:
                data = json.load(file)
                key=zona_numero
                nv_nom = input('Porfavor indique el nuevo nombre: ')
                data[key]['nombre'] = nv_nom
                print ('Zona actualizada correctamente')
                cf.pausar_pantalla()
            with open('data/datos_zonas.json', 'w') as file:
                json.dump(data, file, indent=4)
            
        elif res =='2':
            with open('data/datos_zonas.json', 'r') as file:
                data = json.load(file)
                key=zona_numero
                nv_cap = input('Porfavor indique la nueva capacidad: ')
                data[key]['capacidad'] = nv_cap
                print ('Zona actualizada correctamente')
                cf.pausar_pantalla()
            with open('data/datos_zonas.json', 'w') as file:
                json.dump(data, file, indent=4)
            
        elif res =='3':
            cf.borrar_pantalla()
    cf.borrar_pantalla()
    return m.mostrar_menu_zonas()




def eliminar_zonas():
    #Elimina una zona del archivo JSON `data/datos_zonas.json`.

    #La función borra la pantalla y muestra el título 'ELIMINAR ZONAS'. Luego, carga las zonas desde el archivo JSON y solicita al usuario que ingrese el número de la zona a eliminar.
    #Si el número de zona no existe en el archivo JSON, se muestra un mensaje de error y se regresa al menú anterior.
    #Si el número de zona existe en el archivo JSON, se elimina del archivo JSON utilizando el método `del` y se guardan los cambios en el archivo JSON.
    #Finalmente, se borra la pantalla, se muestra un mensaje de éxito, se pausa la pantalla y se regresa al menú anterior.
    
    cf.borrar_pantalla()
    print('ELIMINAR ZONAS')
    zonas_dict = cargar_zonas()
    zona_numero = input('Por favor ingrese el número de la Zona: ')

    if zona_numero not in zonas_dict:
        cf.borrar_pantalla()
        print('El numero de zona no existe en la base de datos.')
        cf.pausar_pantalla()
        cf.borrar_pantalla()
        return m.mostrar_menu_zonas()
    elif zona_numero in zonas_dict:
        del zonas_dict[zona_numero]
        guardar_zonas('data/datos_zonas.json')
        cf.borrar_pantalla()
        print(f'Zona {zona_numero} eliminada correctamente!')
        cf.pausar_pantalla()
        cf.borrar_pantalla()
        return m.mostrar_menu_zonas()




def buscar_zonas():
    #Busca una zona en el archivo JSON `data/datos_zonas.json`.

    #La función borra la pantalla y muestra el título 'BUSCAR ZONAS'. Luego, solicita al usuario que ingrese el número de la zona a buscar.
    #Luego, se carga el archivo JSON y se busca la zona con el número ingresado.
    #Si la zona no existe en el archivo JSON, se muestra un mensaje de error.
    #Si la zona existe en el archivo JSON, se muestran los detalles de la zona (número, nombre, y capacidad).
    #Finalmente, se pausa la pantalla y se regresa al menú anterior.
    cf.borrar_pantalla()
    zona_numero = input("Ingrese el numero de la Zona: ")
    with open('data/datos_zonas.json', 'r') as file:
        data = json.load(file)
    key=zona_numero
    try:
        zona = data.get(key)
        headers = ['numero', 'nombre', 'napacidad']
        table = [[zona['numero'], zona['nombre'], zona['capacidad']]]
        os.system('cls')
        print(tabulate(table, headers, tablefmt="pretty"))

    except KeyError:
        print("Error al buscar la zona.")
    cf.pausar_pantalla()
    return m.mostrar_menu_zonas()