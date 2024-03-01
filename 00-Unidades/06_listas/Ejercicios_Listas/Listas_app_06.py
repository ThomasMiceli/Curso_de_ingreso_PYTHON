import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class Bolsa:
    def __init__(self):
        self.operaciones = []

    def agregar_operacion(self, nombre, monto, tipo_instrumento, cantidad):
        if monto < 10000:
            print("El monto de la operación debe ser mayor o igual a $10000")
            return
        if cantidad < 0:
            print("La cantidad de instrumentos debe ser mayor o igual a 0")
            return
        self.operaciones.append({
            "nombre": nombre,
            "monto": monto,
            "tipo_instrumento": tipo_instrumento,
            "cantidad": cantidad
        })

    def informe_1(self):
        df = pd.DataFrame(self.operaciones)
        min_operaciones = df["tipo_instrumento"].value_counts().min()
        tipo_instrumento_menos_operado = df["tipo_instrumento"].value_counts().idxmin()
        print(f"El tipo de instrumento que menos se operó en total es {tipo_instrumento_menos_operado} con {min_operaciones} operaciones.")

    def informe_2(self):
        df = pd.DataFrame(self.operaciones)
        usuarios_compraron_MEP = df[(df["tipo_instrumento"] == "MEP") & (df["monto"] >= 50000) & (df["monto"] <= 200000)]["nombre"].nunique()
        print(f"{usuarios_compraron_MEP} usuarios compraron entre 50 y 200 MEP.")

    def informe_3(self):
        df = pd.DataFrame(self.operaciones)
        usuarios_no_compraron_CEDEAR = df[df["tipo_instrumento"] != "CEDEAR"]["nombre"].nunique()
        print(f"{usuarios_no_compraron_CEDEAR} usuarios no compraron CEDEAR.")

    def informe_4(self):
        df = pd.DataFrame(self.operaciones)
        usuario_compro_BONOS_CEDEAR = df[(df["tipo_instrumento"] == "BONOS") | (df["tipo_instrumento"] == "CEDEAR")]
        if not usuario_compro_BONOS_CEDEAR.empty:
            nombre_inversion = usuario_compro_BONOS_CEDEAR.iloc[0]["nombre"]
            cantidad_invertida = usuario_compro_BONOS_CEDEAR["monto"].sum()
            print(f"El nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR es {nombre_inversion} con ${cantidad_invertida}.")
        else:
            print("No hay usuarios que hayan comprado BONOS o CEDEAR.")

    def informe_5(self):
        df = pd.DataFrame(self.operaciones)
        usuario_invertio_menos_dinero = df[df["monto"] == df["monto"].min()]["nombre"].iloc[0]
        posicion_usuario = df[df["nombre"] == usuario_invertio_menos_dinero].index[0]
        print(f"El nombre y posición del usuario que invirtió menos dinero es {usuario_invertio_menos_dinero} en la posición {posicion_usuario}.")

    def informe_6(self):
        df = pd.DataFrame(self.operaciones)
        promedio_dinero_CEDEAR = df[df["tipo_instrumento"] == "CEDEAR"]["monto"].mean()
        print(f"El promedio de dinero en CEDEAR ingresado en total es ${promedio_dinero_CEDEAR}.")
