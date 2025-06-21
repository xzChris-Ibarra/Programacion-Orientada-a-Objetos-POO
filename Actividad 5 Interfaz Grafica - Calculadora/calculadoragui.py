import tkinter as tk
from tkinter import messagebox

#Funciones para operaciones
def obtener_numeros():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        return num1, num2
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")
        return None, None

def sumar():
    num1, num2 = obtener_numeros()
    if num1 is not None:
        resultado.set(str(num1 + num2))

def restar():
    num1, num2 = obtener_numeros()
    if num1 is not None:
        resultado.set(str(num1 - num2))

def multiplicar():
    num1, num2 = obtener_numeros()
    if num1 is not None:
        resultado.set(str(num1 * num2))

def dividir():
    num1, num2 = obtener_numeros()
    if num1 is not None:
        if num2 == 0:
            messagebox.showwarning("Advertencia", "No se puede dividir entre cero.")
        else:
            resultado.set(str(num1 / num2))

def borrar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.set("")

#Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("400x300")
ventana.configure(bg="#f0f8ff")

#Variables
resultado = tk.StringVar()

#Widgets
tk.Label(ventana, text="Primer número", bg="#ffebcd").place(x=30, y=30)
entrada1 = tk.Entry(ventana, bg="#fffacd")
entrada1.place(x=150, y=30, width=200)

tk.Label(ventana, text="Segundo número", bg="#ffebcd").place(x=30, y=70)
entrada2 = tk.Entry(ventana, bg="#fffacd")
entrada2.place(x=150, y=70, width=200)

tk.Label(ventana, text="Resultado", bg="#ffebcd").place(x=30, y=110)
tk.Entry(ventana, textvariable=resultado, bg="#e0ffff", state="readonly").place(x=150, y=110, width=200)

#Botones de operaciones
tk.Button(ventana, text="Sumar", bg="#90ee90", command=sumar).place(x=50, y=160, width=70)
tk.Button(ventana, text="Restar", bg="#ffa07a", command=restar).place(x=130, y=160, width=70)
tk.Button(ventana, text="Multiplicar", bg="#add8e6", command=multiplicar).place(x=210, y=160, width=80)
tk.Button(ventana, text="Dividir", bg="#d8bfd8", command=dividir).place(x=300, y=160, width=70)

#Botón para borrar
tk.Button(ventana, text="Borrar", bg="#f08080", command=borrar).place(x=160, y=210, width=80)

ventana.mainloop()
