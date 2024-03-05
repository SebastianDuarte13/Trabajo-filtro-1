import os
import json
import corefiles as cf
#from tabulate import tabulate

def crear_asignacion():
    print('hola')
    os.system('pause')
    # try:
    #     # Load the data from datos_persona.json
    #     with open('datos_persona.json', 'r') as f:
    #         datos_personas = json.load(f)

    #     # Request the user's ID number
    #     numero_identidad = input('Ingrese su número de identidad: ')

    #     # Check if the person is registered
    #     if numero_identidad not in datos_personas:
    #         print('La persona no está registrada en la base de datos.')
    #         return

        # Continue with the rest of the asignacion_activo() function logic here

    # except FileNotFoundError:
    #     print('Archivo de datos no encontrado.')
    # except json.JSONDecodeError:
    #     print('Error al decodificar el archivo JSON.')
    # except Exception as e:
    #     print(f'Error: {str(e)}')

        
# Se imprime un título de pantalla que indica que se está creando una nueva asignación.
# Se lee el contenido del archivo JSON inventario.json en una variable de Python llamada inventario_dict.
# Se verifica si existen zonas o personal en la base de datos. Si no existen, se muestra un mensaje de error y se sale de la función.
# Se solicita al usuario que ingrese el código del activo a asignar y se valida su entrada.
# Se solicita al usuario que ingrese la fecha de asignación y se almacena en la variable Fecha.
# Se presenta un menú al usuario para seleccionar el tipo de asignación: personal o zona. Se valida la entrada del usuario y se almacena en la variable Tipo.
# Si el tipo de asignación es una zona, se solicita al usuario que ingrese el código de la zona a la que se asignará el activo y se almacena en la variable codigoAsig. Si el tipo de asignación es personal, se solicita al usuario que ingrese el ID del personal al que se asignará el activo y se almacena en la variable codigoAsig.
# Se verifica si el codigoAsig existe en el inventario. Si existe, se agrega la nueva asignación a la lista de asignaciones del codigoAsig. Si no existe, se crea una nueva entrada en el diccionario inventario_dict con la clave codigoAsig y se agrega la nueva asignación a la entrada correspondiente.
# Se actualiza el historial de activos del CodActivo con la nueva asignación.
# Se guarda el inventario actualizado en el archivo inventario.json.
        
# def buscar_asignacion():
#     llave='asignaciones'
#     with open(ruta,"r") as read:
#         dictCampus=json.loads(read.read())
#     DondeAsig=cf.ValidarKeyINT(dictCampus,llave)
#     Asignacion=dictCampus[llave][str(DondeAsig)]
#     print(Asignacion) 
#     x=str(input('Digite cualquier letra para continuar'))
# Se asigna la clave 'asignaciones' a la variable llave y se abre el archivo inventario.json en modo lectura.
# Se carga el contenido del archivo JSON en una variable de Python llamada dictCampus.
# Se solicita al usuario que ingrese el número de asignación que desea buscar y se valida su entrada.
# Se verifica si el número de asignación existe en el diccionario dictCampus. Si no existe, se muestra un mensaje de error y se sale de la función.
# Si el número de asignación existe, se asigna a la variable DondeAsig y se obtiene la información de la asignación correspondiente desde el diccionario dictCampus.
# Se imprime la información de la asignación encontrada.
# Se solicita al usuario que presione cualquier tecla para continuar.