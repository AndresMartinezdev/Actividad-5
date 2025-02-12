import tkinter as tk
from tkinter import messagebox
import statistics

class NotasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        
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
            notas = [float(entrada.get()) for entrada in self.entradas]
            promedio = statistics.mean(notas)
            desviacion = statistics.stdev(notas) if len(notas) > 1 else 0
            valor_max = max(notas)
            valor_min = min(notas)
            
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

if __name__ == "__main__":
    root = tk.Tk()
    app = NotasApp(root)
    root.mainloop()
