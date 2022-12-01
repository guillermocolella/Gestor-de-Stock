import tkinter as tk
from client.gui_app import Frame,barra_menu
import sqlite3

def main():
    root = tk.Tk()
    root.title('Gestor de Stock')
    root.iconbitmap('img\icons8-database-65.ico')
    barra_menu(root)

    app = Frame(root = root)
      


    root.mainloop()     
if __name__ == '__main__':
    main()