import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import os
import csv


# Función para actualizar las opciones del Combobox de autocompletado
def actualizar_completado(event):
    texto = entrada_combobox.get().lower()  # Obtener el texto que el usuario escribió
    lista_completada = [opcion for opcion in opciones1 if texto in opcion.lower()]  # Filtrar opciones
    combobox['values'] = lista_completada  # Actualizar las opciones del combobox
    if lista_completada:
        combobox.current(0)  # Establecer la primera opción si hay coincidencias


def guardar_datos():
    # Obtener los valores de los inputs
    fecha = fecha_var.get()
    numero_orden = numero_orden_var.get()
    referencia = referencia_var.get()
    pxcm = pxcm_var.get()
    inicio = inicio_var.get()
    final = final_var.get()
    tejedor = tejedor_var.get()
    causa = causa_var.get()
    numero_maquina = maquina_var.get()

    # Validar los números
    try:
        pxcm = float(pxcm)
        inicio = float(inicio)
        final = float(final)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")
        return

    # Nombre del archivo CSV
    archivo_csv = 'datos.csv'

    # Verificar si el archivo existe y agregar un encabezado si es necesario
    archivo_existe = os.path.isfile(archivo_csv)

    with open(archivo_csv, 'a', newline='') as file:
        writer = csv.writer(file)

        # Si el archivo no existe, agregar un encabezado
        if not archivo_existe:
            writer.writerow(['Fecha', 'Número de Orden', 'Referencia', 'PXCM', 'Inicio', 'Final', 'Tejedor', 'Causa', 'Número de Máquina'])

        # Escribir los datos en el archivo CSV
        writer.writerow([fecha, numero_orden, referencia, pxcm, inicio, final, tejedor, causa, numero_maquina])

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "Datos guardados correctamente.")

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Datos")

# Variables para almacenar los valores seleccionados
fecha_var = tk.StringVar()
numero_orden_var = tk.StringVar()
referencia_var = tk.StringVar()
pxcm_var = tk.StringVar()
inicio_var = tk.StringVar()
final_var = tk.StringVar()
tejedor_var = tk.StringVar()
causa_var = tk.StringVar()
maquina_var = tk.StringVar()

# Configuración de la interfaz

# Etiqueta para la fecha
etiqueta_fecha = tk.Label(root, text="Fecha (YYYY-MM-DD):")
etiqueta_fecha.grid(row=0, column=0, padx=10, pady=10)

# Entrada de fecha (Entry)
fecha_entry = tk.Entry(root, textvariable=fecha_var)
fecha_entry.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta para número de orden
etiqueta_numero_orden = tk.Label(root, text="Número de Orden:")
etiqueta_numero_orden.grid(row=1, column=0, padx=10, pady=10)

# Entrada de número de orden
numero_orden_entry = tk.Entry(root, textvariable=numero_orden_var)
numero_orden_entry.grid(row=1, column=1, padx=10, pady=10)



# Etiqueta para referencia
etiqueta_referencia = tk.Label(root, text="Referencia:")
etiqueta_referencia.grid(row=2, column=0, padx=10, pady=10)



# Lista de opciones para el autocompletado
opciones1 = [
"Cordon cp",

"Cordon berlin"
"Filato 2",
"Filato 2.5",
"Filato 3",
"Filato 3.5",
"Filato 4",
"Filato 4.5",
"Filato 5",
"Filato 5.5"


]

# Ordenar las opciones de autocompletado
opciones1 = sorted(opciones1, key=lambda x: x.lower())

# Crear el Entry para el autocompletado
entrada_combobox = tk.Entry(root)
entrada_combobox.grid(row=2, column=1, padx=10, pady=10)

# Crear el Combobox para autocompletado
combobox = ttk.Combobox(root, textvariable=referencia_var, values=opciones1)
combobox.grid(row=2, column=3, padx=10, pady=10)

# Vincular la función de autocompletado al evento de escritura en el Entry
entrada_combobox.bind('<KeyRelease>', actualizar_completado)


# Etiqueta para pxcm
etiqueta_pxcm = tk.Label(root, text="PXCM:")
etiqueta_pxcm.grid(row=3, column=0, padx=10, pady=10)

# Entrada de pxcm
pxcm_entry = tk.Entry(root, textvariable=pxcm_var)
pxcm_entry.grid(row=3, column=1, padx=10, pady=10)

# Etiqueta para inicio
etiqueta_inicio = tk.Label(root, text="Inicio:")
etiqueta_inicio.grid(row=4, column=0, padx=10, pady=10)

# Entrada de inicio
inicio_entry = tk.Entry(root, textvariable=inicio_var)
inicio_entry.grid(row=4, column=1, padx=10, pady=10)

# Etiqueta para final
etiqueta_final = tk.Label(root, text="Final:")
etiqueta_final.grid(row=5, column=0, padx=10, pady=10)

# Entrada de final
final_entry = tk.Entry(root, textvariable=final_var)
final_entry.grid(row=5, column=1, padx=10, pady=10)

# Etiqueta para tejedor
etiqueta_tejedor = tk.Label(root, text="Tejedor:")
etiqueta_tejedor.grid(row=6, column=0, padx=10, pady=10)

# Opciones de tejedor
opciones_tejedor = ["ANGEL", "KEVIN", "STEVEN", "ALEX", "JULIO", "EDUARDO", "KATERINE", "JEIMY", "FEDERICO", "EDWIN", "FERNANDO", "ROBERTO"]

# Crear el Combobox para el tejedor
tejedor_menu = ttk.Combobox(root, textvariable=tejedor_var, values=opciones_tejedor)
tejedor_var.set(opciones_tejedor[0])  # Establecer valor por defecto
tejedor_menu.grid(row=6, column=1, padx=10, pady=10)

# Etiqueta para causa
etiqueta_causa = tk.Label(root, text="Causa/Motivo:")
etiqueta_causa.grid(row=7, column=0, padx=10, pady=10)

# Opciones de causa
opciones_causa = ["Rotura de Hilo", "Falta de Material", "Parada de Máquina", "Mantenimiento", "Problema Técnico"]

# Crear el Combobox para la causa
causa_menu = ttk.Combobox(root, textvariable=causa_var, values=opciones_causa)
causa_var.set(opciones_causa[0])  # Establecer valor por defecto
causa_menu.grid(row=7, column=1, padx=10, pady=10)

# Etiqueta para número de máquina
etiqueta_maquina = tk.Label(root, text="Número de Máquina:")
etiqueta_maquina.grid(row=8, column=0, padx=10, pady=10)

# Opciones de máquina
opciones_maquina = ["Máquina 1", "Máquina 2", "Máquina 3", "Máquina 4", "Máquina 5"]

# Crear el Combobox para el número de máquina
maquina_menu = ttk.Combobox(root, textvariable=maquina_var, values=opciones_maquina)
maquina_var.set(opciones_maquina[0])  # Establecer valor por defecto
maquina_menu.grid(row=8, column=1, padx=10, pady=10)

# Botón para guardar los datos
boton_guardar = tk.Button(root, text="Guardar Datos", command=guardar_datos)
boton_guardar.grid(row=9, column=0, columnspan=2, pady=20)

# Ejecutar la interfaz gráfica
root.mainloop()
