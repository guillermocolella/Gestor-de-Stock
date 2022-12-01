import tkinter as tk
from tkinter import ttk,messagebox
from model.productos_dao import guardar,Producto,mostrar,editar,eliminar

""" Barra de menu desplegable  """

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, heigh = 300)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro')
    menu_inicio.add_command(label='Eliminar Registro')
    menu_inicio.add_separator()
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')

""" Pantalla Principal""" 
class Frame(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()
        #self.config(bg="light blue")
        self.id_producto = None

        self.campos_productos()
        self.deshabilitar_campos()
        self.tabla_productos()

    def campos_productos(self):

        """ Labels """
        # Label de Producto
        self.label_producto = tk.Label(self, text = 'Producto: ')
        self.label_producto.config(font = ('Arial', 12, 'bold'))
        self.label_producto.grid(row = 0, column = 0, padx = 10, pady= 10)

        # Label de Cantidad
        self.label_cantidad = tk.Label(self, text = 'Cantidad: ')
        self.label_cantidad.config(font = ('Arial', 12, 'bold'))
        self.label_cantidad.grid(row = 1, column = 0, padx = 10, pady= 10)

        # Label de Precio
        self.label_Precio = tk.Label(self, text = 'Precio: ')
        self.label_Precio.config(font = ('Arial', 12, 'bold'))
        self.label_Precio.grid(row = 2, column = 0, padx = 10, pady= 10)

        """ Entrys """
        # Entry de Producto
        self.mi_producto = tk.StringVar()
        self.entry_producto = tk.Entry(self, textvariable = self.mi_producto)
        self.entry_producto.config(width = 50, font = ('Arial', 12))
        self.entry_producto.grid(row = 0, column = 1, padx = 10, pady= 10, columnspan = 2)

        # Entry de Cantidad
        self.mi_cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self,textvariable = self.mi_cantidad)
        self.entry_cantidad.config(width = 50, font = ('Arial', 12))
        self.entry_cantidad.grid(row = 1, column = 1, padx = 10, pady= 10,columnspan = 2)

        # Entry de Precio
        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable = self.mi_precio)
        self.entry_precio.config(width = 50, font = ('Arial', 12))
        self.entry_precio.grid(row = 2, column = 1, padx = 10, pady= 10,columnspan = 2)

        """ botones """
        # Boton de Nuevo
        self.boton_nuevo = tk.Button(self, text = "Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width= 20, font = ('Arial', 12), fg = 'WHITE', bg='#158645', cursor= 'hand2', activebackground= '#35BD6F')
        self.boton_nuevo.grid(row= 3, column= 0, padx = 10, pady= 10)

        # Boton de Guardar
        self.boton_guardar = tk.Button(self, text = "Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width= 20, font = ('Arial', 12), fg = 'WHITE', bg='#1658A2', cursor= 'hand2', activebackground= '#3586DF')
        self.boton_guardar.grid(row= 3, column= 1, padx = 10, pady= 10)

        # Boton de Cancelar
        self.boton_cancelar = tk.Button(self, text = "Cancelar", command= self.deshabilitar_campos)
        self.boton_cancelar.config(width= 20, font = ('Arial', 12), fg = 'WHITE', bg='#BD152E', cursor= 'hand2', activebackground= '#E15370')
        self.boton_cancelar.grid(row= 3, column= 2, padx = 10, pady= 10)

        """ Funcion para Habilitar y Deshabilitar campos """
        # Habilitar Camposcls
    def habilitar_campos(self):
        self.mi_producto.set('')
        self.mi_cantidad.set('')
        self.mi_precio.set('')

        self.entry_producto.config(state = 'normal')
        self.entry_cantidad.config(state = 'normal')
        self.entry_precio.config(state = 'normal')

        self.boton_guardar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')
        
        # Deshabilitar Campos
    def deshabilitar_campos(self):
        self.id_producto = None
        
        self.mi_producto.set('')
        self.mi_cantidad.set('')
        self.mi_precio.set('')

        self.entry_producto.config(state = 'disabled')
        self.entry_cantidad.config(state = 'disabled')
        self.entry_precio.config(state = 'disabled')

        self.boton_guardar.config(state = 'disabled')
        self.boton_cancelar.config(state = 'disabled')

        """ Funcion para guardar datos """
    def guardar_datos(self):
        producto = Producto(
            self.mi_producto.get(),
            self.mi_cantidad.get(),
            self.mi_precio.get()
        )

        if self.id_producto == None:
            guardar(producto)
        else:
            editar(producto, self.id_producto)
        
        self.tabla_productos()
        self.deshabilitar_campos()


         
        """ Seccion de Tabla de Productos """

    def tabla_productos(self):
        self.lista_productos = mostrar() 
        self.lista_productos.reverse()

        self.tabla = ttk.Treeview(self,column = ('Producto','Cantidad','Precio'))       
        self.tabla.grid(row=4, column=0, columnspan=4, sticky= 'nse')  

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview) 
        self.scroll.grid(row=4, column=4, sticky= 'nse')
        self.tabla.config(yscrollcommand= self.scroll.set)

        self.tabla.heading('#0', text='ID', anchor='center')   
        self.tabla.heading('#1', text='Producto', anchor='w')    
        self.tabla.heading('#2', text='Cantidad')    
        self.tabla.heading('#3', text='Precio')  
        

        self.tabla.column("#0", anchor='center')
        self.tabla.column("#1", anchor='w')
        self.tabla.column("#2", anchor='center')
        self.tabla.column("#3", anchor='center')
        

        for p in self.lista_productos:
            self.tabla.insert('', 0, text= p[0], values= (p[1], p[2], p[3])) 
             
        # Boton Editar
        self.boton_editar = tk.Button(self, text = "Editar", command=self.editar_productos)
        self.boton_editar.config(width= 20, font = ('Arial', 12), fg = 'WHITE', bg='#158645', cursor= 'hand2', activebackground= '#35BD6F')
        self.boton_editar.grid(row= 5, column= 0, padx = 10, pady= 10) 
        # Boton Eliminar
        self.boton_eliminar = tk.Button(self, text = "Eliminar", command= self.eliminar_datos)
        self.boton_eliminar.config(width= 20, font = ('Arial', 12), fg = 'WHITE', bg='#BD152E', cursor= 'hand2', activebackground= '#E15370')
        self.boton_eliminar.grid(row= 5, column= 1, padx = 10, pady= 10)

    def editar_productos(self):
        try:
            self.id_producto = self.tabla.item(self.tabla.selection())['text']
            self.nombre_producto = self.tabla.item(self.tabla.selection())['values'][0]
            self.cantidad_producto = self.tabla.item(self.tabla.selection())['values'][1]
            self.precio_producto = self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campos()

            self.entry_producto.insert(0,self.nombre_producto)
            self.entry_cantidad.insert(0,self.cantidad_producto)
            self.entry_precio.insert(0,self.precio_producto)


        except:
            titulo = 'Edicion de datos'
            mensaje = 'No hay datos seleccionados'
            messagebox.showerror(titulo,mensaje)

    def eliminar_datos(self):

        try:
            self.id_producto = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_producto)

            self.tabla_productos()
            self.id_producto = None
        except:

            titulo = 'Edicion de datos'
            mensaje = 'No hay datos seleccionados'
            messagebox.showerror(titulo,mensaje)   

                