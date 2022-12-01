from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    pass

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE productos'

    conexion.cursor.execute(sql)
    conexion.cerrar()

class Producto:
    def __init__(self,producto,cantidad,precio):
        self.id_producto = None
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):
        return f'Producto[{self.producto}, {self.cantidad}, {self.precio}]'

def guardar(producto):
    conexion = ConexionDB()   

    sql = f"""INSERT INTO Productos (Producto,Cantidad,Precio) VALUES('{producto.producto}','{producto.cantidad}','{producto.precio}')"""     
    conexion.cursor.execute(sql)
    conexion.cerrar()

def mostrar():
    conexion = ConexionDB()

    lista_productos = []
    sql = 'SELECT * FROM Productos'
   

    conexion.cursor.execute(sql)
    lista_productos = conexion.cursor.fetchall()
    conexion.cerrar()
    return lista_productos

def editar(producto,id_producto):
    conexion = ConexionDB()

    sql = f""" UPDATE Productos SET Producto ='{producto.producto}',
     Cantidad = '{producto.cantidad}', Precio = '{producto.precio}'
      WHERE ID = {id_producto} """

    conexion.cursor.execute(sql)
    conexion.cerrar()  

def eliminar(id_producto):
    conexion = ConexionDB()
    sql = f'DELETE FROM Productos WHERE ID = {id_producto}' 

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar de datos'
        mensaje = 'No se pudo eliminar el registro seleccionado'
        messagebox.showerror(titulo,mensaje)    
          