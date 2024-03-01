import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

#De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos
#Marca (no validar)
#Categoría (peligroso, comestible, indumentaria)
#Peso ( entre 100 y 800)
#Tipo de material ( aluminio, hierro , madera)
#Costo en $ (mayor a 0)
#Pedir datos por prompt y mostrar por print, se debe informar:
#Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
#Informe B- El porcentaje de contenedores de Categoría peligroso
#Informe C- La marca y tipo del contenedor más pesado
#Informe D- La marca del contenedor de comestible con menor costo
#Informe E- El promedio de costo de todos los contenedores de HIerro


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
        iteracion = 0
        contador_aluminio = 0
        contador_hierro = 0
        contador_madera = 0
        categoria_peligroso = 0
        acumulador_costo_hierro = 0
        acumulador_peso = 0
        
        while iteracion < 20:
            
            marca = prompt('Marca', 'Ingrese el nombre de su marca')
            while marca == None:
                marca = prompt('Marca', 'Ingrese una marca correcta')

            categoria = prompt('Categoria', 'Ingrese un tipo de categoria correcta')
            while categoria != 'peligroso' and categoria != 'comestible' and categoria != 'indumentaria':
                categoria = prompt('Categoria', 'Ingrese un tipo de categoria correcta')
            if categoria == 'peligroso':
                categoria_peligroso += 1

            peso = prompt('Peso', 'Ingrese el peso de su mascota')
            peso = int(peso)
            while peso < 100 or peso > 800:
                peso = prompt('Peso', 'Ingrese un peso correcto')
                peso = int(peso)

            acumulador_peso += peso

            if iteracion == 0 or peso > peso_mayor:
                peso_mayor = peso
                marca_mayor = marca
                tipo_mayor = tipo_de_material

            tipo_de_material = prompt('Material', 'Ingrese el tipo de material')
            while tipo_de_material != 'aluminio' and tipo_de_material != 'hierro' and tipo_de_material != 'madera':
                tipo_de_material = prompt('Material', 'Reingrese el tipo de material')
            
            match (tipo_de_material):
                case "aluminio":
                    contador_aluminio += 1
                case "hierro":
                    contador_hierro += 1
                case "madera":
                    contador_madera += 1

            costo = prompt('Costo', 'Ingrese el costo')
            while costo < 0:
                costo = prompt('Costo', 'Reingrese el costo')
                if (iteracion == 0 or costo < costo_menor_comestible) and marca == 'comestible':
                    costo_menor_comestible = costo
                    marca_menor_comestible = marca
            
            acumulador_costo_hierro += costo

            

        iteracion += 1


        
        if contador_hierro > contador_madera and contador_hierro > contador_aluminio:
            material_mas_usado = 'hierro'
        elif contador_madera > contador_aluminio:
            material_mas_usado = 'madera'
        else: 
            material_mas_usado = 'aluminio'

        if contador_hierro > 0:
            promedio_hierro_costo = acumulador_costo_hierro / contador_hierro
        else:
            promedio_hierro_costo = 'No se pudo calcular el promedio. No ingreso contenedores de hierro'

        porcentaje_categoria_p = (categoria_peligroso * 100) / iteracion

    
        print (f'#Informe A. El tipo de material mas usado fue el {material_mas_usado}')
        print (f'#Informe B. El porcentaje de contenedores de categoria peligroso son %{porcentaje_categoria_p}')
        print (f'#Informe C. la marca del contenedor mas pesado es {marca_mayor} y el tipo de contenedor mas pesado es {tipo_mayor}')
        print (f'#Informe D. la marca de menor costo de los contenedores comestibles es {marca_menor_comestible}')
        print (f'#Informe E. el promedio de costo de los contenedores de hierro es {promedio_hierro_costo}')

            
