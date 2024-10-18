import unicodedata
import tkinter as tk
from tkinter import filedialog, messagebox

def quitar_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_sin_acentos = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))
    return texto_sin_acentos

def procesar_archivo(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f_entrada:
            contenido = f_entrada.read()

        contenido_sin_acentos = quitar_acentos(contenido)

        with open(archivo_salida, 'w', encoding='utf-8') as f_salida:
            f_salida.write(contenido_sin_acentos)

        messagebox.showinfo("Éxito", f"Archivo procesado y guardado como {archivo_salida}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"El archivo {archivo_entrada} no se encontró.")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")

def seleccionar_archivo_entrada():
    archivo_entrada = filedialog.askopenfilename(
        title="Seleccionar archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if archivo_entrada:
        ruta_entrada.set(archivo_entrada)

def seleccionar_archivo_salida():
    archivo_salida = filedialog.asksaveasfilename(
        title="Guardar archivo de salida",
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if archivo_salida:
        procesar_archivo(ruta_entrada.get(), archivo_salida)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Quitar Acentos de Archivo")
ventana.geometry("400x200")

# Variable para almacenar la ruta del archivo de entrada
ruta_entrada = tk.StringVar()

# Etiqueta y campo para mostrar el archivo seleccionado
tk.Label(ventana, text="Archivo de entrada:").pack(pady=10)
tk.Entry(ventana, textvariable=ruta_entrada, width=50).pack(pady=5)

# Botón para seleccionar el archivo de entrada
tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo_entrada).pack(pady=10)

# Botón para procesar el archivo y pedir la ubicación de salida
tk.Button(ventana, text="Procesar y guardar archivo", command=seleccionar_archivo_salida).pack(pady=20)

# Iniciar la aplicación
ventana.mainloop()
