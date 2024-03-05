from csv import reader
import corefiles as cf
import json
def lista_activos():
    #Crea una lista de activos y los guarda en un archivo JSON.

    #La función crea una lista vacía `data` y lee el archivo CSV `productos.csv`, agregando cada fila a la lista `data`.
    #Luego, crea un diccionario vacío `diccionario` utilizando el método `cf.readDataFile("inventario.json")`.
    #Recorre cada elemento de la lista `data` y crea un diccionario `Activo` con los datos del activo correspondiente a la fila actual.
    #Agrega el diccionario `Activo` al diccionario `diccionario` utilizando el código de campus como clave.
    #Finalmente, actualiza el archivo JSON `inventario.json` con el diccionario `diccionario` utilizando el método `cf.UpdateFile(ruta,diccionario)`.
    
    data=[]
    
    ruta="inventario.json"
    with open("productos.csv", "r") as file:
        lector= reader(file)
        for i in lector:
            data.append(i)
    diccionario=cf.readDataFile("inventario.json")
    for i in range (len(data)):
        #with open("data/inventario.json","r") as read:
        #    diccionario= json.loads(read.read())
        Activo={
            'codtransaccion':data[i][2],
            'NroFormulario': data[i][5],
            'nombre': data[i][6],
            'cod campus': data[i][4],
            'marca': 'compumax',
            'categoria':'Equipo de computo',
            'tipo': data[i][12],
            'valorunitario': data[i][13],
            'proveedor':'campulands',
            'nroserial': data[i][3],
            'estado': 0,
            
            'HistorialActivo':{
                'NroId':[],
                'Fecha':[],
                'tipomov':[],
                'idrespomov':[],
            }
        }
        diccionario.update({data[i][4]:Activo})    
        cf.UpdateFile(ruta,diccionario)