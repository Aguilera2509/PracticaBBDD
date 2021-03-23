from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()

#----------------------------------- OTRAS CARACTERISTICAS ---------------------------

root.title("Guardado de Datos")
root.geometry("300x330")
root.iconbitmap('Database.ico.ico')
root.resizable(0,0)

#---------------------------------- DATOS PEDIDOS -----------------------------

#Falta IP -------------------------------

NameVar = Label(root, text="Nombre:")
NameVar.grid(row=0, column=0, sticky = E, pady=10, padx=10)

ApellidoVar = Label(root, text="Apellido:")
ApellidoVar.grid(row=1, column=0, sticky = E, pady=10, padx=10)

PasswordVar = Label(root, text="Contrasenia:")
PasswordVar.grid(row=2, column=0, sticky = E, pady=10, padx=10)

DirrecionVar = Label(root, text="Direccion:")
DirrecionVar.grid(row=3, column=0, sticky = E, pady=10, padx=10)

EdadVar = Label(root, text="Edad:")
EdadVar.grid(row=4, column=0, sticky = E, pady=10, padx=10)

GeneroVar = Label(root, text="Genero:")
GeneroVar.grid(row=5, column=0, sticky = E, pady=10, padx=10)

#----------------------------------- RELLENAR DATOS -------------------------------

#Falta IP Para leer---------------

NameEntry = Entry(root, width=30)
NameEntry.grid(row=0, column=1)

ApellidoEntry = Entry(root, width=30)
ApellidoEntry.grid(row=1, column=1)

PasswordEntry = Entry(root, width=30, show="*")
PasswordEntry.grid(row=2, column=1)

DirrecionEntry = Entry(root, width=30)
DirrecionEntry.grid(row=3, column=1)

EdadEntry = Entry(root, width=30)
EdadEntry.grid(row=4,column=1)

GeneroEntry = Entry(root, width=30)
GeneroEntry.grid(row=5, column=1)

#-------------------------------------- BARRA DE MENU ----------------------------------

menubar = Menu(root)
root.config(menu = menubar)

#FUNCIONES DEL LOS SUBMENUS-----------------------------------------------------

def derechosReservados():
    messagebox.showinfo(message="""Estos derechos están reservados por parte de
Aguilera D. José A.""", title="Base de Datos")

def funcion():
    messagebox.showinfo(message="""El programa sirve para almacenar datos de una persona de manera ilimitada
en su propia Pc, ya que no hay una base de datos remota, podrá hacer lo que quiera con los datos,
las personas solo tendrán que rellenar las pautas planteadas""", title="Funcion del programa")

def quit():
    opcion = messagebox.askyesno(message="¿Desea salir?",title="Salir")

    if opcion == True:
        exit()

#SubMenus------------------------------------------------

Archivomenu = Menu(menubar, tearoff=0)
Archivomenu.add_command(label="Vaciar")
Archivomenu.add_separator()
Archivomenu.add_command(label="Salir", command=quit)  #command = root.quit

BBDDmenu = Menu(menubar, tearoff=0)
BBDDmenu.add_command(label="Crear")
BBDDmenu.add_command(label="Leer")
BBDDmenu.add_command(label="Actualizar")
BBDDmenu.add_separator()
BBDDmenu.add_command(label="Eliminar")

Ayudamenu = Menu(menubar, tearoff=0)
Ayudamenu.add_command(label="Acerca de...", command=funcion)
Ayudamenu.add_separator()
Ayudamenu.add_command(label="Licencia de...", command=derechosReservados)

#Asignando los Submenus-------------------------------------

menubar.add_cascade(label="Archivo", menu= Archivomenu)
menubar.add_cascade(label="BBDD", menu= BBDDmenu)
menubar.add_cascade(label="Ayuda", menu= Ayudamenu)

#----------------------------------------------- BOTONES -----------------------------------

B1 = Button(root, text="Crear")
B1.place(x=20, y=260)
B1.config(width=5, height=2)

B2 = Button(root, text="Leer")
B2.place(x=85, y=260)
B2.config(width=5, height=2)

B3 = Button(root, text="Actualizar")
B3.place(x=150, y=260)
B3.config(width=8, height=2)

B4 = Button(root, text="Eliminar")
B4.place(x=230, y=260)
B4.config(width=6, height=2)

#--------------------------------------------- BBDD(BASE DE DATOS) -------------------------------------

root.mainloop()