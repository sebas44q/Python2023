#TEMA: MENUS

######################################################################
from tkinter import *
######################################################################
def hola():
	print("hola jeb")
######################################################################
root= Tk()

#Se crea un menu y se agrega a la raiz
barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

#Opcion 1
#Tearoff es uná linea que sirve para separar el menu de la raiz
archivo_menu=Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar Como")
archivo_menu.add_separator() # Linea separadora -> solo visual
archivo_menu.add_command(label="Cerrar")
archivo_menu.add_command(label="Salir")

#Opcion 2
archivo_edicion=Menu(barra_menu, tearoff=0)
archivo_edicion.add_command(label="Copiar")
archivo_edicion.add_command(label="Cortar")
archivo_edicion.add_command(label="Pegar")

#Opcion 3
archivo_herramientas=Menu(barra_menu, tearoff=0)

#Opcion 3.1 #Un submenu
archivo_herramientas_hack=Menu(archivo_herramientas, tearoff=0)

archivo_herramientas_hack.add_command(label="Clonar")
archivo_herramientas_hack.add_command(label="Eliminar")
archivo_herramientas_hack.add_command(label="Rayar")

#Añadimos el submenu
archivo_herramientas.add_cascade(label="Hackear", menu=archivo_herramientas_hack)



#Opcion 4
archivo_ayudas=Menu(barra_menu, tearoff=0)
archivo_ayudas.add_command(label="Licencia")
archivo_ayudas.add_command(label="Acerca de")



#Añadimos las opciones principales, que son a su vez menus
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Edicion", menu=archivo_edicion)
barra_menu.add_cascade(label="Herramienta", menu=archivo_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=archivo_ayudas)

root.mainloop()
######################################################################
