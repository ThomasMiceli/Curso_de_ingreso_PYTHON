import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        contador = 1
        contador_iteracion = 0
        
        
        while True:
            numero = prompt('Ingrese un número', 'Ingrese aqui')
            if numero == None or numero == '':
                break
            numeroParseado = int(numero)

            if contador == 1 or numeroParseado < numero_minimo:
                numero_minimo = numeroParseado
                contador_iteracion = contador
                contador += 1
            
            if contador == 1 or numeroParseado > numero_maximo:
                numero_maximo = numeroParseado
                contador_iteracion = contador
                contador += 1
                
                
            if numeroParseado < 0:
                suma_negativos += numeroParseado
                cantidad_negativos += 1
            elif numeroParseado > 0: 
                suma_positivos += numeroParseado
                cantidad_positivos += 1
            else:
                cantidad_ceros += 1
                
        diferencia = cantidad_positivos - cantidad_negativos

        if diferencia < 0:
            diferencia *= -1


        resultado = (
            'A. Suma acumulada de los negativos:' + str(suma_negativos) + '\n' +
            'B. Suma acumulada de los positivos:' + str(suma_positivos) + '\n' +
            'C. Cantidad de números positivos ingresados:' + str(cantidad_positivos) + '\n' +
            'D. Cantidad de números negativos ingresados:' + str(cantidad_negativos) + '\n' +
            'E. Cantidad de ceros:' + str(cantidad_ceros) + '\n' +
            'F. Diferencia entre la cantidad de los números positivos ingresados y los negativos:' + str(diferencia) + '\n' +
            'G. El valor maximo es:' + str(numero_maximo) + '\n' +
            'H. El valor minimo es:' + str(numero_minimo))
        
        alert('Resultado', resultado)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
