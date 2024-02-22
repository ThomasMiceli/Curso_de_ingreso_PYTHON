import tkinter as tk
from tkinter import filedialog

def abrir_imagen():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.png;*.gif")])
    if archivo:
        imagen = tk.PhotoImage(file=archivo)
        label_imagen.config(image=imagen)
        label_imagen.image = imagen

app = tk.Tk()
app.title("Mostrar imagen")

frame = tk.Frame(app)
frame.pack()

boton_abrir = tk.Button(frame, text="Abrir imagen", command=abrir_imagen)
boton_abrir.pack()

label_imagen = tk.Label(frame)
label_imagen.pack()

app.mainloop()
