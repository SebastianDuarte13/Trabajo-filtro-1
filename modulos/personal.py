import json,os,time
import menus as m
from tabulate import tabulate
def cargar_datos():
    try:
        with open('data/datos_personal.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}
# Esta función carga datos personales desde un archivo json, devolviendo un diccionario vacío si el archivo no se encuentra.


def guardar_datos(personal_dict):
    with open('data/datos_personal.json', 'w') as json_file:
        json.dump(personal_dict, json_file, indent=4)
#Esta función guarda un diccionario de datos personales en un archivo JSON con formato legible.




def toto():
    os.system('cls')
    if not os.path.exists('data'):    # Verifica si el directorio 'data' existe
        os.makedirs('data')    # Crea el directorio 'data' si no existe

    def agregar_personal():
        personal_dict = cargar_datos()    # Carga los datos personales desde el archivo JSON
        nro_id = input('Por favor ingrese el número de identificación: ')    # Solicitar los datos 

        if nro_id in personal_dict:
            print("La ID ingresada ya existe en la base de datos.")
            os.system('pause')
            return m.mostrar_menu_personal

        tipo = input('indique si es natural o jurídico: ')    
        nombre_id = input('Por favor ingrese el nombre: ')    
        email_id = input(f'Por favor {nombre_id} ingrese su email: ')    
        tel_mov = input(f'Por favor {nombre_id} ingrese su número móvil: ')    
        tel_cas = input(f'Por favor {nombre_id} ingrese su número casa: ')    
        tel_per = input(f'Por favor {nombre_id} ingrese su número personal: ')    
        tel_ofi = input(f'Por favor {nombre_id} ingrese su número oficina: ')    

        personal_dict[nro_id] = {
            'numero de documento': nro_id,
            'tipo': tipo,
            'nombre': nombre_id,
            'email': email_id,
            'telefono movil': tel_mov,
            'telefono casa': tel_cas,
            'telefono personal': tel_per,
            'telefono oficial': tel_ofi,
            'asignaciones de activos': 0
        }    # Agrega los datos del personal al diccionario de datos personales

        guardar_datos(personal_dict)    # Guarda los datos personales en el archivo JSON
        print("Datos personales guardados exitosamente.")
        os.system('pause')
        return m.mostrar_menu_personal

    agregar_personal()
#Esta función permite agregar datos personales de individuos al sistema, guardándolos en un archivo JSON.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def editar_personal():
    personal_dict = cargar_datos()
    nro_id = input('Por favor ingrese el número de identificación: ')
    if nro_id not in personal_dict:
        print('El numero de identificacion ingresada no existe en la base de datos.')
        os.system('pause')
        return m.mostrar_menu_personal
    elif nro_id in personal_dict:
        print('¿Qué deseas modificar?')
        menu = [["1.","tipo"],["2.", "nombre"],["3.","Email"],["4.","Telefono movil"],["5.","telefono casa"],["6.","telefono personal"],["7.","telefono oficial"],["8","volver al menu idincipal"]]
        print(tabulate(menu, tablefmt="grid"))
        res=input('¿Por favor indique que es lo que desea modificar?: ')
        if res=='1':
            os.system('cls')
            with open('data/datos_personal.json', 'r') as file:
                data = json.load(file)
                key=nro_id
                nv_nom = input('Porfavor indique el nuevo tipo: ')
                data[key]['tipo'] = nv_nom
            with open('data/datos_personal.json', 'w') as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            print('dato actualizado en su totalidad')
            print('volviendo al menu principal...')
            time.sleep(3)
            #pasa lo mismo con el resto de las opciones
        elif res =='2':
            os.system('cls')
            with open('data/datos_personal.json', 'r') as file:
                data = json.load(file)
                key=nro_id
                nv_nom = input('Porfavor indique el nuevo nombre: ')
                data[key]['nombre'] = nv_nom
            with open('data/datos_personal.json', 'w') as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            print('dato actualizado en su totalidad')
            print('volviendo al menu principal...')
            time.sleep(3)
        elif res =='3':
            os.system('cls')
            with open('data/datos_personal.json', 'r') as file:
                data = json.load(file)
                key=nro_id
                nv_nom = input('Porfavor indique el nuevo email: ')
                data[key]['email'] = nv_nom
            with open('data/datos_personal.json', 'w') as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            print('dato actualizado en su totalidad')
            print('volviendo al menu principal...')
            time.sleep(3)
        elif res =='4':
            os.system('cls')
            with open('data/datos_personal.json', 'r') as file:
                data = json.load(file)
                key=nro_id
                nv_nom = input('Porfavor indique el nuevo telefono movil: ')
                data[key]['telefono movil'] = nv_nom
            with open('data/datos_personal.json', 'w') as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            print('dato actualizado en su totalidad')
            print('volviendo al menu principal...')
            time.sleep(3)
        elif res =='5':
            os.system('cls')
            with open('data/datos_personal.json', 'r') as file:
                data = json.load(file)
                key=nro_id
                nv_nom = input('Porfavor indique el nuevo telefono casa: ')
                data[key]['telefono casa'] = nv_nom
            with open('data/datos_personal.json', 'w') as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            print('dato actualizado en su totalidad')
            print('volviendo al menu principal...')
            time.sleep(3)
        elif res =='6':
            os.system('cls')
            with open('data/datos_personal.json', 'r') as file:
                data = json.load(file)
                key=nro_id
                nv_nom = input('Porfavor indique el nuevo telefono personal: ')
                data[key]['telefono personal'] = nv_nom
            with open('data/datos_personal.json', 'w') as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            print('dato actualizado en su totalidad')
            print('volviendo al menu principal...')
            time.sleep(3)
        elif res =='7':
            os.system('cls')
            with open('data/datos_personal.json', 'r') as file:
                data = json.load(file)
                key=nro_id
                nv_nom = input('Porfavor indique el nuevo telefono oficial: ')
                data[key]['telefono oficial'] = nv_nom
            with open('data/datos_personal.json', 'w') as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            print('dato actualizado en su totalidad')
            print('volviendo al menu principal...')
            time.sleep(3)
        elif res =='8':
            print('volviendo al menú anterior')
            os.system('pause')
            return m.mostrar_menu_personal
        else:
            print('opcion no valida quiere volver al menu principal? (s/n)')
            otra= print("\n>> ")
            if otra=='s':
                return m.mostrar_menu_pr
            elif otra=='n':
                return
            
            









#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def eliminar_personal():    
    #Elimina un registro de personal del archivo JSON `data/personal.json`.

    #La función borra la pantalla y muestra el título 'ELIMINAR PERSONAL'. Luego, carga el archivo JSON y solicita al usuario que ingrese el número de identificación del personal a eliminar.
    #Si el número de identificación no existe en el archivo JSON, se muestra un mensaje de error y se regresa al menú anterior.
    #Si el número de identificación existe en el archivo JSON, se elimina del archivo JSON utilizando el método `del` y se guardan los cambios en el archivo JSON.
    #Finalmente, se borra la pantalla, se muestra un mensaje de éxito, se pausa la pantalla y se regresa al menú anterior.
 
    personal_dict = cargar_datos()    
    elim = input('Ingrese la ID del personal a eliminar: ')    
   
    if elim not in personal_dict:    
        print('El número de identificación ingresado no existe en la base de datos.')
        os.system('pause')
        return m.mostrar_menu_personal
    else:
        print(f'¿Estás seguro de eliminar al personal registrado con el ID {elim}? (s/n)')    
        respuesta = input('>> ').lower()

        if respuesta == 's':    
            del personal_dict[elim]
            guardar_datos('data/datos_personal.json')
            print('Personal eliminado exitosamente.')
            os.system('pause')
            return m.mostrar_menu_personal
        elif respuesta == 'n':    
            os.system('cls')
            print('Redirigiendo al menú principal...')
            time.sleep(2)
            return m.mostrar_menu_pr

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def buscar_personal():
    #Busca un registro de personal en el archivo JSON `data/personal.json` por número de identificación.

    #La función borra la pantalla y muestra el título 'BUSCAR PERSONAL'. Luego, solicita al usuario que ingrese el número de identificación del personal a buscar.
    #Luego, se carga el archivo JSON y se busca el registro de personal con el número de identificación ingresado.
    #Si el registro no existe en el archivo JSON, se muestra un mensaje de error.
    #Si el registro existe en el archivo JSON, se muestran los detalles del registro (número de identificación, nombre, email, teléfonos, y asignaciones de activos).
    #Finalmente, se pausa la pantalla y se regresa al menú anterior.
    
    personal_dict = cargar_datos()    
    os.system('cls')
    nro_id = input("Ingrese el número de documento del personal a buscar: ")    
    if nro_id in personal_dict:    
        personal = personal_dict.get(nro_id)    
        headers = ['numero de documento', 'tipo', 'nombre', 'email', 'telefono movil', 'telefono casa', 'telefono personal', 'telefono oficial', 'asignaciones de activos']
        table = [[personal['numero de documento'], personal['tipo'], personal['nombre'], personal['email'], personal['telefono movil'], personal['telefono casa'], personal['telefono personal'], personal['telefono oficial'], personal['asignaciones de activos']]]

        os.system('cls')
        print(tabulate(table, headers, tablefmt="pretty"))    
        os.system('pause')
        return m.mostrar_menu_personal

    else:
        print('El número de documento ingresado no existe en la base de datos.')    
        return m.mostrar_menu_personal
