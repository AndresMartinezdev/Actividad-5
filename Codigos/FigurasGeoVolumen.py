import tkinter as tk
from tkinter import messagebox
import math

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("400x200")

        tk.Label(self, text="Seleccione una figura", font=("Arial", 14)).pack(pady=10)

        tk.Button(self, text="Cilindro", command=self.abrir_cilindro).pack(pady=5)
        tk.Button(self, text="Esfera", command=self.abrir_esfera).pack(pady=5)
        tk.Button(self, text="Pirámide", command=self.abrir_piramide).pack(pady=5)

    def abrir_cilindro(self):
        CilindroGUI(self)

    def abrir_esfera(self):
        EsferaGUI(self)

    def abrir_piramide(self):
        PiramideGUI(self)

class CilindroGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("300x250")

        tk.Label(self, text="Radio (cms):").pack()
        self.radio = tk.Entry(self)
        self.radio.pack()

        tk.Label(self, text="Altura (cms):").pack()
        self.altura = tk.Entry(self)
        self.altura.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=5)
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        try:
            r = float(self.radio.get())
            h = float(self.altura.get())
            volumen = math.pi * r**2 * h
            superficie = 2 * math.pi * r * (r + h)
            self.resultado.config(text=f"Volumen: {volumen:.2f} cm³\nSuperficie: {superficie:.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

class EsferaGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("300x200")

        tk.Label(self, text="Radio (cms):").pack()
        self.radio = tk.Entry(self)
        self.radio.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=5)
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        try:
            r = float(self.radio.get())
            volumen = (4/3) * math.pi * r**3
            superficie = 4 * math.pi * r**2
            self.resultado.config(text=f"Volumen: {volumen:.2f} cm³\nSuperficie: {superficie:.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

class PiramideGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("300x250")

        tk.Label(self, text="Base (cms):").pack()
        self.base = tk.Entry(self)
        self.base.pack()

        tk.Label(self, text="Altura (cms):").pack()
        self.altura = tk.Entry(self)
        self.altura.pack()

        tk.Label(self, text="Apotema (cms):").pack()
        self.apotema = tk.Entry(self)
        self.apotema.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=5)
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        try:
            b = float(self.base.get())
            h = float(self.altura.get())
            a = float(self.apotema.get())
            volumen = (1/3) * b**2 * h
            superficie = b**2 + 2 * b * a
            self.resultado.config(text=f"Volumen: {volumen:.2f} cm³\nSuperficie: {superficie:.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()