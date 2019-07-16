# -*- coding: utf-8 -*-
import Tkinter as tk
from Tkinter import *
import pymysql
import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

try:
    #Cadena de conexión al servidor de base de datos
    db = pymysql.connect("localhost","root","","automatas2")
except:
    print("Error, no se estableció la conexión ...")

def reporte():
    lstReporte.delete(0,END)
    cursor = db.cursor()
    #Buscar
    sqlbuscar = "SELECT * FROM Keywords"
    cursor.execute(sqlbuscar)
    result=cursor.fetchall()
    cont = 1
    lstReporte.insert(0,"Clave|Nombre")
    for row in result:
        clave = row[0]
        nombre = row[1]
        lstReporte.insert(cont,"| {0} | {1} ".format(clave,nombre))
        cont = cont+1
        
def eliminar():
    cursor = db.cursor()
    clave = txtEliminar.get()
    if clave=="":
        print("Error, Favor de Ingresar una clave.")
        #tk.messageBox.showerror("Error", "Favor de Ingresar una clave.")
    else:
        try:
            #Eliminar
            sqldel = "delete from keywords where clave = "+clave
            cursor.execute(sqldel)
            db.commit()
            print("Exito, Se ha eliminado el registro.")
            #tk.messageBox.showinfo('Exito', 'Se ha eliminado el registro.')
        except:
            print("Error, no se ha podido eliminar el registro.")
            #tk.messageBox.showerror("Error", "No se ha podido eliminar el registro.")

def actualizar():
    nombre=txtNombre.get()
    clave=txtClave.get()
    cursor = db.cursor()
    #Cambiar
    try:
        sqlchange= "UPDATE keywords SET nombre = '"+nombre+"' WHERE clave = "+clave+";"
        cursor.execute(sqlchange)
        print("Exito, Se ha actualizado el registro.")
        #tk.messageBox.showinfo('Exito', 'Se ha actualizado el registro.')
        db.commit()
    except:
        print("Error, No se ha podido actualizar el registro.")
        #tk.messageBox.showerror("Error", "No se ha podido actualizar el registro.")
    

def insertar():
    cursor = db.cursor()
    clave = txtClave.get()
    nombre = txtNombre.get()
    try:
        #Podemos usar instrucciones sql por medio del cursor
        sqlinsertar = "INSERT INTO keywords VALUES("+clave+",'"+nombre+"');"
        cursor.execute(sqlinsertar)
        print("Exito, Se ha insertado el registro.")
    except:
         print("Error, No se ha podido insertar el registro.")
    
def reportePDF():
    h = A4
    c = canvas.Canvas("Reporte.pdf")
    cursor = db.cursor()
    #Buscar
    sqlbuscar = "SELECT * FROM Keywords"
    cursor.execute(sqlbuscar)
    result=cursor.fetchall()
    text = c.beginText(100,100)
    text.setFont("Times-Roman", 12)
    text.textLine("- - - - - - - - - - - REPORTE - - - - - - - - - - - -")
    text.textLine("Clave | Nombre")
    for row in result:
        clave = row[0]
        nombre = row[1]
        text.textLine("|    {0}    |    {1} ".format(clave,nombre))
    c.drawText(text)
    c.showPage()
    c.save()
    print("PDF Guardado")
    

#Crear una Ventana
ventana= Tk()
#Título de la Ventana
ventana.title("Python y Base de Datos")
#AnchoxAlto
ventana.geometry('400x400+0+0')
#Color del fondo de la Ventana
ventana.configure(background='light grey')

mainframe=Frame(ventana)
#---------------------------------------------------
#Componentes de la ventana
#Botones
btnReporte = Button(ventana,text="Imprimir reporte",command=reporte)
btnEliminar = Button(ventana,text="Eliminar Registro",command=eliminar)
btnActualizar = Button(ventana,text="Actualizar",command=actualizar)
btnReportePDF = Button(ventana,text="Crear PDF",command=reportePDF)
btnInsertar = Button(ventana,text="Insertar",command=insertar)
#Listas
lstReporte = Listbox(ventana,width=15,height=10)

#TextBox
txtEliminar = Entry(ventana)
txtNombre= Entry(ventana)
txtClave = Entry(ventana)

#Label
lblEliminar = Label(ventana,text="Clave:")
lblNombre = Label(ventana,text="Nombre:")
lblClave = Label(ventana,text="Clave:")

#---------------------------------------------------
#Componentes para Reporte
lstReporte.grid(row = 7, column=4)
btnReporte.grid(row = 8, column=4)

#Componentes para ELiminar
btnEliminar.grid(row = 1,column=3)
txtEliminar.grid(row =0,column=3)
lblEliminar.grid(row=0,column=2)

#Componentes para actualizar
lblClave.grid(row=0,column=4)
txtClave.grid(row=0,column=5)
lblNombre.grid(row=1,column=4)
txtNombre.grid(row=1,column=5)
btnActualizar.grid(row=6,column=5)

#Componentes para ReportePDF
btnReportePDF.grid(row=9,column=4)

#Componentes para Insertar
btnInsertar.grid(row=5,column=5)

ventana.mainloop()