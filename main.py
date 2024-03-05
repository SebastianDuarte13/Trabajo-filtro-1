import menus as m
import corefiles as cf
import modulos.subiractivos as s

inventario ={
    'activos': {},
    'personal': {},
    'zonas': {},
    'asignaciones': {}
}
def main():
    cf.checkDirectory()
    cf.checkFile("inventario.json",inventario)
    #s.lista_activos()
    m.mostrar_menu(cf.readDataFile("inventario.json"))
    
#Crea el Diccionario principal
#define el menu y empieza mirando si está la carpeta data
#si no existe lo crea e igualmente con el json del inventario
#nos envia al menu principal y le damos los valores para que pueda ejecutar lo necesario

if __name__=='__main__':
    main()

#falta verificart asignacion y movimientos
#falta agregar validaciones