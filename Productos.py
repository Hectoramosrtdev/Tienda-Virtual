import pandas as pd

class Producto:
    def __init__(self, path):
        self.path = path
        self.tabla_producto = pd.DataFrame(columns=['id', 'tienda_id', 'nombre', 'codigo', 'descripcion', 'cantidad', 'cantidadMinima'])
        self.cargar_base_datos()

    def guardar_base_datos(self):
        with pd.ExcelWriter(self.path) as writer:
            self.tabla_producto.to_excel(writer, sheet_name='Producto', index=False)

    def cargar_base_datos(self):
        try:
            with pd.ExcelFile(self.path) as excel:
                self.tabla_producto = pd.read_excel(excel, sheet_name='Producto')
        except FileNotFoundError:
            print("La base de datos no existe. Se creará una nueva.")

    def listar(self):
        return self.tabla_producto

    def agregar(self, id, tienda_id, nombre, codigo, descripcion, cantidad=0, cantidadMinima=0):
        nuevo_registro = pd.DataFrame([[id, tienda_id, nombre, codigo, descripcion, cantidad, cantidadMinima]], columns=['id', 'tienda_id', 'nombre', 'codigo', 'descripcion', 'cantidad', 'cantidadMinima'])
        self.tabla_producto = pd.concat([self.tabla_producto, nuevo_registro], ignore_index=True)
        print("Producto agregado exitosamente.")

    def ver(self, id):
        registro = self.tabla_producto.loc[self.tabla_producto['id'] == id]
        if len(registro) > 0:
            return registro
        else:
            print("No se encontró ningún producto con el ID proporcionado.")

    def actualizar(self, id, tienda_id, nombre, codigo, descripcion, cantidad, cantidadMinima):
        if len(self.tabla_producto.loc[self.tabla_producto['id'] == id]) > 0:
            self.tabla_producto.loc[self.tabla_producto['id'] == id, 'tienda_id'] = tienda_id
            self.tabla_producto.loc[self.tabla_producto['id'] == id, 'nombre'] = nombre
            self.tabla_producto.loc[self.tabla_producto['id'] == id, 'codigo'] = codigo
            self.tabla_producto.loc[self.tabla_producto['id'] == id, 'descripcion'] = descripcion
            self.tabla_producto.loc[self.tabla_producto['id'] == id, 'cantidad'] = cantidad
            self.tabla_producto.loc[self.tabla_producto['id'] == id, 'cantidadMinima'] = cantidadMinima
            print("Producto actualizado exitosamente.")
        else:
            print("No se encontró ningún producto con el ID proporcionado.")

    def eliminar(self, id):
        if len(self.tabla_producto.loc[self.tabla_producto['id'] == id]) > 0:
            self.tabla_producto = self.tabla_producto.loc[self.tabla_producto['id'] != id]
            print("Producto eliminado exitosamente.")
        else:
            print("No se encontró ningún producto con el ID proporcionado.")

    def buscar_por_id(self, id):
        registro = self.tabla_producto.loc[self.tabla_producto['id'] == id]
        if len(registro) > 0:
            return registro
        else:
            print("No se encontró ningún producto con el ID proporcionado.")

    def buscar_por_codigo(self, codigo):
        registros = self.tabla_producto.loc[self.tabla_producto['codigo'] == codigo]
        if len(registros) > 0:
            return registros
        else:
            print("No se encontraron productos con el código proporcionado.")

    def buscar_por_nombre(self, nombre):
        registros = self.tabla_producto.loc[self.tabla_producto['nombre'] == nombre]
        if len(registros) > 0:
            return registros
        else:
            print("No se encontraron productos con el nombre proporcionado.")

def crear_base_datos():
    path = 'Tienda.xlsx'
    tienda = Producto(path)
    while True:
        print("======= Menú de Productos =======")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Ver producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Buscar producto por ID")
        print("7. Buscar producto por código")
        print("8. Buscar producto por nombre")
        print("9. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            productos = tienda.listar()
            print(productos)

        elif opcion == "2":
            id = int(input("Ingrese el ID del producto: "))
            tienda_id = int(input("Ingrese el ID de la tienda asociada al producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            codigo = input("Ingrese el código del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto (opcional, dejar en blanco si no desea ingresar): "))
            cantidadMinima = int(input("Ingrese la cantidad mínima del producto (opcional, dejar en blanco si no desea ingresar): "))
            tienda.agregar(id, tienda_id, nombre, codigo, descripcion, cantidad, cantidadMinima)

        elif opcion == "3":
            id = int(input("Ingrese el ID del producto a ver: "))
            registro = tienda.ver(id)
            if registro is not None:
                print(registro)

        elif opcion == "4":
            id = int(input("Ingrese el ID del producto a actualizar: "))
            tienda_id = int(input("Ingrese el nuevo ID de la tienda asociada al producto: "))
            nombre = input("Ingrese el nuevo nombre del producto: ")
            codigo = input("Ingrese el nuevo código del producto: ")
            descripcion = input("Ingrese la nueva descripción del producto: ")
            cantidad = int(input("Ingrese la nueva cantidad del producto (opcional, dejar en blanco si no desea actualizar): "))
            cantidadMinima = int(input("Ingrese la nueva cantidad mínima del producto (opcional, dejar en blanco si no desea actualizar): "))
            tienda.actualizar(id, tienda_id, nombre, codigo, descripcion, cantidad, cantidadMinima)

        elif opcion == "5":
            id = int(input("Ingrese el ID del producto a eliminar: "))
            tienda.eliminar(id)

        elif opcion == "6":
            id = int(input("Ingrese el ID del producto a buscar: "))
            registro = tienda.buscar_por_id(id)
            if registro is not None:
                print(registro)

        elif opcion == "7":
            codigo = input("Ingrese el código del producto a buscar: ")
            registros = tienda.buscar_por_codigo(codigo)
            if registros is not None:
                print(registros)

        elif opcion == "8":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            registros = tienda.buscar_por_nombre(nombre)
            if registros is not None:
                print(registros)

        elif opcion == "9":
            tienda.guardar_base_datos()
            print("Gracias por utilizar la Tienda App. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número del menú.")

crear_base_datos()
