import tkinter as tk


root = tk.Tk()
root.geometry("300x300")
root.title("Calculadora con Python")







root.mainloop()











Numero1 = float(input("Introduce el primer numero: "))
Numero2 = float(input("Introduce el segundo numero: "))
Operacion = input("¿Que operación quieres hacer? ")

if Operacion == "sumar":
    suma = Numero1 + Numero2
    print("La suma es : ", suma)

if Operacion == "restar":
    resta = Numero1 - Numero2
    print("La resta es : ", resta)

if Operacion == "multiplicar":
    resultado = Numero1 * Numero2
    print("La multiplicacion es : ", resultado)

if Operacion == "dividir":
    resultado = Numero1 / Numero2
    print("La division es : ", resultado)

if Operacion == "fraccionar":
    resultado = Numero1 / Numero2
    resultado = Numero1 + Numero2
    print("La modulo es : ", resultado)

if Operacion == "elevalo":
    resultado = Numero1 ** Numero2
    print("La exponencial es : ", resultado)
