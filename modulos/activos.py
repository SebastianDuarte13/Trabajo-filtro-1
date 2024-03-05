import corefiles as cf
import tabulate,os, json, time
import menus as m

def cargar_datos():
    try:
        with open('data/inventario.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}
    #Abre el json y lo carga en el archivo que necesitemos
    #ya está validado por si no encuentra  el archivo o tiene errores de formato
    
def guardar_datos(inventario_dict):
    with open('data/inventario.json', 'w') as json_file:
        json.dump(inventario_dict, json_file, indent=4)
    #actualiza el json en la ruta de data, aparte crea los espacios
    #y las llaves
       
def agregar_activo():
    try:
        inventario_dict = cargar_datos()
        cod_campus = input('Por favor ingrese codigo de campus (ej: MOU045): ')
        if cod_campus in inventario_dict:
            print("El codigo ingresado ya existe en la base de datos.")
            cf.pausar_pantalla()
            return m.mostrar_menu_personal()
        
        codtransaccion='327'
        NroFormulario = '966217823'
        nombre = input(f'Por favor ingrese el nombre (ejemplo: Mouse-Bodg50-9048-900-0044 GMRESC R3): ')
        marca = input(f'Por favor ingrese la marca(ej: compumax): ')
        categoria = input(f'Por favor ingrese la categoria(ej: Equipo de computo): ')
        tipo = input(f'Por favor digite el tipo (ej: MOUSE, CPU): ')
        valorunitario = int(input(f'Por favor ingrse el valor unitario '))
        proveedor = input(f'Por favor ingrese el proveedor del producto(EJ: campulands): ')
        nroserial = input(f'Por favor ingrese el numero de serial del producto: ')
        
        inventario_dict[cod_campus] ={
            "codigo de transaccion": codtransaccion,
            "NroFormulario": NroFormulario,
            "nombre": nombre,
            "codigo de campus": cod_campus,
            "marca": marca,
            "categoria": categoria,
            "tipo": tipo,
            "valor unitario": valorunitario,
            "proveedor": proveedor,
            "numero de serial": nroserial,
            "estado": 0,
            "Historial Activo": {
                "NroId": [],
                "Fecha": [],
                "tipomov": [],
                "idrespomov": []
            }
        }
        
        guardar_datos(inventario_dict)
        print("Datos personales guardados exitosamente.")
        cf.pausar_pantalla()
        return m.mostrar_menu_personal()
    
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico para el valor unitario.")
        cf.pausar_pantalla()
        return agregar_activo()
    
    except Exception as e:
        print(f"Se ha producido un error: {str(e)}")
        cf.pausar_pantalla()
    #agregamos los datos a un diccionario provicional
    #este luego vamos a meterlo al normal mediante la funcion
    #guardar datos
    

def editar_activo():
    try:
        inventario_dict = cargar_datos()
        valo=input("Ingrese el codigo del campus a editar: ").upper()
        if valo not in inventario_dict:
            cf.borrar_pantalla()
            print(f"El codigo ingresado como {valo} no existe en la base de datos.")
            cf.pausar_pantalla()
            return m.mostrar_menu_personal()
        #validamos que el codigo este en el diccionario y le tiramos error al usuario
        #si no existe
        
        elif valo in inventario_dict:
            print('¿Qué deseas modificar?')
        menu = [["1.","NroFormulario"],["2.", "nombre"],["3.","Marca"],["4.","Categoria movil"],["5.","Tipo"],["6.","Valor Unitario"],["7.","Proveedor"],["8","Empresa Responsable"],["9.","Ubicacion"],["10.","Regresar al menu anterior"]]
        for option in menu:
            print("".join(option))
        res = input('Por favor, indique qué desea modificar: ')
        if res == '1':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique el nuevo NroFormulario: ')
                data[key]['NroFormulario'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            #abrimos el archivo y editamos el numero de formulario
            #le pedimos el valor a ingresar y actualizamos el archivo con su respectivo
            #contenido
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
            
            
        elif res == '2':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique el nuevo nombre: ')
                data[key]['nombre'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
            #abrimos el archivo y editamos el nuevo nombre a mostrar
            #le pedimos el valor a ingresar y actualizamos el archivo con su respectivo
            #contenido
        elif res == '3':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique la nueva Marca: ')
                data[key]['marca'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
            #hacemos lo mismo pero con la marca, usa los mismos parametros
            #abrimos el archivo y editamos la marca
            #le pedimos el valor a ingresar y actualizamos el archivo con su respectivo
            #contenido
        elif res == '4':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique la nueva Categoria: ')
                data[key]['categoria'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
        elif res == '5':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique el nuevo Tipo: ')
                data[key]['tipo'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
        elif res == '6':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique el nuevo Valor Unitario: ')
                data[key]['valorunitario'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
        elif res == '7':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique el nuevo Proveedor: ')
                data[key]['proveedor'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
        elif res == '8':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique la nueva Empresa Responsable: ')
                data[key]['empresaresponsable'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
        elif res == '9':
            cf.borrar_pantalla()
            with open('data/inventario.json', 'r') as file:
                data = json.load(file)
                key=valo
                nv_nom = input('Por favor, indique la nueva Ubicacion: ')
                data[key]['ubicacion'] = nv_nom
            with open('data/inventario.json', 'w') as file:
                json.dump(data, file, indent=4)
            cf.borrar_pantalla()
            print('Dato actualizado correctamente')
            print  ('Quiere editar algun otro dato? (si/no)')
            r=input('>> ').lower()
            if r=='si':
                return editar_activo()
            elif r== 'no':
                return m.mostrar_menu_activos()
        elif res == '10':
            print('Redirigiendo al menú anterior...')
            time.sleep(3)
            return m.mostrar_menu()
        else:
            print('Opción no válida. ¿Quiere volver al menú principal? (s/n)')
            mp= input("\n>> ").lower()
            if mp=='s':
                return m.mostrar_menu()
            elif mp=='n':
                print('Reiniciando el formulario...')
                time.sleep(3)
                return m.mostrar_menu_activos()  
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico para el Valor Unitario.")
        cf.pausar_pantalla()
        return editar_activo()
    except Exception as e:
        print(f"Se ha producido un error: {str(e)}")
        cf.pausar_pantalla()



def eliminar_activo():
    try:
        inventario_dict = cargar_datos()
        elim = input('Ingrese la ID del activo a eliminar: ')
        if elim not in inventario_dict:
            print('El número de Inventario ingresado no existe en la base de datos.')
            cf.pausar_pantalla()
            return m.mostrar_menu_activos()
        
        print(f'¿Estás seguro de eliminar al activo {elim}? (s/n)')
        respuesta = input('>> ').lower()
        if respuesta == 's':
            inventario_dict.pop(elim)
            guardar_datos(inventario_dict)
            print('Activo eliminado exitosamente.')
            cf.pausar_pantalla()
            return m.mostrar_menu_activos()
        elif respuesta == 'n':
            cf.borrar_pantalla()
            print('Redirigiendo al menú principal...')
            time.sleep(2)
            return m.mostrar_menu_principal()
    except Exception as e:
        print(f"Se ha producido un error: {str(e)}")
        cf.pausar_pantalla()
    # - La función eliminar_activo():
    #   1. Carga el diccionario de datos del inventario desde el archivo.
    #   2. Solicita al usuario que ingrese la ID del activo a eliminar.
    #   3. Verifica si la ID ingresada existe en el diccionario del inventario.
    #   4. Si la ID no existe, muestra un mensaje de error y vuelve al menú de activos.
    #   5. Si la ID existe, confirma la eliminación con el usuario.
    #   6. Si el usuario confirma, elimina el activo del diccionario del inventario y guarda los cambios en el archivo.
    #   7. Muestra un mensaje de éxito y vuelve al menú de activos.


def buscar_activo():
    try:
        inventario_dict = cargar_datos()
        bus = input('Ingrese la ID del activo a buscar: ')
        if bus not in inventario_dict:
            print('El número de Inventario ingresado no existe en la base de datos.')
            cf.pausar_pantalla()
            cf.borrar_pantalla()
            return m.mostrar_menu_activos()
        
        print(inventario_dict[bus])
        cf.pausar_pantalla()
    except Exception as e:
        print(f"Se ha producido un error: {str(e)}")
        cf.pausar_pantalla()
    # - La función buscar_activo():
    #   1. Carga el diccionario de datos del inventario desde el archivo.
    #   2. Solicita al usuario que ingrese la ID del activo a buscar.
    #   3. Verifica si la ID ingresada existe en el diccionario del inventario.
    #   4. Si la ID no existe, muestra un mensaje de error y vuelve al menú de activos.
    #   5. Si la ID existe, muestra la información del activo y espera a que el usuario presione una tecla para continuar.
