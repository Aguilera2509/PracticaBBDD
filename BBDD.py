from tkinter import *
from tkinter import messagebox
import sqlite3

#CERRAR LA CONECCIÓN DE LA BASE DE DATOS

root = Tk()

#----------------------------------- OTRAS CARACTERISTICAS ---------------------------

root.title("Guardado de Datos")
root.geometry("340x375")
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

CorreoVar = Label(root, text="Correo electronico:")
CorreoVar.grid(row=6, column=0, sticky = E, pady=10, padx=10)

#----------------------------------- RELLENAR DATOS -------------------------------

#Falta IP Para leer---------------

miName = StringVar()
miApellido = StringVar()
miPassword = StringVar()
miDireccion = StringVar()
miEdad = StringVar()
miGenero = StringVar()
miCorreo = StringVar()


NameEntry = Entry(root, width=30, textvariable=miName)
NameEntry.grid(row=0, column=1)

ApellidoEntry = Entry(root, width=30, textvariable=miApellido)
ApellidoEntry.grid(row=1, column=1)

PasswordEntry = Entry(root, width=30, show="*", textvariable=miPassword)
PasswordEntry.grid(row=2, column=1)

DirrecionEntry = Entry(root, width=30, textvariable=miDireccion)
DirrecionEntry.grid(row=3, column=1)

EdadEntry = Entry(root, width=30, textvariable=miEdad)
EdadEntry.grid(row=4,column=1)
EdadEntry.config(justify="right")

GeneroEntry = Entry(root, width=30, textvariable=miGenero)
GeneroEntry.grid(row=5, column=1)

CorreoEntry = Entry(root, width=30, textvariable=miCorreo)
CorreoEntry.grid(row=6, column=1)

#-------------------------------------- BARRA DE MENU ----------------------------------

menubar = Menu(root)
root.config(menu = menubar)

#FUNCIONES DEL LOS SUBMENUS-----------------------------------------------------

def derechosReservados():
    messagebox.showinfo(message="""Estos derechos están reservados por parte de
Aguilera D. José A.""", title="Base de Datos")

def funcion():
    messagebox.showinfo(message="""El programa sirve para almacenar datos de una persona de manera ilimitada
en su propia Pc, ya que no hay una base de datos remota, las personas solo tendrán que rellenar 
las pautas planteadas""", title="Funcion del programa")

def quit():
    opcion = messagebox.askyesno(message="¿Desea salir?",title="Salir")

    if opcion == True:
        exit()

def borrar():

    miName.set("")
    miApellido.set("")
    miPassword.set("")
    miDireccion.set("")
    miEdad.set("")
    miGenero.set("")
    miCorreo.set("")

#FUNCIÓN PARA CREAR LA BASE DE DATOS----------------------------------------

def create():

    try:

        IP = sqlite3.connect("Almacenamiento De Datos.bd")
        Servidor = IP.cursor()

        Servidor.execute("CREATE TABLE Información (Nombre, Apellido, Contrasenia, Direccion, Edad, Genero, Correo_Electrico)")

        messagebox.showinfo(message="Se ha creado la Base de Datos correctamente", title="Base de Datos")

    except sqlite3.OperationalError:

        messagebox.showwarning(message="Ya la Base de Datos Existe", title="Error Operacional")

#Funciones de los SubMenus------------------------------------------------

Archivomenu = Menu(menubar, tearoff=0)
Archivomenu.add_command(label="Vaciar", command=borrar)
Archivomenu.add_separator()
Archivomenu.add_command(label="Salir", command=quit) #command = root.quit

BBDDmenu = Menu(menubar, tearoff=0)
BBDDmenu.add_command(label="Crear BBDD", command=create)

Ayudamenu = Menu(menubar, tearoff=0)
Ayudamenu.add_command(label="Acerca de...", command=funcion)
Ayudamenu.add_separator()
Ayudamenu.add_command(label="Licencia de...", command=derechosReservados)

#Asignando/Definiendo los Submenus-------------------------------------

menubar.add_cascade(label="Archivo", menu= Archivomenu)
menubar.add_cascade(label="BBDD", menu= BBDDmenu)
menubar.add_cascade(label="Ayuda", menu= Ayudamenu)


#--------------------------------------------- BBDD(BASE DE DATOS) -------------------------------------

def obtenerInformacion():

    IP2 = sqlite3.connect("Almacenamiento De Datos.bd")
    Servidor2 = IP2.cursor()

    Servidor2.execute("INSERT INTO Información VALUES ('" + miName.get() + 
        "','" + miApellido.get() +
        "','" + miPassword.get() +
        "','" + miDireccion.get() +
        "','" + miEdad.get() +
        "','" + miGenero.get() +
        "','" + miCorreo.get() + "')")

    IP2.commit()

    messagebox.showinfo(message="Se ha guardado la informacion con exito", title="Tabla De Datos")


#----------------------------------------------- BOTONES -----------------------------------

B1 = Button(root, text="Crear", command=obtenerInformacion)
B1.place(x=30, y=290)
B1.config(width=5, height=2)

B2 = Button(root, text="Leer")
B2.place(x=100, y=290)
B2.config(width=5, height=2)

B3 = Button(root, text="Actualizar")
B3.place(x=170, y=290)
B3.config(width=8, height=2)

B4 = Button(root, text="Eliminar", command=borrarInformacion)
B4.place(x=260, y=290)
B4.config(width=6, height=2)


root.mainloop()