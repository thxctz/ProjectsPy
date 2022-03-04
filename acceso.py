#CREANDO LOGIN CON PYTHON Y TKINTER.
#ASHLEY BUENO INTRIAGO
#import sqlite3
from cProfile import label
from cgitb import text
from cmath import log
from tkinter import *
import os #PERMITE REALIZAR OPERACIONES DEPENDIENTES DEL SO - Sistema Operativo
#import juegoSnake
import tkinter
from winreg import ExpandEnvironmentStrings




def abrir():
    #messagebox.showinfo(title="EY", message="Hiciste clic en abrir")
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("200x200+100+100")
    ventanaAbrir.title("Otra ventana")
    ventanaAbrir.mainloop()

#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    #root = Tk()
    #root.config(bg="#6E7EF8")
    #MAINFRAME
    #mainFrame = Frame(root)
    #mainFrame.config(width=480, height=320, bg="#6E7EF8")
    global ventana_principal
    pestas_color="#83A5AB"
    ventana_principal=Tk()
    ventana_principal.config(bg = "#4D84C7")
    #82A5ED
    ventana_principal.geometry("600x600")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Inicio de Sesión")#TITULO DE LA VENTANA
    ventana_principal.iconbitmap("programas\Iniciar Sesion\logo2.ico")
    Label(text="").pack()
    
    frame = Frame(ventana_principal)  

    # Empaqueta el frame en la raíz
    frame.pack()      

    # Como no tenemos ningún elemento dentro del frame, 
    # no tiene tamaño y aparece ocupando lo mínimo posible, 0*0 px

    # Color de fondo, background
    frame.config(bg="black")     

    # Podemos establecer un tamaño,
    # la raíz se adapta al frame que contiene
    #frame.config(width=200,height=2) 
    Frame(ventana_principal, width=480,height=320) 
    frame.config(cursor="")         # Tipo de cursor
    frame.config(relief="sunken")   # relieve del frame hundido
    frame.config(bd=25)             # tamaño del borde en píxeles 

    ventana_principal.config(bg="#438490")          # color de fondo, background
    ventana_principal.config(cursor="pirate")    # tipo de cursor (arrow defecto)
    ventana_principal.config(relief="sunken")    # relieve del root 
    ventana_principal.config(bd=25)      

 

    #RECETA PARA CREAR MENÚS

    #1.- CREAR LA BARRA DE MENÚ
    barraMenu = Menu(ventana_principal, background="black")

    #2.- CREAR LOS MENÚS
    menuArchivo = Menu(barraMenu, tearoff=False, background="white")
    menuEdicion = Menu(barraMenu, tearoff=False, background="white")

    #3.- CREAR LOS COMANDOS DE LOS MENÚS
    menuArchivo.add_command(label="Abrir", command=abrir)
    menuArchivo.add_command(label="Nuevo")
    menuArchivo.add_command(label="Guardar")
    menuArchivo.add_command(label="Cerrar")
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Salir")

    menuEdicion.add_command(label="Copiar")
    menuEdicion.add_command(label="Pegar")
    menuEdicion.add_command(label="Deshacer")
    menuEdicion.add_command(label="Rehacer")

    #4.- AGREGAR MENÚS A LA BARRA DE MENÚS
    barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
    barraMenu.add_cascade(label="Edición", menu=menuEdicion)
    #barraMenu.config(bg="#000000")
    #5.- Indicamos que la barra de menú estará en la ventana
    ventana_principal.config(menu=barraMenu)


    image = PhotoImage(file="programas\Iniciar Sesion\logo2.png")
    image = image.subsample(1,1)
    label = Label(image=image)
    label.pack()
    Label(text="").pack()

    Label(text = "BIENVENIDO", bg="#83A5AB", fg="black", width="310", height="2", font=('Lucida Sans', 30, "bold")).pack()
    Label(text="").pack()
    
    #Label(text="Por favor, ingrese sus datos para validar su cuenta", bg="navy", fg="white", width="100", height="2", font=("Lucida Sans", 15, "bold")).pack()
    

    #Label(text="Escoja su opción", bg="#183FD7", width="300", height="3", fg= "white", font=("Lucida Sans", 15, "bold")).pack()#ETIQUETA CON TEXTO
    #Label(text="").pack()
    Button(text="Iniciar Sesión", height="1", width="15", bg="black", fg= "white", font=('Lucida Sans', 15, "bold"), command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="1", width="14", bg=pestas_color, fg= "black", font=('Lucida Sans', 16, "bold"), command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    Button(text="Salir", height="1", width="15", bg="black", fg= "white", font=('Lucida Sans', 15, "bold"), command=Salir).pack()
    Label(text="").pack()
    #Button(text="Ingresar",height="1", width="20", bg=pestas_color, fg= "white", font=('Roboto', 15, "bold"), command=ingresar).pack() #BOTÓN "Acceder"
    #Label(text="").pack()
    #Button(text="Jugar", height="1", width="20", bg=pestas_color, fg= "#000000", font=("Lucida Sans", 15, "bold"), command=Juego).pack()
    #Label(text="").pack()
    ventana_principal.mainloop()

    #Button(text="Jugar",height="1", width="20", bg=pestas_color, fg= "#000000", font=("Lucida Sans", 15, "bold"), command=).pack()
    #Label(text="").pack()



#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    #ventana_registro.config(bg="#6D46E4")
    ventana_registro.geometry("450x450")
    ventana_registro.config(bg ="#83A5AB")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"
    
    miFrame=Frame(ventana_registro, width=395, height=295)
    miFrame.pack()

    mensaje=Label(miFrame,text="Ingrese sus datos: ", font=('Lucida Sans', 20, "bold"))
    mensaje.grid(row=0, column=0, columnspan=2)


    entrada_nombre=Entry(miFrame,textvariable=nombre_usuario )
    entrada_nombre.grid(row=1, column=1, padx=5, pady=5)

    entrada_clave=Entry(miFrame, textvariable=clave, show='*')
    entrada_clave.grid(row=2, column=1, padx=5, pady=5)

    etiqueta_nombre= Label(miFrame, text="Nombre de usuario: ",bg="#4F858D", fg="black", font=('Lucida Sans', 20, "bold") )
    etiqueta_nombre.grid(row=1, column=0, sticky="n", padx=5, pady=5)

    etiqueta_clave=Label(miFrame, text="Contraseña: ", bg="#4F858D", fg="black", font=('Lucida Sans', 20, "bold"))
    etiqueta_clave.grid(row=2, column=0, sticky="n", padx=5, pady=5)

    Label(ventana_registro, text="", width=50, height=2, bg="#54939C").pack()
    Button(ventana_registro, text="Registrarse", width=14, height=1, font=("Lucida Sans",16, "bold"), bg="LightGreen",
     command = registro_usuario).pack() #BOTÓN "Registrarse"


#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    #ventana_login.config(bg="#6D46E4")
    ventana_login.geometry("450x450")
    Label(ventana_login, text="Ingrese sus datos", bg="#183FD7",fg ="white", font=("Lucida Sans", 12, "bold" )).pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre de usuario: ", font=("Lucida Sans", 12, "bold")).pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña: ", font=("LLucida Sans", 12, "bold")).pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="", width=10, height=2).pack()
    Button(ventana_login, text="Acceder", font=("Lucida Sans", 12, "bold"), bg ="LightGreen", width=10, height=2, command = verifica_login).pack()

def ingresar():
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("400x400+200+200")
    ventanaAbrir.title("Otra ventana")
    ventanaAbrir.config(bg="#438490 ")




    ventanaAbrir.mainloop()
       



#VENTANA "VERIFICACION DE LOGIN".
def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 
def exito_login():
    #global ventana_ash
    global nueva_ventana
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    #EN PROCESO DE CREACIÓN DE LA VENTANA AL OBTENER ACCESO EXITOSO
    Label(ventana_exito, text="Ya puedes ingresar a ingresar ").pack()
    Button(ventana_exito, text="OK", command=borrar_exito_login).pack()
    

    
#VENTANA DE "Contraseña incorrecta".
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS
def Salir():
    global salir
    quit()

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)

 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()

ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.
#TERMINAR DE CODIFICAR LA PARTE DE LA INTERFAZ DE USUARIO 