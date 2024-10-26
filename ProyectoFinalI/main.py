from tkinter import messagebox
from tkinter import  ttk
import tkinter as tk
import mate
import prueba
import algebra2

#ejecutar main2

def ventana_mate():
    ventana.withdraw()
    mate.abrir_ventana_matematica_discreta()
    
def ventana_algoritmos():
    ventana.withdraw()
    prueba.abrir_algoritmos()
    
    
def ventana_algebra():
    ventana.withdraw()
    algebra2.abrir_ventana_algebra2()

    

def abrir_ventana_principal():
    global ventana
    ventana = tk.Tk()
    ventana.title("Proyecto Final segundo semestre")
    ventana.configure(bg="lightgreen")
    ventana.geometry("700x500+325+100") 
    titulo = tk.Label(ventana, text="Proyecto Final", font=("Arial", 16), background="lightgreen")
    titulo.pack(pady="10")
    
    
        
    boton_estilo = {
        'bg': 'green',    
        'fg': 'white',        
        'font': ('Arial', 10),  
        'width': 30,          
        'height': 3,          
        'borderwidth': 5,     
        'relief': 'ridge'    
    }
        
    
    boton = tk.Button(ventana, text= "Matematica Discreta", command=ventana_mate, **boton_estilo)
    boton.pack(padx="100", pady="10")

    boton2 = tk.Button(ventana, text= "Algoritmos", command=ventana_algoritmos, **boton_estilo)
    boton2.pack(padx="100", pady="10")

    boton3 =  tk.Button(ventana, text="Algebra Lineal", command= ventana_algebra, **boton_estilo)
    boton3.pack(padx="100", pady="10") 
    
    ventana.mainloop()
