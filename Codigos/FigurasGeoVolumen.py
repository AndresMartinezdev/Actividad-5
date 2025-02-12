import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0
    
    def setVolumen(self, volumen):
        self.volumen = volumen
    
    def setSuperficie(self, superficie):
        self.superficie = superficie
    
    def getVolumen(self):
        return self.volumen
    
    def getSuperficie(self):
        return self.superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.calcularVolumen()
        self.calcularSuperficie()
    
    def calcularVolumen(self):
        self.setVolumen(math.pi * self.radio**2 * self.altura)
    
    def calcularSuperficie(self):
        self.setSuperficie(2 * math.pi * self.radio * (self.radio + self.altura))

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.calcularVolumen()
        self.calcularSuperficie()
    
    def calcularVolumen(self):
        self.setVolumen((4/3) * math.pi * self.radio**3)
    
    def calcularSuperficie(self):
        self.setSuperficie(4 * math.pi * self.radio**2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.calcularVolumen()
        self.calcularSuperficie()
    
    def calcularVolumen(self):
        self.setVolumen((1/3) * self.base**2 * self.altura)
    
    def calcularSuperficie(self):
        self.setSuperficie(self.base**2 + 2 * self.base * self.apotema)

class VentanaCilindro(tk.Toplevel):
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
            figura = Cilindro(float(self.radio.get()), float(self.altura.get()))
            self.resultado.config(text=f"Volumen: {figura.getVolumen():.2f} cm³\nSuperficie: {figura.getSuperficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

class VentanaEsfera(tk.Toplevel):
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
            figura = Esfera(float(self.radio.get()))
            self.resultado.config(text=f"Volumen: {figura.getVolumen():.2f} cm³\nSuperficie: {figura.getSuperficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

class VentanaPiramide(tk.Toplevel):
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
            figura = Piramide(float(self.base.get()), float(self.altura.get()), float(self.apotema.get()))
            self.resultado.config(text=f"Volumen: {figura.getVolumen():.2f} cm³\nSuperficie: {figura.getSuperficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("400x200")

        tk.Label(self, text="Seleccione una figura", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Cilindro", command=self.abrir_cilindro).pack(pady=5)
        tk.Button(self, text="Esfera", command=self.abrir_esfera).pack(pady=5)
        tk.Button(self, text="Pirámide", command=self.abrir_piramide).pack(pady=5)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)

class Principal:
    @staticmethod
    def ejecutar():
        app = VentanaPrincipal()
        app.mainloop()

if __name__ == "__main__":
    Principal.ejecutar()
