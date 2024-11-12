# Función para actualizar las opciones del combobox mientras escribimos
import tkinter as tk
from tkinter import ttk


def actualizar_completado(event):
    texto = entrada_combobox.get().lower()  # Obtener el texto que el usuario escribió
    lista_completada = [opcion for opcion in opciones if texto in opcion.lower()]  # Filtrar opciones
    combobox['values'] = lista_completada  # Actualizar las opciones del combobox
    if lista_completada:
        combobox.current(0)  # Establecer la primera opción si hay coincidencias

# Crear la ventana principal
root = tk.Tk()
root.title("Autocompletado en Combobox")

# Lista de opciones
opciones = ["Apple", "Banana", "Cherry", "Date", "Grapes", "Kiwi", "Mango","Mafffngo", "Orange", "Peach", "Pear"]

# Crear el Entry para el autocompletado
entrada_combobox = tk.Entry(root)
entrada_combobox.pack(padx=10, pady=10)

# Crear el Combobox
combobox = ttk.Combobox(root, state="readonly", values=opciones)
combobox.pack(padx=10, pady=10)

# Vincular la función de autocompletado al evento de escritura en el Entry
entrada_combobox.bind('<KeyRelease>', actualizar_completado)

# Ejecutar la interfaz gráfica
root.mainloop()