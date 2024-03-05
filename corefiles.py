import sys
import os
import json
BASE="data/"

def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")
#para no tener que llamar el cls a cada rato
#ademas sirve tanto para linux como para windows

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")
#para no llamar el pause a cada rato
#ademas verifica si andamos en linux o windows
def checkDirectory():
    if not os.path.exists(BASE):
        os.makedirs(BASE)
        
def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE+ archivo))):
        with open(BASE + archivo ,"w") as bw:
            json.dump(data,bw,indent=4)
#sirve para verificar si existe un archivo en el directorio
#especificado por la variable BASE. si no existe, crea un nuevo archivo 
#con el nombre y contenido proporcionados
# para acceder al checkfile: checkFile("usuarios.json", {})

def readDataFile(archivo):
    with open(BASE+archivo,"r+") as rf:
       return json.load(rf)
#lee el contenido de un archivo de un archivo en el directorio que queramos
#debe estar especificado por la variable BASE
#archivo es el archivo que va a leer
#para acceder a ella se pone: data = readDataFile("usuarios.json")
    
def createData(archivo,data):
    with open(BASE+archivo,"w+") as rwf:
        json.dump(data,rwf,indent=4)
#crea o sobreescribe un archivo en el directorio especificado por la BASE
#funciona con: el nombre del archivo y los datos que se van a escribir en el
#para usarlo debemos escribir: createData("usuarios.json", data)
        
def updateData(data,srcData):
    if (len(data) <=0):
        print('No se encontró información :(')
        pausar_pantalla()
    else:
        for key in data.keys():
            if(key != 'nit'):
                if(type(data[key]) == dict):
                    for key2 in data[key].keys():
                        if(bool(input(f'Desea modificar el {key2} s(si) o enter(no)'))):
                            os.system('cls')
                            data[key][key2] = input(f'Ingrese el nuevo valor para {key2} :')
                else:
                    if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                        os.system('cls')
                        data[key] = input(f'Ingrese el nuevo valor para {key} :')
        srcData['proveedores'].update({data['nit']:data})
        UpdateFile('inventario.json',srcData)
    os.system('pause')
#actualiza los datos de un archivo JSON que ya exista, toma data y srcDara
#data es un diccionario que tiene los nuevos datos que se van a poner
#srcData es el disccionario cargado desde el JSON existente
#esto reemplaza el srcData con data para luego actualizar el archivo
    
def UpdateFile(archivo,data):
    with open(BASE+ archivo,'w+') as fw:
        json.dump(data,fw,indent=4)
#Actualiza el contenido de un JSON especifico tomando dos argumentos
#el argumento (archivo) es una cadena que representa el nombre del archivo que se va a actualizar
#(data) es un objeto que representa los nuevos datos que se van a escribir en el archivo
#esto abre el archivo y escribe el objeto data
        
def delData(data):
    delVal = input("Ingrese el Nit del proveedor que desea borrar -> ")
    #la siguiente linea signifdica que deonde va proovedo
    data['proveedor'].pop(delVal)
    UpdateFile('inventario.json',data)
#elimina el elemento de un archivo JSON que tiene una lista de diccionarios
#donde elimina todo lo relacionado con el nit
#(data) es el diccinoario donde esta el archivo que queremos eliminar

def searchProv(data):
    valor = input("Ingrese el Nit del Proveedor a buscar: ")
    result = data['proveedores'].get(valor)
    nit,nombrePro,tipo,direccion = result.values()
    ciudad,ubicacion,longitud,latitud = direccion.values()
    #aqui debemos poner que valores queremos extraer y se van a mostrar al usuario
    print(f'Nit {nit}:')
    os.system('pause')
#se encarga de buscar un proveedor en el archivo de datos
# si no encuentra el proveedor, se muestra un mensaje que no

def ValidarTIP(inventario_dict):
    try:
        x=int(input('Ingrese una opcion\n'))
        if x==1:
            tipo="personal"
        elif x==2:
            tipo="zonas"
        else:
            print('Opcion no valida')
            return ValidarTIP()
        if len(inventario_dict[tipo])==0:
            print(f'No hay {tipo} registrad@s en la base de datos')
            return ValidarTIP(inventario_dict)
        return tipo
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarTIP(inventario_dict)
#es una validacion para el tipo
#pide la opcion y mira si es de personal o zonas
#mira si hay en el diccionario y si no hay  devuelve a pedirlo otra vez
    
def ValidarINT():
    try:
        x=int(input(''))
        return x
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarINT
#se utiliza para validar y obtener una entrada entera del usuario
#conviente la entrada en un entero y si funciona, lo devuelve entero
    
def ValidarKey(inventario_dict,key):
    try:
        x=str(input(''))
        inventario_dict[key][x]
        return x
    except KeyError:
        print('Elemento no existente')
        return ValidarKey(inventario_dict,key)
#se usa para mirar si la key existe en el diccionario principal
#tiene un valor asociado que si existe, lo retorna
    
def ValidarKeyInt(inventario_dict,key):
    try:
        x=int(input('Ingrese el identificador\n'))
        inventario_dict[key][str(x)]
        return x
    except KeyError:
        print('Elemento no existente')
        return ValidarKeyInt(inventario_dict,key)
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarKeyInt(inventario_dict,key)
#Esta función valida un identificador introducido por el usuario en forma de número entero para asegurarse de que exista 
#como clave en un diccionario específico. Si la clave no existe en el diccionario, muestra un mensaje de error y solicita 
#al usuario que ingrese otro identificador. Si el valor ingresado no es un número entero válido, también muestra un mensaje 
#de error y solicita al usuario que ingrese otro identificador.





def ValidarKeyExist(inventario_dict,codigoExiste)->bool:
    try:
        inventario_dict['asignaciones'][codigoExiste]
        return True
    except KeyError:
        return False

#Esta función valida si un código de activo existe en un diccionario específico. Si el código existe en la sección "asignaciones" 
#del diccionario, devuelve True; de lo contrario, devuelve False.

def ValidarKeyAsig(inventario_dict,key):
    try:
        x=str(input(' '))
        inventario_dict[key][x]
        return x
    except KeyError:
        print('Elemento no existente')
        return ValidarKey(inventario_dict,key)
    
#Esta función valida una clave introducida por el usuario para asegurarse de que exista en un diccionario específico. Solicita al usuario
#que ingrese una clave en forma de cadena y verifica si esa clave existe en el diccionario. Si la clave no existe, muestra un mensaje de
#error y solicita al usuario que ingrese otra clave.
    
def ValidarKey2(inventario_dict,key):
    try:
        x=str(input(''))
        inventario_dict[key][x]
        if inventario_dict[key][x]['Estado']==2:
            print('Activo dado de baja, no es posible asignarlo')
            return ValidarKey2(inventario_dict,key)
        elif inventario_dict[key][x]['Estado']==3:
            print('Activo en reparacion o garantia, no es posible asignarlo')
            return ValidarKey2(inventario_dict,key)
        elif inventario_dict[key][x]['Estado']==1:
            print('Activo ya asignado, no es posible asignarlo de nuevo')
            return ValidarKey2(inventario_dict,key)
        else:
            return x
    except KeyError:
        print('Elemento no existente')
        return ValidarKey(inventario_dict,key)
    
#Esta función valida una clave introducida por el usuario en un diccionario específico. Solicita al usuario que ingrese una clave en forma de
#cadena y verifica si esa clave existe en el diccionario y si el estado del activo asociado a esa clave permite su asignación. Si la clave no existe, 
#muestra un mensaje de error y solicita al usuario que ingrese otra clave. Si el activo asociado a la clave está dado de baja, en reparación/garantía 
#o ya está asignado, muestra un mensaje de error correspondiente y solicita al usuario que ingrese otra clave. Si la clave es válida y el activo asociado 
#no tiene ningún problema, devuelve la clave.

