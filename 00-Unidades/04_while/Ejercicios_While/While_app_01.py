import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        
        #ANTES DEL WHILE
        iteraciones = 0

        #Informe A- Cuál fue el sexo menos ingresado (F o M)
        contador_M = 0
        contador_F = 0

        #Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0

        #Informe E- El promedio de peso de todas las mascotas
        acumulador_peso = 0

        #Nombre
        #Tipo (gato ,perro o exotico)
        #Peso ( entre 10 y 80)
        #Sexo( F o M  )
        # Edad(mayor a 0)
        #DURANTE EL WHILE
        while iteraciones < 5:
            nombre = prompt("Nombre", "Ingrese el nombre de su mascota")
            while nombre == None or nombre == "":
                nombre = prompt("Nombre", "Ingrese un nombre correcto")

            tipo = prompt("Tipo de mascota", "Ingrese su tipo de mascota")
            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt("Tipo de mascota", "Ingrese un tipo de mascota correcto")

            #Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
            match tipo:
                case "gato":
                    contador_gato += 1
                case "perro":
                    contador_perro += 1
                case "exotico":
                    contador_exotico += 1

            peso = prompt("Peso", "Ingrese el peso de su mascota")
            peso = int(peso)
            while peso < 10 or peso > 80:
                peso = prompt("Peso", "Ingrese un peso correcto")
                peso = int(peso)
            
            #Informe E- El promedio de peso de todas las mascotas
            acumulador_peso += peso

            #Informe C- El nombre y tipo de la mascota menos pesada
            if iteraciones == 0 or menos_peso > peso:
                menos_peso = peso
                tipo_menos_peso = tipo
                nombre_menos_peso = nombre

            sexo = prompt("Sexo", "Ingrese el sexo de su mascota")
            while sexo != "F" and sexo != "M":
                sexo = prompt("Sexo", "Ingrese un sexo correcto")

            #Informe A- Cuál fue el sexo menos ingresado (F o M)
                if sexo == "M":
                    contador_M += 1
                else:
                    contador_F += 1

            edad = prompt("Edad", "Ingrese la edad de su mascota")
            while int(edad) <= 0:
                edad = prompt("Edad", "Ingrese una edad correcta")
                edad = int(edad)

            #Informe D- El nombre del perro más joven
            if iteraciones == 0 or edad_menor_perro > edad and tipo == "perro":
                edad_menor_perro = edad
                nombre_perro_joven = nombre

            iteraciones += 1

        #DESPUES DEL WHILE
        #Informe A- Cuál fue el sexo menos ingresado (F o M)
        if contador_M < contador_F:
            mensaje = f"El sexo menos ingresado fue el Masculino\n"
        else:
            mensaje = f"El sexo menos ingresado fue el Femenino\n"

        #Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
        porcentaje_gato = (contador_gato * 100) / iteraciones
        porcentaje_perro = (contador_perro * 100) / iteraciones
        porcentaje_exotico = (contador_exotico * 100) / iteraciones

        mensaje += f"El porcentaje de mascotas que hay por cada tipo es:\n -{porcentaje_gato}% de gatos\n -{porcentaje_perro}% de perros\n -{porcentaje_exotico}% de exoticos\n"

        #Informe C- El nombre y tipo de la mascota menos pesada
        mensaje += f"El nombre de las mascota menos pesada es {nombre_menos_peso} y su tipo es {tipo_menos_peso}\n"

        #Informe D- El nombre del perro más joven
        mensaje += f"El nombre del perro mas joven es {nombre_perro_joven}\n"

        #Informe E- El promedio de peso de todas las mascotas
        promedio_peso = acumulador_peso / iteraciones
        mensaje += f"El promedio de peso de todas las mascotas es {promedio_peso}"

        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()