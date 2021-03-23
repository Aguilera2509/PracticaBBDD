from tkinter import *
from tkinter import messagebox


root = Tk()

#----------------------------------- OTRAS CARACTERISTICAS ---------------------------

root.title("Guardado de Datos")
root.geometry("300x280")
root.iconbitmap('Database.ico.ico')
root.resizable(0,0)

#---------------------------------- DATOS PEDIDOS -----------------------------

#Falta IP------------

NameVar = Label(root, text="Nombre:")
NameVar.grid(row=0, column=3, sticky = E, pady=10, padx=10)

ApellidoVar = Label(root, text="Apellido:")
ApellidoVar.grid(row=1, column=3, sticky = E, pady=10, padx=10)

PasswordVar = Label(root, text="Contrasenia:")
PasswordVar.grid(row=2, column=3, sticky = E, pady=10, padx=10)

DirrecionVar = Label(root, text="Direccion:")
DirrecionVar.grid(row=3, column=3, sticky = E, pady=10, padx=10)

EdadVar = Label(root, text="Edad:")
EdadVar.grid(row=4, column=3, sticky = E, pady=10, padx=10)

GeneroVar = Label(root, text="Genero:")
GeneroVar.grid(row=5, column=3, sticky = E, pady=10, padx=10)

#----------------------------------- RELLENAR DATOS -------------------------------

#Falta IP Para leer---------------

NameEntry = Entry(root, width=30)
NameEntry.grid(row=0, column=4)

ApellidoEntry = Entry(root, width=30)
ApellidoEntry.grid(row=1, column=4)

PasswordEntry = Entry(root, width=30, show="*")
PasswordEntry.grid(row=2, column=4)

DirrecionEntry = Entry(root, width=30)
DirrecionEntry.grid(row=3, column=4)

EdadEntry = Entry(root, width=30)
EdadEntry.grid(row=4,column=4)

GeneroEntry = Entry(root, width=30)
GeneroEntry.grid(row=5, column=4)

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



root.mainloop()