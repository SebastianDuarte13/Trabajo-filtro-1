import corefiles as cf
import json

ruta="data/Inventario.json"

def retorno_de_activo():
    llave='activos'
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())

    print('Ingrese el Codigo del activo')
    cod=cf.ValidarKey(dictCampus,llave)
    if dictCampus['activos'][cod]['Estado']==3:
        print('Ingrese el ID del personal que hara el retorno\n')
        codigo=cf.ValidarKeyAsig(dictCampus,"personal")
        fecha=str(input('Ingrese la fecha\n'))
        dictCampus['activos'][cod]['Estado']=0
        print(f'El activo {cod} ha sido retornado, listo para ser asignado')
        dictCampus['activos'][cod]['HistorialActivo']['NroId'].append(codigo)
        dictCampus['activos'][cod]['HistorialActivo']['Fecha'].append(fecha)
        dictCampus['activos'][cod]['HistorialActivo']['tipoMov'].append("Retorno")
        dictCampus['activos'][cod]['HistorialActivo']['idRespMov'].append(codigo)
        dictCampus['asignaciones'][id]['Activos'].remove(str(cod))
        if len(dictCampus['asignaciones'][id]['Activos'])==0:
            dictCampus['asignaciones'].pop(str(id))
        else:
            pass
        with open(ruta,"w+") as createdata:
            json.dump(dictCampus,createdata,indent=4)
    else:
        print(f'El activo {cod} no se encuentra en garantia o reparacion, no es posible retornarlo')
    x=input('Digite una tecla para continuar')

def dar_de_baja_activo():
    llave='activos'
    with open (ruta,"r") as read:
        dictCampus=json.loads(read.read())
    
    print('Ingrese el codigo del activo')
    cod=cf.ValidarKey(dictCampus,llave)
    if dictCampus['activos'][cod]['Estado']==3:
        fecha=input('Ingrese la fecha\n')
        print('Ingrese el id del personal que dara de baja al activo')
        id=cf.ValidarKeyAsig(dictCampus,"personal")

        dictCampus['activos'][cod]['HistorialActivo']['NroId'].append(id)
        dictCampus['activos'][cod]['HistorialActivo']['Fecha'].append(fecha)
        dictCampus['activos'][cod]['HistorialActivo']['tipoMov'].append("Dado de baja")
        dictCampus['activos'][cod]['HistorialActivo']['idRespMov'].append(id)
        dictCampus['activos'][cod]['Estado']=2
        dictCampus['asignaciones'][id]['Activos'].remove(str(cod))
        if len(dictCampus['asignaciones'][id]['Activos'])==0:
            dictCampus['asignaciones'].pop(str(id))
        else:
            pass
        with open(ruta,"w+") as createdata:
            json.dump(dictCampus,createdata,indent=4)

    else:
        print('No es posible dar de baja este Activo, unicamente a los activos que esten en garantia o reparacion')
    x=(input('Digite una tecla para continuar'))


def enviar_a_garantia_activo():
    llave='activos'
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    
    print('Ingrese el codigo del activo')
    cod=cf.ValidarKey(dictCampus,llave)

    if dictCampus['activos'][cod]['Estado']==1:
        fecha=input('Ingrese la fecha\n')
        print('Ingrese el id del personal que dara de baja al activo')
        id=cf.ValidarKeyAsig(dictCampus,"personal")

        dictCampus['activos'][cod]['HistorialActivo']['NroId'].append(id)
        dictCampus['activos'][cod]['HistorialActivo']['Fecha'].append(fecha)
        dictCampus['activos'][cod]['HistorialActivo']['tipoMov'].append("Garantia o reparacion")
        dictCampus['activos'][cod]['HistorialActivo']['idRespMov'].append(id)
        dictCampus['activos'][cod]['Estado']=3
        dictCampus['asignaciones'][id]['Activos'].remove(str(cod))
        if len(dictCampus['asignaciones'][id]['Activos'])==0:
            dictCampus['asignaciones'].pop(str(id))
        else:
            pass
        with open(ruta,"w+") as createdata:
            json.dump(dictCampus,createdata,indent=4)

    else:
        print('No es posible enviar a garantia este activo, unicamente a los activos que esten asigandos')
    x=(input('Digite una tecla para continuar'))


def cambiar_asignacion_de_activo():
    llave='activos'
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())

    print('Ingrese el codigo del activo')
    cod=cf.ValidarKey(dictCampus,llave)

    if dictCampus['activos'][cod]['Estado']==1:
        fecha=(input('Ingrese la fecha\n'))
        print('Ingrese el codigo de la zona')
        codigoExiste=cf.ValidarKeyExist(dictCampus,"zonas")
        codigoAsig=cf.ValidarKeyAsig(dictCampus,codigoExiste)

        if codigoExiste:
            dictCampus['asignasiones'][codigoAsig]['FechaAsignacion'].append(fecha)
            dictCampus['asignasiones'][codigoAsig]['Activos'].append(cod)
        else:
            Asignacion={
                    'FechaAsignacion':[fecha],
                    'TipoAsignacion':"zonas",
                    'Cod':codigoAsig,
                    'Activos':[cod]
                }
            dictCampus['asignaciones'].update({codigoAsig:Asignacion})
        dictCampus['activos'][cod]['HistorialActivo']['NroId'].append(codigoAsig)
        dictCampus['activos'][cod]['HistorialActivo']['Fecha'].append(fecha)
        dictCampus['activos'][cod]['HistorialActivo']['tipoMov'].append("Re-Asignado")
        dictCampus['activos'][cod]['HistorialActivo']['idRespMov'].append(codigoAsig)
       
        dictCampus['asignaciones'][id]['Activos'].remove(str(cod))
        if len(dictCampus['asignaciones'][id]['Activos'])==0:
            dictCampus['asignaciones'].pop(str(id))
        else:
            pass
        with open(ruta,"w+") as createdata:
            json.dump(dictCampus,createdata,indent=4)
    else:
        print('No es posible enviar a garantia este activo, unicamente a los activos que esten asigandos')
    x=(input('Digite una tecla para continuar'))