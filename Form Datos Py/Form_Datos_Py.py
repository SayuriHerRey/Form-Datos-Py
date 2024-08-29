##3M-SayuriHernandez-03Python
##Formulario de Registro
##Almacenamiento de TXT sin validacion
import tkinter as tk 
from tkinter import messagebox

##Definicion de funciones
def Borrar_campos ():
    tbNombres.delete(0, tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)
def borrar ():
    Borrar_campos()
    
def Guardar_campos ():
    ##Obtener los valores de los Tb
    nombres = tbNombres.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono =tbTelefono.get()
    ##Obtener la seleccion de los rb
    genero = ""
    if var_genero.get()==1:
        genero = "Hombre"
    elif var_genero.get()==2:
        genero = "Mujer"
        
    ##Generar la cadena de datos
    datos = "Nombres: " +nombres +"\n"+"Apellidos: "+apellidos +"\n"+"Edad: "+edad +"\n"+"Estatura: " +estatura +"\n"+ "Telefonp: "+telefono+"\n"+"Genero: "+ genero+"\n"
        
    ##Guardar los datos en el archivo TXT
    with open ("C:/Users/herna/OneDrive/Documentos/Datos form.txt" , "a") as archivo:
        archivo.write(datos + "\n\n")

    ##Mostrar mensaje de conformacion
    messagebox.showinfo ("Informacion" , "Datos guardados con exito: \n\n" + datos)
    Borrar_campos()

##Creacion de ventana
ventana = tk.Tk()
ventana.geometry ("520x500")
ventana .title("Formulario de Registro.03 - Py ")

##Crear variables para Rb
var_genero= tk.IntVar()

##Creae etiquetas y TextBox
lbNombres = tk.Label (ventana, text= "Nombres: ")
lbNombres.pack()

tbNombres = tk. Entry (ventana)
tbNombres.pack()

lbApellidos=tk.Label (ventana, text= "Apellidos: ")
lbApellidos.pack()

tbApellidos = tk. Entry (ventana)
tbApellidos.pack()

lbEdad= tk.Label (ventana, text = "Edad: ")
lbEdad.pack()

tbEdad= tk. Entry (ventana)
tbEdad.pack()

lbEstatura = tk.Label (ventana , text = "Estatura: ")
lbEstatura.pack()

tbEstatura = tk.Entry (ventana)
tbEstatura.pack()

lbTelefono = tk.Label(ventana , text="Telefono: ")
lbTelefono.pack()

tbTelefono = tk.Entry (ventana)
tbTelefono.pack()

lbGenero= tk.Label (ventana, text = "Genero: ")
lbGenero.pack()

rbHombre = tk.Radiobutton (ventana , text ="Hombre ", variable = var_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton (ventana , text ="Mujer ", variable = var_genero , value= 2)
rbMujer.pack()

##Creacion de borones
btnGuardar= tk.Button (ventana , text ="Guardar valores ", command = Guardar_campos)
btnGuardar.pack()

btnBorrar =tk.Button (ventana , text="Borrar valores ", command = borrar)
btnBorrar.pack()

ventana.mainloop()

