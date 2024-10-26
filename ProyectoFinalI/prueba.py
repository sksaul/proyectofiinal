import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import main


def abrir_algoritmos():
    global ventana_principal

    def cargar_datos():
        try:
            with open("datos.txt", "r") as archivo:
                datos = archivo.readlines()
            productos = []
            clientes = []
            ventas = []
            for linea in datos:
                tipo, contenido = linea.strip().split(":", 1)
                if tipo == "producto":
                    productos.append(eval(contenido))
                elif tipo == "cliente":
                    clientes.append(eval(contenido))
                elif tipo == "venta":
                    ventas.append(eval(contenido))
            return productos, clientes, ventas
        except FileNotFoundError:
            return [], [], []

    def guardar_datos(productos, clientes, ventas):
        with open("datos.txt", "w") as archivo:
            for producto in productos:
                archivo.write(f"producto:{producto}\n")
            for cliente in clientes:
                archivo.write(f"cliente:{cliente}\n")
            for venta in ventas:
                archivo.write(f"venta:{venta}\n")

    productos, clientes, ventas = cargar_datos()

    
    def crear_producto():
        codigo = entry_codigo_producto.get()
        nombre = entry_nombre_producto.get()
        existencia = entry_existencia_producto.get()
        proveedor = entry_proveedor_producto.get()
        precio = entry_precio_producto.get()

        try:
            existencia = int(existencia)  
            precio = float(precio)  
            producto = {'Código': codigo, 'Nombre': nombre, 'Existencia': existencia, 'Proveedor': proveedor, 'Precio': precio}
            productos.append(producto)
            guardar_datos(productos, clientes, ventas)
            messagebox.showinfo("Éxito", "Producto creado exitosamente")
        except ValueError:
            messagebox.showerror("Error", "La existencia y el precio deben ser números válidos.")

    def listar_productos():
        global treeview_productos  
        for i in treeview_productos.get_children():
            treeview_productos.delete(i)  

        for producto in productos:
            treeview_productos.insert("", "end", values=(producto['Código'], producto['Nombre'], producto['Existencia'], producto['Proveedor'], producto['Precio']))

    def modificar_producto():
        codigo = entry_codigo_producto.get()
        for producto in productos:
            if producto['Código'] == codigo:
                producto['Nombre'] = entry_nombre_producto.get()
                producto['Existencia'] = entry_existencia_producto.get()
                producto['Proveedor'] = entry_proveedor_producto.get()
                producto['Precio'] = entry_precio_producto.get()
                guardar_datos(productos, clientes, ventas)
                messagebox.showinfo("Éxito", "Producto modificado exitosamente")
                return
        messagebox.showerror("Error", "Producto no encontrado.")

    def eliminar_producto():
        codigo = entry_codigo_producto.get()
        for producto in productos:
            if producto['Código'] == codigo:
                productos.remove(producto)
                guardar_datos(productos, clientes, ventas)
                messagebox.showinfo("Éxito", "Producto eliminado exitosamente")
                return
        messagebox.showerror("Error", "Producto no encontrado.")

    
    def crear_cliente():
        codigo = entry_codigo_cliente.get()
        nombre = entry_nombre_cliente.get()
        direccion = entry_direccion_cliente.get()

        cliente = {'Código': codigo, 'Nombre': nombre, 'Dirección': direccion}
        clientes.append(cliente)
        guardar_datos(productos, clientes, ventas)
        messagebox.showinfo("Éxito", "Cliente creado exitosamente")

    def listar_clientes():
        global treeview_clientes  
        for i in treeview_clientes.get_children():
            treeview_clientes.delete(i)

        for cliente in clientes:
            treeview_clientes.insert("", "end", values=(cliente['Código'], cliente['Nombre'], cliente['Dirección']))

    def modificar_cliente():
        codigo = entry_codigo_cliente.get()
        for cliente in clientes:
            if cliente['Código'] == codigo:
                cliente['Nombre'] = entry_nombre_cliente.get()
                cliente['Dirección'] = entry_direccion_cliente.get()
                guardar_datos(productos, clientes, ventas)
                messagebox.showinfo("Éxito", "Cliente modificado exitosamente")
                return
        messagebox.showerror("Error", "Cliente no encontrado.")

    def eliminar_cliente():
        codigo = entry_codigo_cliente.get()
        for cliente in clientes:
            if cliente['Código'] == codigo:
                clientes.remove(cliente)
                guardar_datos(productos, clientes, ventas)
                messagebox.showinfo("Éxito", "Cliente eliminado exitosamente")
                return
        messagebox.showerror("Error", "Cliente no encontrado.")

    
    def crear_venta():
        codigo_producto = entry_codigo_producto_venta.get()
        codigo_cliente = entry_codigo_cliente_venta.get()
        cantidad = entry_cantidad_venta.get()

        try:
            cantidad = int(cantidad) 
            producto = next((p for p in productos if p['Código'] == codigo_producto), None)
            cliente = next((c for c in clientes if c['Código'] == codigo_cliente), None)

            if not producto:
                messagebox.showerror("Error", "Producto no encontrado.")
                return

            if not cliente:
                messagebox.showerror("Error", "Cliente no encontrado.")
                return

            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser mayor que cero.")
                return

            if int(producto['Existencia']) >= cantidad:
                total = cantidad * producto['Precio']
                venta = {'Código Producto': codigo_producto, 'Código Cliente': codigo_cliente, 'Cantidad': cantidad, 'Total': total}
                ventas.append(venta)
                producto['Existencia'] = int(producto['Existencia']) - cantidad  # Restar la cantidad a la existencia
                guardar_datos(productos, clientes, ventas)
                messagebox.showinfo("Éxito", f"Venta creada exitosamente. Total: Q{total:.2f}")
            else:
                messagebox.showerror("Error", "No hay suficiente existencia del producto.")
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")

    def listar_ventas():
        for i in treeview_ventas.get_children():
            treeview_ventas.delete(i)

        for venta in ventas:
            treeview_ventas.insert("", "end", values=(venta['Código Producto'], venta['Código Cliente'], venta['Cantidad'], venta['Total']))

    def anular_venta():
        codigo_producto = entry_codigo_producto_venta.get()
        codigo_cliente = entry_codigo_cliente_venta.get()
        cantidad = entry_cantidad_venta.get()

        try:
            cantidad = int(cantidad)

            for venta in ventas:
                if (venta['Código Producto'] == codigo_producto and 
                    venta['Código Cliente'] == codigo_cliente and 
                    venta['Cantidad'] == cantidad):
                    ventas.remove(venta)
                    producto = next((p for p in productos if p['Código'] == codigo_producto), None)
                    if producto:
                        producto['Existencia'] = int(producto['Existencia']) + cantidad 
                    guardar_datos(productos, clientes, ventas)
                    messagebox.showinfo("Éxito", "Venta anulada exitosamente")
                    return
            messagebox.showerror("Error", "No se encontró la venta para anular.")
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")

    def reportes_basicos():
        reportes_ventana = tk.Toplevel()
        reportes_ventana.title("Reportes Básicos")
        reportes_ventana.geometry("700x500+325+100")

        tk.Label(reportes_ventana, text="Ventas por Cliente:").pack()
        clientes_ventas = {}
        for venta in ventas:
            cliente_codigo = venta['Código Cliente']
            if cliente_codigo not in clientes_ventas:
                clientes_ventas[cliente_codigo] = 0
            clientes_ventas[cliente_codigo] += venta['Total']
        
        for cliente, total in clientes_ventas.items():
            tk.Label(reportes_ventana, text=f"Cliente {cliente}: Q{total:.2f}").pack()

        tk.Label(reportes_ventana, text="Ventas por Producto:").pack()
        productos_ventas = {}
        for venta in ventas:
            producto_codigo = venta['Código Producto']
            if producto_codigo not in productos_ventas:
                productos_ventas[producto_codigo] = 0
            productos_ventas[producto_codigo] += venta['Total']
        
        for producto, total in productos_ventas.items():
            tk.Label(reportes_ventana, text=f"Producto {producto}: Q{total:.2f}").pack()

   
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema de Inventario y Ventas")
    ventana_principal.geometry("700x500+325+100")  
    ventana_principal.configure(bg="#e0f7fa")
    

   
    def control_inventario():
        global entry_codigo_producto, entry_nombre_producto, entry_existencia_producto, entry_proveedor_producto, entry_precio_producto, treeview_productos

        inventario_ventana = tk.Toplevel(ventana_principal)
        inventario_ventana.title("Control de Inventario")
        inventario_ventana.geometry("700x500+325+100")
        inventario_ventana.configure(bg="#e0f7fa")

        
        tk.Label(inventario_ventana, text="Código:", bg="#e0f7fa").pack()
        entry_codigo_producto = tk.Entry(inventario_ventana)
        entry_codigo_producto.pack()

        tk.Label(inventario_ventana, text="Nombre:", bg="#e0f7fa").pack()
        entry_nombre_producto = tk.Entry(inventario_ventana)
        entry_nombre_producto.pack()

        tk.Label(inventario_ventana, text="Existencia:", bg="#e0f7fa").pack()
        entry_existencia_producto = tk.Entry(inventario_ventana)
        entry_existencia_producto.pack()

        tk.Label(inventario_ventana, text="Proveedor:", bg="#e0f7fa").pack()
        entry_proveedor_producto = tk.Entry(inventario_ventana)
        entry_proveedor_producto.pack()

        tk.Label(inventario_ventana, text="Precio:", bg="#e0f7fa").pack()
        entry_precio_producto = tk.Entry(inventario_ventana)
        entry_precio_producto.pack()

       
        tk.Button(inventario_ventana, text="Crear Producto", command=crear_producto, bg="aqua").pack(pady=2)
        tk.Button(inventario_ventana, text="Modificar Producto", command=modificar_producto, bg="aqua").pack(pady=2)
        tk.Button(inventario_ventana, text="Eliminar Producto", command=eliminar_producto, bg="aqua").pack(pady=2)
        tk.Button(inventario_ventana, text="Listar Productos", command=listar_productos, bg="aqua").pack(pady=2)

        
        treeview_productos = ttk.Treeview(inventario_ventana, columns=("Código", "Nombre", "Existencia", "Proveedor", "Precio"), show="headings")
        for col in treeview_productos["columns"]:
            treeview_productos.heading(col, text=col)
        treeview_productos.pack(fill="both", expand=True)

    
    def control_clientes():
        global entry_codigo_cliente, entry_nombre_cliente, entry_direccion_cliente, treeview_clientes

        clientes_ventana = tk.Toplevel(ventana_principal)
        clientes_ventana.title("Control de Clientes")
        clientes_ventana.geometry("700x500+325+100")
        clientes_ventana.configure(bg="#e0f7fa")

      
        tk.Label(clientes_ventana, text="Código:", bg="#e0f7fa").pack()
        entry_codigo_cliente = tk.Entry(clientes_ventana)
        entry_codigo_cliente.pack()

        tk.Label(clientes_ventana, text="Nombre:", bg="#e0f7fa").pack()
        entry_nombre_cliente = tk.Entry(clientes_ventana)
        entry_nombre_cliente.pack()

        tk.Label(clientes_ventana, text="Dirección:", bg="#e0f7fa").pack()
        entry_direccion_cliente = tk.Entry(clientes_ventana)
        entry_direccion_cliente.pack()

        
        tk.Button(clientes_ventana, text="Crear Cliente", command=crear_cliente, bg="aqua").pack(pady=2)
        tk.Button(clientes_ventana, text="Modificar Cliente", command=modificar_cliente, bg="aqua").pack(pady=2)
        tk.Button(clientes_ventana, text="Eliminar Cliente", command=eliminar_cliente, bg="aqua").pack(pady=2)
        tk.Button(clientes_ventana, text="Listar Clientes", command=listar_clientes, bg="aqua").pack(pady=2)


        treeview_clientes = ttk.Treeview(clientes_ventana, columns=("Código", "Nombre", "Dirección"), show="headings")
        for col in treeview_clientes["columns"]:
            treeview_clientes.heading(col, text=col)
        treeview_clientes.pack(fill="both", expand=True)

    
    def control_ventas():
        global entry_codigo_producto_venta, entry_codigo_cliente_venta, entry_cantidad_venta, treeview_ventas

        ventas_ventana = tk.Toplevel(ventana_principal)
        ventas_ventana.title("Control de Ventas")
        ventas_ventana.geometry("700x500+325+100")
        ventas_ventana.configure(bg="#e0f7fa")


        tk.Label(ventas_ventana, text="Código Producto:", bg="#e0f7fa").pack()
        entry_codigo_producto_venta = tk.Entry(ventas_ventana)
        entry_codigo_producto_venta.pack()

        tk.Label(ventas_ventana, text="Código Cliente:", bg="#e0f7fa").pack()
        entry_codigo_cliente_venta = tk.Entry(ventas_ventana)
        entry_codigo_cliente_venta.pack()

        tk.Label(ventas_ventana, text="Cantidad:", bg="#e0f7fa").pack()
        entry_cantidad_venta = tk.Entry(ventas_ventana)
        entry_cantidad_venta.pack()

  
        tk.Button(ventas_ventana, text="Crear Venta", command=crear_venta, bg="aqua").pack(pady=2)
        tk.Button(ventas_ventana, text="Anular Venta", command=anular_venta, bg="aqua").pack(pady=2)
        tk.Button(ventas_ventana, text="Listar Ventas", command=listar_ventas, bg="aqua").pack(pady=2)
        tk.Button(ventas_ventana, text="Listar Productos en Ventas", command=listar_productos_ventas, bg="aqua").pack(pady=2)

        
        treeview_ventas = ttk.Treeview(ventas_ventana, columns=("Código Producto", "Código Cliente", "Cantidad", "Total"), show="headings")
        for col in treeview_ventas["columns"]:
            treeview_ventas.heading(col, text=col)
        treeview_ventas.pack(fill="both", expand=True)

    #fondo_imagen = Image.open("fondo.jpg")  
    #fondo_imagen = fondo_imagen.resize((700, 450), Image.LANCZOS)  
    #fondo = ImageTk.PhotoImage(fondo_imagen)  

    #label_fondo = tk.Label(ventana_principal, image=fondo)

    #label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  

    def listar_productos_ventas():
        productos_ventas_ventana = tk.Toplevel(ventana_principal)
        productos_ventas_ventana.title("Lista de Productos")
        

        treeview_productos_ventas = ttk.Treeview(productos_ventas_ventana, columns=("Código", "Nombre", "Existencia", "Proveedor", "Precio"), show="headings")
        treeview_productos_ventas.heading("Código", text="Código")
        treeview_productos_ventas.heading("Nombre", text="Nombre")
        treeview_productos_ventas.heading("Existencia", text="Existencia")
        treeview_productos_ventas.heading("Proveedor", text="Proveedor")
        treeview_productos_ventas.heading("Precio", text="Precio")
        treeview_productos_ventas.pack()

        for producto in productos:
            treeview_productos_ventas.insert("", "end", values=(producto['Código'], producto['Nombre'], producto['Existencia'], producto['Proveedor'], producto['Precio']))
            

    def regresar_menu_principal():
        ventana_principal.withdraw()
        main.abrir_ventana_principal()

    
    

    menu_bar = tk.Menu(ventana_principal)
    control_menu = tk.Menu(menu_bar, tearoff=0)
    control_menu.add_command(label="Control de Inventario", command=control_inventario)
    control_menu.add_command(label="Control de Clientes", command=control_clientes)
    control_menu.add_command(label="Control de Ventas", command=control_ventas)
    menu_bar.add_cascade(label="Controles", menu=control_menu)

    reportes_menu = tk.Menu(menu_bar, tearoff=0)
    reportes_menu.add_command(label="Reportes Básicos", command=reportes_basicos)
    menu_bar.add_cascade(label="Reportes", menu=reportes_menu)

    opciones_menu = tk.Menu(menu_bar, tearoff=0)
    opciones_menu.add_command(label="Regresar al Menú Principal", command=regresar_menu_principal)
    menu_bar.add_cascade(label="Menu principal", menu=opciones_menu)

    ventana_principal.config(menu=menu_bar)

    ventana_principal.mainloop()
