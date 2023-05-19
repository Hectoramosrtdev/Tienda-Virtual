import pandas as pd
from datetime import datetime

class Inventario:
    def __init__(self, path):
        self.path = path
        self.tabla_inventario = pd.DataFrame(columns=['id', 'producto_id', 'fecha', 'tipo', 'cantidad'])
        self.cargar_base_datos()

    def guardar_base_datos(self):
        with pd.ExcelWriter(self.path) as writer:
            self.tabla_inventario.to_excel(writer, sheet_name='Inventario', index=False)

    def cargar_base_datos(self):
        try:
            with pd.ExcelFile(self.path) as excel:
                self.tabla_inventario = pd.read_excel(excel, sheet_name='Inventario')
        except FileNotFoundError:
            print("La base de datos no existe. Se creará una nueva.")

    def listar(self):
        return self.tabla_inventario

    def agregar_producto(self, producto_id, cantidad):
        fecha_actual = datetime.now()
        nuevo_registro = pd.DataFrame([[len(self.tabla_inventario)+1, producto_id, fecha_actual, 'Entrada', cantidad]], columns=['id', 'producto_id', 'fecha', 'tipo', 'cantidad'])
        self.tabla_inventario = pd.concat([self.tabla_inventario, nuevo_registro], ignore_index=True)
        print("Producto agregado al inventario exitosamente.")

    def ver(self, id):
        registro = self.tabla_inventario.loc[self.tabla_inventario['id'] == id]
        if len(registro) > 0:
            return registro
        else:
            print("No se encontró ningún registro de inventario con el ID proporcionado.")

    def actualizar(self, id, producto_id, fecha, tipo, cantidad):
        if len(self.tabla_inventario.loc[self.tabla_inventario['id'] == id]) > 0:
            self.tabla_inventario.loc[self.tabla_inventario['id'] == id, 'producto_id'] = producto_id
            self.tabla_inventario.loc[self.tabla_inventario['id'] == id, 'fecha'] = fecha
            self.tabla_inventario.loc[self.tabla_inventario['id'] == id, 'tipo'] = tipo
            self.tabla_inventario.loc[self.tabla_inventario['id'] == id, 'cantidad'] = cantidad
            print("Registro de inventario actualizado exitosamente.")
        else:
            print("No se encontró ningún registro de inventario con el ID proporcionado.")

    def eliminar(self, id):
        if len(self.tabla_inventario.loc[self.tabla_inventario['id'] == id]) > 0:
            self.tabla_inventario = self.tabla_inventario.loc[self.tabla_inventario['id'] != id]
            print("Registro de inventario eliminado exitosamente.")
        else:
            print("No se encontró ningún registro de inventario con el ID proporcionado.")

    def eliminar_producto(self, producto_id, cantidad):
        registros = self.tabla_inventario.loc[self.tabla_inventario['producto_id'] == producto_id]
        if len(registros) > 0:
            registros_eliminados = registros.head(cantidad)
            self.tabla_inventario = self.tabla_inventario.drop(registros_eliminados.index)
            print("Productos eliminados del inventario exitosamente.")
        else:
            print("No se encontraron productos en el inventario con el ID proporcionado.")

def crear_base_datos():
    path = 'Tienda.xlsx'
    inventario = Inventario(path)
    while True:
        print("======= Menú de Inventario =======")
        print("1. Listar registros de inventario")
        print("2. Agregar producto al inventario")
        print("3. Ver registro de inventario por ID")
        print("4. Actualizar registro de inventario")
        print("5. Eliminar registro de inventario")
        print("6. Eliminar productos del inventario por ID de producto")
        print("7. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            registros = inventario.listar()
            print(registros)

        elif opcion == "2":
            producto_id = int(input("Ingrese el ID del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto a agregar: "))
            inventario.agregar_producto(producto_id, cantidad)

        elif opcion == "3":
            id = int(input("Ingrese el ID del registro de inventario a ver: "))
            registro = inventario.ver(id)
            if registro is not None:
                print(registro)

        elif opcion == "4":
            id = int(input("Ingrese el ID del registro de inventario a actualizar: "))
            producto_id = int(input("Ingrese el nuevo ID del producto: "))
            fecha = input("Ingrese la fecha del registro (opcional, dejar en blanco para mantener la fecha actual): ")
            tipo = input("Ingrese el tipo del registro (Entrada o Salida): ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario.actualizar(id, producto_id, fecha, tipo, cantidad)

        elif opcion == "5":
            id = int(input("Ingrese el ID del registro de inventario a eliminar: "))
            inventario.eliminar(id)

        elif opcion == "6":
            producto_id = int(input("Ingrese el ID del producto a eliminar del inventario: "))
            cantidad = int(input("Ingrese la cantidad de productos a eliminar: "))
            inventario.eliminar_producto(producto_id, cantidad)

        elif opcion == "7":
            inventario.guardar_base_datos()
            print("Gracias por utilizar la aplicación de Inventario. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número del menú.")

crear_base_datos()
