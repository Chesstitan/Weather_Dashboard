#%% 
import pandas as pd
import glob 
import os

def comparador_arch_esolmet(f,arch_ref):
    '''
    Esta función sirve para comparar cuántas y qué columnas son diferentes
    en todos los archivos respecto a un archivo de referencia arbitrario.

    f: es la ruta de la carpeta que contiene los archivos csv de ESOLMET
    arch_ref: es la ubicación del archivo de referencia'''
    # Ruta de mis archivos
    # f = "../data/01_raw/ESOLMET/*.csv"

    # Columnas del archivo de referencia
    # arch_ref = "../data/01_raw/ESOLMET/2010_ESOLMET.csv"
    df_ref = pd.read_csv(arch_ref,encoding="ANSI",nrows=0)
    cols_ref = set(df_ref.columns)

    #Obtener lista de archivos csv, comparación y print
    archivos_csv = glob.glob(f)
    nombre_arch_ref = os.path.basename(arch_ref)
    print(f"Tomando como referencia el archivo: {nombre_arch_ref}")
    for archivo in archivos_csv:
        nombre_arch = os.path.basename(archivo)
        df_actual = pd.read_csv(archivo, encoding="ANSI",nrows=0)
        cols_actual = set(df_actual.columns)

        #Comparación de columnas
        cols_faltantes = cols_ref - cols_actual 
        cols_extras = cols_actual - cols_ref

        # Output que muestra las diferencias
        print(f"El archivo: {nombre_arch}")
        if not cols_faltantes  and not cols_extras:
            print("Coincide con todas las columnas de referencia ")
        else:
            if cols_faltantes:
                print(f"Le faltan {len(cols_faltantes)} columna(s): {cols_faltantes}")
            if cols_extras:
                print(f"Tiene {len(cols_extras)} columna(s) extra: {cols_extras}")
        print("-"*50)

# Prueba de la función
f = "../data/01_raw/ESOLMET/*.csv"
arch_ref = "../data/01_raw/ESOLMET/2020_ESOLMET.csv"
comparador_arch_esolmet(f,arch_ref)
# %%
