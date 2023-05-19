import pandas as pd

class Tienda:
    def __init__(self, path):
        self.path = path
        self.tabla = pd.DataFrame(columns=['id', 'nombre', 'direccion', 'telefono'])
        self.cargar_base_datos()

    def guardar_base_datos(self):
        self.tabla.to_excel(self.path, index=False)

    def cargar_base_datos(self):
        try:
            self.tabla = pd.read_excel(self.path)
        except FileNotFoundError:
            print("La base de datos no existe. Se creará una nueva.")

    def listar(self):
        return self.tabla

    def agregar(self, id, nombre, direccion, telefono):
        nuevo_registro = pd.DataFrame([[id, nombre, direccion, telefono]], columns=['id', 'nombre', 'direccion', 'telefono'])
        self.tabla = pd.concat([self.tabla, nuevo_registro], ignore_index=True)
        print("Registro agregado exitosamente.")

    def ver(self, id):
        registro = self.tabla.loc[self.tabla['id'] == id]
        if len(registro) > 0:
            return registro
        else:
            print("No se encontró ningún registro con el ID proporcionado.")

    def actualizar(self, id, nombre, direccion, telefono):
        if len(self.tabla.loc[self.tabla['id'] == id]) > 0:
            self.tabla.loc[self.tabla['id'] == id, 'nombre'] = nombre
            self.tabla.loc[self.tabla['id'] == id, 'direccion'] = direccion
            self.tabla.loc[self.tabla['id'] == id, 'telefono'] = telefono
            print("Registro actualizado exitosamente.")
        else:
            print("No se encontró ningún registro con el ID proporcionado.")

    def eliminar(self, id):
        if len(self.tabla.loc[self.tabla['id'] == id]) > 0:
            self.tabla = self.tabla.loc[self.tabla['id'] != id]
            print("Registro eliminado exitosamente.")
        else:
            print("No se encontró ningún registro con el ID proporcionado.")

    def buscar_por_id(self, id):
        registro = self.tabla.loc[self.tabla['id'] == id]
        if len(registro) > 0:
            return registro
        else:
            print("No se encontró ningún registro con el ID proporcionado.")

    def buscar_por_nombre(self, nombre):
        registros = self.tabla.loc[self.tabla['nombre'] == nombre]
        if len(registros) > 0:
            return registros
        else:
            print("No se encontraron registros con el nombre proporcionado.")

def mostrar_menu():
    print("======= Tienda App =======")
    print("1. Listar registros")
    print("2. Agregar registro")
    print("3. Ver registro por ID")
    print("4. Actualizar registro")
    print("5. Eliminar registro")
    print("6. Buscar registro por ID")
    print("7. Buscar registro por nombre")
    print("8. Salir")

def ejecutar_tienda():
    tienda = Tienda('tienda.xlsx')
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            registros = tienda.listar()
            print(registros)

        elif opcion == "2":
            id = input("Ingrese el ID del registro: ")
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la dirección: ")
            telefono = input("Ingrese el teléfono: ")
            tienda.agregar(id, nombre, direccion, telefono)

        elif opcion == "3":
            id = input("Ingrese el ID del registro a ver: ")
            registro = tienda.ver(id)
            if registro is not None:
                print(registro)

        elif opcion == "4":
            id = input("Ingrese el ID del registro a actualizar: ")
            nombre = input("Ingrese el nuevo nombre: ")
            direccion = input("Ingrese la nueva dirección: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            tienda.actualizar(id, nombre, direccion, telefono)

        elif opcion == "5":
            id = input("Ingrese el ID del registro a eliminar: ")
            tienda.eliminar(id)

        elif opcion == "6":
            id = input("Ingrese el ID del registro a buscar: ")
            registro = tienda.buscar_por_id(id)
            if registro is not None:
                print(registro)

        elif opcion == "7":
            nombre = input("Ingrese el nombre a buscar: ")
            registros = tienda.buscar_por_nombre(nombre)
            if registros is not None:
                print(registros)

        elif opcion == "8":
            tienda.guardar_base_datos()
            print("Gracias por utilizar la Tienda App. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número del menú.")

ejecutar_tienda()
