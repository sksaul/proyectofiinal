import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  
from math import factorial
import main

#ejecutar main2

def Regresar():
    ventana.withdraw()
    main.abrir_ventana_principal()
    

def abrir_ventana_matematica_discreta():
    global ventana
    
    def calcular_permutaciones(n, r):
        return factorial(n) // factorial(n - r)

    def calcular_permutaciones_repeticion(n, r):
        return n ** r

    def calcular_combinaciones(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))

    def calcular_combinaciones_repeticion(n, r):
        return factorial(n + r - 1) // (factorial(r) * factorial(n - 1))

    def calcular():
        try:
            n = int(entry_n.get())
            r = int(entry_r.get())
            if n < 0 or r < 0 or r > n and (combobox_tipo.get() != "Combinaciones con repetición"):
                raise ValueError("Valores no válidos.")

            if combobox_opcion.get() == "Permutaciones":
                if combobox_tipo.get() == "Sin repetición":
                    resultado = calcular_permutaciones(n, r)
                    label_resultado.config(text=f"Permutaciones (Sin repetición): {resultado}")
                else: 
                    resultado = calcular_permutaciones_repeticion(n, r)
                    label_resultado.config(text=f"Permutaciones (Con repetición): {resultado}")
            else: 
                if combobox_tipo.get() == "Sin repetición":
                    resultado = calcular_combinaciones(n, r)
                    label_resultado.config(text=f"Combinaciones (Sin repetición): {resultado}")
                else: 
                    resultado = calcular_combinaciones_repeticion(n, r)
                    label_resultado.config(text=f"Combinaciones (Con repetición): {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa números enteros válidos, donde n >= r >= 0.")
            
    ventana = tk.Tk()
    ventana.title("Permutaciones y Combinaciones")
    ventana.configure(bg="lightgrey")
    ventana.geometry("700x500+325+100")
    titulo = tk.Label(ventana, text="Matematica Discreta", font=("Arial", 16), background="lightgrey")
    titulo.pack(pady="10") 

    label_n = tk.Label(ventana, text="Valor de n:", bg="lightgrey", fg="black", font=("Arial", 12))
    label_n.pack()
    entry_n = tk.Entry(ventana, bg="white", fg="black", font=("Arial", 12))
    entry_n.pack(pady="2")

    label_r = tk.Label(ventana, text="Valor de r:", bg="lightgrey", fg="black", font=("Arial", 12))
    label_r.pack()
    entry_r = tk.Entry(ventana, bg="white", fg="black", font=("Arial", 12))
    entry_r.pack(pady="2")

    opcion = tk.StringVar(value="Permutaciones") 
    label_opcion = tk.Label(ventana, text="Selecciona una opción:", bg="lightgrey", fg="black", font=("Arial", 12))
    label_opcion.pack()
    combobox_opcion = ttk.Combobox(ventana, textvariable=opcion, background="white", font=("Arial", 12))
    combobox_opcion['values'] = ("Permutaciones", "Combinaciones")
    combobox_opcion.pack(pady="2")

    tipo_opcion = tk.StringVar(value="Sin repetición") 
    label_tipo = tk.Label(ventana, text="Selecciona el tipo:", bg="lightgrey", fg="black", font=("Arial", 12))
    label_tipo.pack()
    combobox_tipo = ttk.Combobox(ventana, textvariable=tipo_opcion, background="white", font=("Arial", 12))
    combobox_tipo['values'] = ("Sin repetición", "Con repetición")
    combobox_tipo.pack(pady="2")
    
       
    boton_estilo = {
        'bg': 'blue',    
        'fg': 'white',        
        'font': ('Arial', 9),  
        'width': 20,          
        'height': 2,          
        'borderwidth': 5,     
        'relief': 'ridge'     
    }

    boton_calcular = tk.Button(ventana, text="Calcular", command=calcular, **boton_estilo)
    boton_calcular.pack(pady="6")

    label_resultado = tk.Label(ventana, text="", bg="lightyellow", fg="black", font=("Arial", 12))
    label_resultado.pack(pady="6")

    boton_regresar = tk.Button(ventana, text="Regresar", command= Regresar, **boton_estilo )
    boton_regresar.pack(padx="10", pady="30")

    ventana.mainloop()
