import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime, timedelta
import os
import csv
from tkinter import messagebox
from datetime import datetime, timedelta
import os
from tkinter import messagebox
from datetime import datetime, timedelta
import os
from datetime import datetime, timedelta
from tkinter import messagebox

def guardar_datos():
    # Obtener los valores de los inputs
    opcion1_seleccionada = opcion1_var.get()
    opcion2_seleccionada = opcion2_var.get()
    numero_ingresado = numero_var.get()

    # Obtener la fecha de ayer
    ayer = datetime.now() - timedelta(days=1)

    # Formatear la fecha para mostrarla en un formato legible
    ayer_formateada = ayer.strftime('%Y-%m-%d')

    # Validar si el número es realmente un número
    try:
        numero_ingresado = float(numero_ingresado)  # Convertir a float
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido.")
        return

    # Nombre del archivo de texto
    archivo_txt = 'datos.txt'

    # Verificar si el archivo existe y agregar un encabezado si es necesario
    archivo_existe = os.path.isfile(archivo_txt)

    with open(archivo_txt, 'a') as file:
        # Si el archivo no existe, agregar un encabezado
        if not archivo_existe:
            file.write(' Referencia ,Operario, metros, Fecha\n')  # Encabezado con comas

        # Escribir los datos en el archivo (formato: Opción1, Opción2, Número, Fecha)
        file.write(f'{opcion1_seleccionada}, {opcion2_seleccionada}, {numero_ingresado}, {ayer_formateada}\n')

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "Datos guardados correctamente.")

# Función para actualizar las opciones del Combobox de autocompletado
def actualizar_completado(event):
    texto = entrada_combobox.get().lower()  # Obtener el texto que el usuario escribió
    lista_completada = [opcion for opcion in opciones1 if texto in opcion.lower()]  # Filtrar opciones
    combobox['values'] = lista_completada  # Actualizar las opciones del combobox
    if lista_completada:
        combobox.current(0)  # Establecer la primera opción si hay coincidencias


# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Datos")

# Variables para almacenar los valores seleccionados
opcion1_var = tk.StringVar()
opcion2_var = tk.StringVar()
numero_var = tk.StringVar()

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
"Filato 5.5",




"Cinta Montana 2",
"Cinta Montana 2.5",
"Cinta Montana 3",
"Cinta Montana 3.5",
"Cinta Montana 4",
"Cinta Montana 4.5",
"Cinta Montana 5",
"Cinta Montana 5.5",





"Cinta Hiladillo 1",
"Cinta Hiladillo 1.5",
"Cinta Hiladillo 2",
"Cinta Hiladillo 2.5",
"Cinta Hiladillo 3",


"Cinta Spum 3.5",
"Cinta Spum 4",

"Cinta Colmena 4",
"Cinta Danessa 4",

"Randa Napolitana 1.5",
"Randa Napolitana 2",
"Randa Napolitana 2.5",

"Montana Cocida 1",
"Montana Cocida 1.5",
"Montana Cocida 2",
"Montana Cocida 2.5",
"Montana Cocida 3",

"Fleco cuquillo N 5",
"Fleco cuquillo N 6",
"Fleco cuquillo N 7",
"Fleco cuquillo N 8",
"Fleco cuquillo N 9",
"Fleco cuquillo N 10",
"Fleco cuquillo N 11",
"Fleco cuquillo N 12",
"Fleco cuquillo N 13",
"Fleco cuquillo N 14",
"Fleco cuquillo N 15",
"Fleco cuquillo N 16",
"Fleco cuquillo N 17",
"Fleco cuquillo N 18",
"Fleco cuquillo N 19",
"Fleco cuquillo N 20",
"Fleco cuquillo N 21",
"Fleco cuquillo N 22",
"Fleco cuquillo N 23",
"Fleco cuquillo N 24",
"Fleco cuquillo N 25",
"Fleco cuquillo N 26",
"Fleco cuquillo N 27",
"Fleco cuquillo N 28",
"Fleco cuquillo N 29",
"Fleco cuquillo N 30",
"Fleco cuquillo N 31",
"Fleco cuquillo N 32",
"Fleco cuquillo N 33",
"Fleco cuquillo N 34",
"Fleco cuquillo N 35",
"Fleco cuquillo N 36",
"Fleco cuquillo N 37",
"Fleco cuquillo N 38",
"Fleco cuquillo N 39",
"Fleco cuquillo N 40",
"Fleco cuquillo N 41",
"Fleco cuquillo N 42",
"Fleco cuquillo N 43",
"Fleco cuquillo N 44",
"Fleco cuquillo N 45",
"Fleco cuquillo N 46",
"Fleco cuquillo N 47",
"Fleco cuquillo N 48",
"Fleco cuquillo N 49",
"Fleco cuquillo N 50",
"Fleco cuquillo N 51",
"Fleco cuquillo N 52",
"Fleco cuquillo N 53",
"Fleco cuquillo N 54",
"Fleco cuquillo N 55",
"Fleco cuquillo N 56",
"Fleco cuquillo N 57",
"Fleco cuquillo N 58",
"Fleco cuquillo N 59",
"Fleco cuquillo N 60",

"Fleco toño jerez N5",
"Fleco pol 5",
"Fleco pol 6",
"Fleco pol 4",
"Venessiana N 4",
"Venessiana N 8",
"Venessiana N 16",
"Randa gusanillo 2.5",
"Millare 88",
"Millare sencillo",
"Millare 10",
"Millare Afa especial",
"Randa gusanillo 2.5",
"Randa gusanillo 3.0",
"Randa gusanillo 3.5",
"Randa gusanillo 4.0",
"Randa gusanillo 4.5",
"Randa gusanillo 5.0",
"Randa gusanillo 5.5",
"Randa gusanillo 6.0",
"Randa gusanillo 6.5",
"Randa gusanillo 7.0",
"Randa gusanillo 7.5",
"Randa gusanillo 8.0",
"Randa gusanillo 8.5",
"Randa gusanillo 9.0",
"Randa gusanillo 9.5",
"Randa gusanillo 10.0",
"Randa gusanillo 10.5",
"Randa gusanillo 11.0",
"Randa gusanillo 11.5",
"Randa gusanillo 12.0",
"Randa gusanillo 12.5",
"Randa gusanillo 13.0",
"Randa gusanillo 13.5",
"Randa gusanillo 14.0",
"Randa gusanillo 14.5",
"Randa gusanillo 15.0",
"Randa gusanillo 15.5",
"Randa gusanillo 16.0",
"Randa gusanillo 16.5",
"Randa gusanillo 17.0",
"Randa gusanillo 17.5",
"Randa gusanillo 18.0",
"Randa gusanillo 18.5",
"Randa gusanillo 19.0",
"Randa gusanillo 19.5",
"Randa gusanillo 20.0",
"Randa gusanillo 20.5",
"Randa gusanillo 21.0",
"Randa gusanillo 21.5",
"Randa gusanillo 22.0",
"Randa gusanillo 22.5",
"Randa gusanillo 23.0",
"Randa gusanillo 23.5",
"Randa gusanillo 24.0",
"Randa gusanillo 24.5",
"Randa gusanillo 25.0",
"Randa gusanillo 25.5",
"Randa gusanillo 26.0",
"Randa gusanillo 26.5",
"Randa gusanillo 27.0",
"Randa gusanillo 27.5",
"Randa gusanillo 28.0",
"Randa gusanillo 28.5",
"Randa gusanillo 29.0",
"Randa gusanillo 29.5",
"Randa gusanillo 30.0",
"Ribete 4",
"Ribete 5",
"Ribete 6",
"Ribete 7",
"Ribete 8",
"Fleco 3 argollas",
"Fleco 2 argollas",
"Fleco Test",
"Millare Gaviota 1.5",
"Millare Gaviota 2",
"Millare Gaviota 2.5",
"Millare Gaviota 3",
"Millare Gaviota 3.5",
"Cinta lisa 2.5",
"Cinta lisa 3",
"Cinta lisa 3.5",
"Cinta lisa 4",

"Cinta Americana 2.5",
"Cinta Americana 3",
"Cinta Americana 3.5",
"Cinta Americana 4",

"Trensado M5 0.8",
"Trensado M5 0.9",
"Trensado M5 1.0",
"Trensado M5 1.1",
"Trensado M5 1.2",
"Trensado M5 1.3",
"Trensado M5 1.4",
"Trensado M5 1.5"

,"Trensado M3 0.8"
,"Trensado M3 0.9"
,"Trensado M3 1.0"
,"Trensado M3 1.1"
,"Trensado M3 1.2"
,"Trensado M3 1.3"
,"Trensado M3 1.4"
,"Trensado M3 1.5"






,"Trensado M9 1.5"
,"Trensado M9 1.6"
,"Trensado M9 1.7"
,"Trensado M9 1.8"
,"Trensado M9 1.9"
,"Trensado M9 2.0"
,"Trensado M9 2.1"
,"Trensado M9 2.2"
,"Trensado M9 2.3"
,"Trensado M9 2.4"
,"Trensado M9 2.5"
,"Trensado M9 2.6"
,"Trensado M9 2.7"
,"Trensado M9 2.8"
,"Trensado M9 2.9"
,"Trensado M9 3.0"
,"Trensado M9 3.1"
,"Trensado M9 3.2"
,"Trensado M9 3.3"
,"Trensado M9 3.4"
,"Trensado M9 3.5"
,"Trensado M9 3.6"
,"Trensado M9 3.7"
,"Trensado M9 3.8"
,"Trensado M9 3.9"
,"Trensado M9 4.0"



,"Sutache T5 0.5"
,"Sutache T5 0.6"
,"Sutache T5 0.7"
,"Sutache T5 0.8"
,"Sutache T5 0.9"
,"Sutache T5 1.0"
,"Trensa 5 Milimetros"

,"Trensa M9 1.5"
,"Trensa M9 1.6"
,"Trensa M9 1.7"
,"Trensa M9 1.8"
,"Trensa M9 1.9"
,"Trensa M9 2"

,"M9 3"
,"M9 3.5"
,"M9 4"
,"M9 4.5"
,"M9 5"
,"M9 5.5"



,"Sutache 0.8"
,"Sutache 0.9"
,"Sutache 1.0"
,"Sutache 1.1"
,"Sutache 1.2"
,"Sutache 1.3"
,"Sutache 1.4"
,"Sutache 1.5"

,"M5 especial 1.0"
,"M5 especial 1.1"
,"M5 especial 1.2"
,"M5 especial 1.3"
,"M5 especial 1.4"
,"M5 especial 1.5"
,"M5 especial 1.6"
,"M5 especial 1.7"
,"M5 especial 1.8"
,"M5 especial 1.9"
,"M5 especial 2.0"
,"Ginebra 4"

,"Riata Monserat 3.0"
,"Riata Monserat 3.5"
,"Riata Monserat 4.0"
,"Riata Monserat 4.5"
,"Riata Monserat 5.0"

,"Riata Guayu 3.0"
,"Riata Guayu 3.5"
,"Riata Guayu 4.0"
,"Riata Guayu 4.5"
,"Riata Guayu 5.0"
,"Riata Cortina Europea"
,"Riata galon tricolor"
,"Cordon mini"
,"Cordon 5"
,"Cordon 7"
,"Cordon 8"
,"Cordon 10"

"Trensado M5 retorcido  0.8",
"Trensado M5 retorcido  0.9",
"Trensado M5 retorcido  1.0",
"Trensado M5 retorcido  1.1",
"Trensado M5 retorcido  1.2",
"Trensado M5 retorcido  1.3",
"Trensado M5 retorcido  1.4",
"Trensado M5 retorcido  1.5"

,"Trensado M3 retorcido  0.8"
,"Trensado M3 retorcido  0.9"
,"Trensado M3 retorcido  1.0"
,"Trensado M3 retorcido  1.1"
,"Trensado M3 retorcido  1.2"
,"Trensado M3 retorcido  1.3"
,"Trensado M3 retorcido  1.4"
,"Trensado M3 retorcido  1.5"






,"Trensado M9 retorcido  1.5"
,"Trensado M9 retorcido  1.6"
,"Trensado M9 retorcido  1.7"
,"Trensado M9 retorcido  1.8"
,"Trensado M9 retorcido  1.9"
,"Trensado M9 retorcido  2.0"
,"Trensado M9 retorcido  2.1"
,"Trensado M9 retorcido  2.2"
,"Trensado M9 retorcido  2.3"
,"Trensado M9 retorcido  2.4"
,"Trensado M9 retorcido  2.5"
,"Trensado M9 retorcido  2.6"
,"Trensado M9 retorcido  2.7"
,"Trensado M9 retorcido  2.8"
,"Trensado M9 retorcido  2.9"
,"Trensado M9 retorcido  3.0"
,"Trensado M9 retorcido  3.1"
,"Trensado M9 retorcido  3.2"
,"Trensado M9 retorcido  3.3"
,"Trensado M9 retorcido  3.4"
,"Trensado M9 retorcido  3.5"
,"Trensado M9 retorcido  3.6"
,"Trensado M9 retorcido  3.7"
,"Trensado M9 retorcido  3.8"
,"Trensado M9 retorcido retorcido 3.9"
,"Trensado M9 retorcido  4.0"



,"Sutache T5 retorcido  0.5"
,"Sutache T5 retorcido  0.6"
,"Sutache T5 retorcido  0.7"
,"Sutache T5 retorcido  0.8"
,"Sutache T5 retorcido  0.9"
,"Sutache T5 retorcido  1.0"
,"Trensa retorcido  5 Milimetros"

,"Trensa M9 retorcido  1.5"
,"Trensa M9 retorcido 1.6"
,"Trensa M9 retorcido 1.7"
,"Trensa M9 retorcido  1.8"
,"Trensa M9 retorcido  1.9"
,"Trensa M9 retorcido  2"

,"M9 retorcido  3"
,"M9 retorcido  3.5"
,"M9 retorcido  4"
,"M9 retorcido  4.5"
,"M9 retorcido  5"
,"M9 retorcido  5.5"



,"Sutache retorcido  0.8"
,"Sutache retorcido  0.9"
,"Sutache retorcido  1.0"
,"Sutache retorcido   1.1"
,"Sutache retorcido  1.2"
,"Sutache retorcido  1.3"
,"Sutache retorcido  1.4"
,"Sutache  retorcido 1.5"

,"M5 especial retorcido  1.0"
,"M5 especial retorcido  1.1"
,"M5 especial retorcido  1.2"
,"M5 especial retorcido  1.3"
,"M5 especial retorcido  1.4"
,"M5 especial retorcido  1.5"
,"M5 especial retorcido  1.6"
,"M5 especial retorcido  1.7"
,"M5 especial retorcido  1.8"
,"M5 especial retorcido  1.9"
,"M5 especial retorcido  2.0"


]

# Ordenar las opciones de autocompletado
opciones1 = sorted(opciones1, key=lambda x: x.lower())

# Crear el Entry para el autocompletado
entrada_combobox = tk.Entry(root)
entrada_combobox.grid(row=0, column=1, padx=10, pady=10)

# Crear el Combobox para autocompletado
combobox = ttk.Combobox(root, textvariable=opcion1_var, values=opciones1)
combobox.grid(row=0, column=2, padx=20, pady=20)

# Vincular la función de autocompletado al evento de escritura en el Entry
entrada_combobox.bind('<KeyRelease>', actualizar_completado)


# Configuración de la interfaz

# Etiqueta para la segunda opción fija (Operario)
etiqueta_opcion2 = tk.Label(root, text="Operario:")
etiqueta_opcion2.grid(row=1, column=0, padx=10, pady=10)

# Opciones fijas para el segundo Combobox (Operario)
opciones2 = ["ANGEL", "KEVIN", "STEVEN", "ALEX", "JULIO", "EDUARDO", "KATERINE", 
             "JEIMY", "FEDERICO", "EDWIN", "FERNANDO", "ROBERTO", "OMAIRA", "DAVID", 
             "NUÑEZ", "SANTOS", "SALINAS", "MENDOZA", "KATHERINE", "WILLIAM"]

# Ordenar las opciones de operarios
opciones2 = sorted(opciones2, key=lambda x: x.lower())

# Crear el Combobox para la segunda opción (Operario)
opcion2_menu = ttk.Combobox(root, textvariable=opcion2_var, values=opciones2)
opcion2_var.set(opciones2[0])  # Establecer valor por defecto
opcion2_menu.grid(row=1, column=1, padx=10, pady=10)

# Etiqueta para la primera opción fija (Referencia)
etiqueta_opcion1 = tk.Label(root, text="Referencia:")
etiqueta_opcion1.grid(row=0, column=0, padx=10, pady=10)

# Entrada de número (Entry)
etiqueta_numero = tk.Label(root, text="Ingresa un número:")
etiqueta_numero.grid(row=3, column=0, padx=10, pady=10)

# Entrada de número (Entry)
numero_entry = tk.Entry(root, textvariable=numero_var)
numero_entry.grid(row=3, column=1, padx=10, pady=10)

# Botón para guardar los datos
boton_guardar = tk.Button(root, text="Guardar Datos", command=guardar_datos)
boton_guardar.grid(row=4, column=0, columnspan=2, pady=20)

# Ejecutar la interfaz gráfica
root.mainloop()












