import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import main

def abrir_ventana_algebra2():
    global root
    


    class MatrixCalculator:
        def __init__(self, root):
            self.root = root
            self.root.title("Calculadora de Matrices")
            self.root.geometry("700x500+325+100")
            
            
          
            self.matrix_a = None
            self.matrix_b = None
            self.result_matrix = None
            
            
            self.notebook = ttk.Notebook(root)
            self.notebook.pack(pady=10, expand=True)
            
           
            self.inverse_frame = ttk.Frame(self.notebook)
            self.multiply_frame = ttk.Frame(self.notebook)
            self.system_frame = ttk.Frame(self.notebook)
            self.boton_regresar_frame = ttk.Frame(self.notebook)
            
           
            self.notebook.add(self.inverse_frame, text="Matriz Inversa")
            self.notebook.add(self.multiply_frame, text="Multiplicación")
            self.notebook.add(self.system_frame, text="Sistema de Ecuaciones")
            self.notebook.add(self.boton_regresar_frame, text="Menu Principal")
            
            
            self.setup_inverse_tab()
            self.setup_multiply_tab()
            self.setup_system_tab()
            self.setup_boton_regresar_tab()
            
        def setup_boton_regresar_tab(self):
            button = ttk.Button(self.boton_regresar_frame, text="Regresar al menu principal", command=self.boton_regresar)
            button.pack(pady=20)

        def boton_regresar(self):
            root.withdraw()
            main.abrir_ventana_principal()
            

        def setup_inverse_tab(self):
            
            dim_frame = ttk.Frame(self.inverse_frame)
            dim_frame.pack(pady=10)
            
            ttk.Label(dim_frame, text="Dimensión de la matriz:").pack(side=tk.LEFT)
            self.inverse_dim = ttk.Spinbox(dim_frame, from_=2, to=4, width=5)
            self.inverse_dim.pack(side=tk.LEFT, padx=5)
            
            
            ttk.Button(self.inverse_frame, text="Crear Matriz", 
                    command=self.create_inverse_matrix).pack(pady=5)
            
            
            self.inverse_matrix_frame = ttk.Frame(self.inverse_frame)
            self.inverse_matrix_frame.pack(pady=10)
            
            
            self.inverse_result_frame = ttk.Frame(self.inverse_frame)
            self.inverse_result_frame.pack(pady=10)

        def setup_multiply_tab(self):
            
            dim_frame = ttk.Frame(self.multiply_frame)
            dim_frame.pack(pady=10)
            
            ttk.Label(dim_frame, text="Dimensiones (MxN, NxP):").pack(side=tk.LEFT)
            self.mult_dim_m = ttk.Spinbox(dim_frame, from_=2, to=4, width=5)
            self.mult_dim_n = ttk.Spinbox(dim_frame, from_=2, to=4, width=5)
            self.mult_dim_p = ttk.Spinbox(dim_frame, from_=2, to=4, width=5)
            
            self.mult_dim_m.pack(side=tk.LEFT, padx=5)
            self.mult_dim_n.pack(side=tk.LEFT, padx=5)
            self.mult_dim_p.pack(side=tk.LEFT, padx=5)
            
            
            ttk.Button(self.multiply_frame, text="Crear Matrices", 
                    command=self.create_multiply_matrices).pack(pady=5)
            
           
            self.mult_matrix_a_frame = ttk.Frame(self.multiply_frame)
            self.mult_matrix_a_frame.pack(pady=10)
            
            self.mult_matrix_b_frame = ttk.Frame(self.multiply_frame)
            self.mult_matrix_b_frame.pack(pady=10)
            
            self.mult_result_frame = ttk.Frame(self.multiply_frame)
            self.mult_result_frame.pack(pady=10)

        def setup_system_tab(self):
       
            config_frame = ttk.Frame(self.system_frame)
            config_frame.pack(pady=10)
        
      
            dim_frame = ttk.Frame(config_frame)
            dim_frame.pack(fill='x', pady=5)
            ttk.Label(dim_frame, text="Número de ecuaciones:").pack(side=tk.LEFT, padx=5)
            self.system_dim = ttk.Spinbox(dim_frame, from_=2, to=3, width=5)
            self.system_dim.pack(side=tk.LEFT, padx=5)
        
        
            method_frame = ttk.Frame(config_frame)
            method_frame.pack(fill='x', pady=5)
            ttk.Label(method_frame, text="Método:").pack(side=tk.LEFT, padx=5)
            self.method_var = tk.StringVar(value="gauss")
            ttk.Radiobutton(method_frame, text="Gauss-Jordan", 
                    variable=self.method_var, value="gauss").pack(side=tk.LEFT)
            ttk.Radiobutton(method_frame, text="Cramer", 
                    variable=self.method_var, value="cramer").pack(side=tk.LEFT)
        
     
            button_frame = ttk.Frame(config_frame)
            button_frame.pack(fill='x', pady=5)
            ttk.Button(button_frame, text="Crear Sistema", 
                command=self.create_equation_inputs).pack(pady=5)
        
       
            self.system_equations_frame = ttk.Frame(self.system_frame)
            self.system_equations_frame.pack(pady=10)
        
       
            self.system_result_frame = ttk.Frame(self.system_frame)
            self.system_result_frame.pack(pady=10)
        
       
            self.graph_frame = ttk.Frame(self.system_frame)
            self.graph_frame.pack(pady=10)

        def create_inverse_matrix(self):
            n = int(self.inverse_dim.get())
            
        
            for widget in self.inverse_matrix_frame.winfo_children():
                widget.destroy()
            for widget in self.inverse_result_frame.winfo_children():
                widget.destroy()
            
          
            self.inverse_entries = []
            for i in range(n):
                row = []
                for j in range(n):
                    entry = ttk.Entry(self.inverse_matrix_frame, width=8)
                    entry.grid(row=i, column=j, padx=2, pady=2)
                    row.append(entry)
                self.inverse_entries.append(row)
            
           
            ttk.Button(self.inverse_matrix_frame, text="Calcular Inversa", 
                    command=self.calculate_inverse).grid(row=n, columnspan=n, pady=10)

        def calculate_inverse(self):
            try:
                n = len(self.inverse_entries)
                matrix = []
                for i in range(n):
                    row = []
                    for j in range(n):
                        value = Fraction(self.inverse_entries[i][j].get())
                        row.append(float(value))
                    matrix.append(row)
                
                matrix = np.array(matrix)
                det = np.linalg.det(matrix)
                
                if abs(det) < 1e-10:
                    messagebox.showerror("Error", "La matriz no es invertible (determinante = 0)")
                    return
                
                inverse = np.linalg.inv(matrix)
                
                
                for widget in self.inverse_result_frame.winfo_children():
                    widget.destroy()
                
                ttk.Label(self.inverse_result_frame, text="Matriz Inversa:").grid(row=0, columnspan=n)
                
                for i in range(n):
                    for j in range(n):
                        value = Fraction.from_float(inverse[i][j]).limit_denominator()
                        ttk.Label(self.inverse_result_frame, 
                                text=str(value)).grid(row=i+1, column=j, padx=2, pady=2)
            
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese números válidos")
            except np.linalg.LinAlgError:
                messagebox.showerror("Error", "Error al calcular la inversa")

        def create_multiply_matrices(self):
            m = int(self.mult_dim_m.get())
            n = int(self.mult_dim_n.get())
            p = int(self.mult_dim_p.get())
            
            
            for frame in [self.mult_matrix_a_frame, self.mult_matrix_b_frame, 
                        self.mult_result_frame]:
                for widget in frame.winfo_children():
                    widget.destroy()
            
            
            ttk.Label(self.mult_matrix_a_frame, text="Matriz A:").grid(row=0, columnspan=n)
            self.mult_entries_a = []
            for i in range(m):
                row = []
                for j in range(n):
                    entry = ttk.Entry(self.mult_matrix_a_frame, width=8)
                    entry.grid(row=i+1, column=j, padx=2, pady=2)
                    row.append(entry)
                self.mult_entries_a.append(row)
            
            
            ttk.Label(self.mult_matrix_b_frame, text="Matriz B:").grid(row=0, columnspan=p)
            self.mult_entries_b = []
            for i in range(n):
                row = []
                for j in range(p):
                    entry = ttk.Entry(self.mult_matrix_b_frame, width=8)
                    entry.grid(row=i+1, column=j, padx=2, pady=2)
                    row.append(entry)
                self.mult_entries_b.append(row)
            
           
            ttk.Button(self.mult_matrix_b_frame, text="Multiplicar", 
                    command=self.multiply_matrices).grid(row=n+1, columnspan=p, pady=10)

        def multiply_matrices(self):
            try:
               
                m = len(self.mult_entries_a)
                n = len(self.mult_entries_a[0])
                p = len(self.mult_entries_b[0])
                
                
                matrix_a = []
                matrix_b = []
                
                for i in range(m):
                    row = []
                    for j in range(n):
                        value = Fraction(self.mult_entries_a[i][j].get())
                        row.append(float(value))
                    matrix_a.append(row)
                
                for i in range(n):
                    row = []
                    for j in range(p):
                        value = Fraction(self.mult_entries_b[i][j].get())
                        row.append(float(value))
                    matrix_b.append(row)
                
                
                result = np.dot(np.array(matrix_a), np.array(matrix_b))
                
              
                for widget in self.mult_result_frame.winfo_children():
                    widget.destroy()
                
                ttk.Label(self.mult_result_frame, text="Resultado:").grid(row=0, columnspan=p)
                
                for i in range(m):
                    for j in range(p):
                        value = Fraction.from_float(result[i][j]).limit_denominator()
                        ttk.Label(self.mult_result_frame, 
                                text=str(value)).grid(row=i+1, column=j, padx=2, pady=2)
            
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese números válidos")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        def create_equation_inputs(self):
        
            for frame in [self.system_equations_frame, self.system_result_frame, self.graph_frame]:
                for widget in frame.winfo_children():
                    widget.destroy()
        
            n = int(self.system_dim.get())
            self.equation_entries = []
        
        
            ttk.Label(self.system_equations_frame, 
                    text="Ingrese las ecuaciones").pack(pady=5)
        
            for i in range(n):
                frame = ttk.Frame(self.system_equations_frame)
                frame.pack(pady=5)
                ttk.Label(frame, text=f"Ecuación {i+1}:").pack(side=tk.LEFT, padx=5)
                entry = ttk.Entry(frame, width=30)
                entry.pack(side=tk.LEFT, padx=5)
                self.equation_entries.append(entry)
            
            
                if i == 0:
                    entry.insert(0, "x + y = 2")
                elif i == 1:
                    entry.insert(0, "2x + 3y = 5")
        
    
            ttk.Button(self.system_equations_frame, text="Resolver", 
                    command=self.parse_and_solve_system).pack(pady=10)


        def parse_equation(self, equation_str):
            """Parsea una ecuación en formato texto a coeficientes."""
            try:
               
                equation_str = equation_str.lower().replace(" ", "")
                
                
                if '=' not in equation_str:
                    raise ValueError("La ecuación debe contener un signo '='")
                    
                
                left_side, right_side = equation_str.split("=")
                
               
                try:
                    constant = float(right_side)
                except ValueError:
                    raise ValueError(f"El lado derecho '{right_side}' debe ser un número")
                
                
                coefficients = {'x': 0, 'y': 0, 'z': 0}
                
                
                if not left_side.startswith('+') and not left_side.startswith('-'):
                    left_side = '+' + left_side
                    
                
                import re
               
                terms = re.findall(r'[+-](?:\d*\.)?\d*[xyz]?', left_side)
                
                for term in terms:
                    
                    sign = 1 if term[0] == '+' else -1
                    
                    term = term[1:]
                    
                   
                    if term == '':
                        continue
                    elif term == 'x':
                        coefficients['x'] += sign * 1
                    elif term == 'y':
                        coefficients['y'] += sign * 1
                    elif term == 'z':
                        coefficients['z'] += sign * 1
                    else:
                        
                        var = None
                        if term.endswith('x'): var = 'x'
                        elif term.endswith('y'): var = 'y'
                        elif term.endswith('z'): var = 'z'
                        
                        if var:
                            
                            coef = term[:-1]
                            if coef == '': coef = '1'
                            coefficients[var] += sign * float(coef)
                
                return list(coefficients.values()), constant
                
            except Exception as e:
                raise ValueError(f"Error al parsear la ecuación '{equation_str}': {str(e)}")

        def parse_and_solve_system(self):
            try:
                n = len(self.equation_entries)
                A = []
                b = []
                
              
                for entry in self.equation_entries:
                    coeffs, constant = self.parse_equation(entry.get())
                    A.append(coeffs[:n]) 
                    b.append(constant)
                
             
                A = np.array(A)
                b = np.array(b)
                
                
                method = self.method_var.get()
                if method == "gauss":
                    solution = self.solve_gauss_jordan(A, b)
                else:
                    solution = self.solve_cramer(A, b)
                
                
                self.display_solution(solution)
                if not isinstance(solution, str):
                    self.plot_system(A, b, solution)
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error al resolver el sistema: {str(e)}")

        def display_solution(self, solution):
            for widget in self.system_result_frame.winfo_children():
                widget.destroy()
            
            if isinstance(solution, str):
                ttk.Label(self.system_result_frame, text=solution).pack(pady=10)
            else:
                ttk.Label(self.system_result_frame, text="Solución:").pack(pady=5)
                variables = ['x', 'y', 'z']
                for i, value in enumerate(solution):
                    frac_value = Fraction.from_float(value).limit_denominator()
                    ttk.Label(self.system_result_frame, 
                            text=f"{variables[i]} = {frac_value}").pack()


        def solve_gauss_jordan(self, A, b):
                try:
                    n = len(A)
                    augmented = np.column_stack((A, b))
                    rank_A = np.linalg.matrix_rank(A)
                    rank_aug = np.linalg.matrix_rank(augmented)
                    
                    if rank_A < rank_aug:
                        return "El sistema no tiene solución"
                    elif rank_A < n:
                        return "El sistema tiene infinitas soluciones"
                    else:
                        
                        solution = np.linalg.solve(A, b)
                        return solution
                except np.linalg.LinAlgError:
                    return "El sistema no tiene solución única"

        def solve_cramer(self, A, b):
                try:
                    n = len(A)
                    det_A = np.linalg.det(A)
                    
                    if abs(det_A) < 1e-10:
                        return "No se puede aplicar el método de Cramer (determinante = 0)"
                    
                    solution = []
                    for i in range(n):
                        
                        Ai = A.copy()
                        Ai[:, i] = b
                        det_Ai = np.linalg.det(Ai)
                        xi = det_Ai / det_A
                        solution.append(xi)
                    
                    return np.array(solution)
                except np.linalg.LinAlgError:
                    return "Error al calcular la solución por el método de Cramer"

        def plot_system(self, A, b, solution):
            for widget in self.graph_frame.winfo_children():
                widget.destroy()
            
            n = len(A)
            fig = plt.Figure(figsize=(6, 6))
            
            if n == 2:
               
                ax = fig.add_subplot(111)
                x = np.linspace(-10, 10, 100)
                
                for i in range(2):
                    if abs(A[i,1]) < 1e-10:  
                        if abs(A[i,0]) < 1e-10:
                            continue
                        x_val = b[i]/A[i,0]
                        ax.axvline(x=x_val, label=f'Ecuación {i+1}')
                    else:
                        y = (-A[i,0]*x - b[i]) / A[i,1]
                        ax.plot(x, y, label=f'Ecuación {i+1}')
                
                if not isinstance(solution, str):
                    ax.plot(solution[0], solution[1], 'ro', label='Solución')
                
                ax.grid(True)
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.legend()
                ax.set_title('Sistema de ecuaciones 2x2')
                
            elif n == 3:
                
                ax = fig.add_subplot(111, projection='3d')
                x = y = np.linspace(-10, 10, 30)
                X, Y = np.meshgrid(x, y)
                
                for i in range(3):
                    if abs(A[i,2]) > 1e-10:  
                        Z = (-A[i,0]*X - A[i,1]*Y - b[i]) / A[i,2]
                        surf = ax.plot_surface(X, Y, Z, alpha=0.3, label=f'Ecuación {i+1}')
                        surf._facecolors2d = surf._facecolor3d
                        surf._edgecolors2d = surf._edgecolor3d
                
                if not isinstance(solution, str):
                    ax.scatter(solution[0], solution[1], solution[2], color='red', s=100, label='Solución')
                
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')
                ax.set_title('Sistema de ecuaciones 3x3')
            
            canvas = FigureCanvasTkAgg(fig, self.graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

    
    root = tk.Tk()
    app = MatrixCalculator(root)
    root.mainloop()

    