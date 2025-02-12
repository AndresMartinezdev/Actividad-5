import tkinter as tk
from tkinter import messagebox
import statistics

class Notas:
    def __init__(self):
        self.listaNotas = []
    
    def calcularPromedio(self):
        return statistics.mean(self.listaNotas) if self.listaNotas else 0
    
    def calcularDesviacion(self):
        return statistics.stdev(self.listaNotas) if len(self.listaNotas) > 1 else 0
    
    def calcularMayor(self):
        return max(self.listaNotas) if self.listaNotas else 0
    
    def calcularMenor(self):
        return min(self.listaNotas) if self.listaNotas else 0

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        
        self.notas = Notas()
        self.entradas = []
        
        for i in range(5):
            tk.Label(root, text=f"Nota {i+1}:").grid(row=i, column=0, padx=5, pady=5)
            entrada = tk.Entry(root)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas.append(entrada)
        
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.grid(row=5, column=0, columnspan=2, pady=5)
        
        tk.Button(root, text="Calcular", command=self.calcular).grid(row=6, column=0, pady=5)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=6, column=1, pady=5)
    
    def calcular(self):
        try:
            self.notas.listaNotas = [float(entrada.get()) for entrada in self.entradas]
            promedio = self.notas.calcularPromedio()
            desviacion = self.notas.calcularDesviacion()
            valor_max = self.notas.calcularMayor()
            valor_min = self.notas.calcularMenor()
            
            resultado = (f"Promedio = {promedio:.2f}\n"
                         f"Desviación estándar = {desviacion:.2f}\n"
                         f"Valor mayor = {valor_max:.1f}\n"
                         f"Valor menor = {valor_min:.1f}")
            self.resultado_label.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
    
    def limpiar(self):
        for entrada in self.entradas:
            entrada.delete(0, tk.END)
        self.resultado_label.config(text="")

def main():
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()