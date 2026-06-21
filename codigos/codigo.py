import pandas as pd
from pathlib import Path

# Archivo original
archivo = r"C:\Users\aLESS\Documents\MATLAB\Biomecanica\angulos_crudo\149ANGLES.csv"

# Carpeta donde guardar recortados
salida = r"C:\Users\aLESS\Documents\MATLAB\Biomecanica\angulos_recortados"

# Leer CSV
df = pd.read_csv(archivo)

# Pedir tiempos
t_ini = float(input("Tiempo inicial (s): "))
t_fin = float(input("Tiempo final (s): "))

# Recortar
df_rec = df[(df["Time"] >= t_ini) & (df["Time"] <= t_fin)].copy()

# Opcional: reiniciar tiempo a 0
df_rec["Time"] = df_rec["Time"] - df_rec["Time"].iloc[0]

# Nombre de salida
nombre_original = Path(archivo).stem
nombre_salida = f"{nombre_original}_recortado.csv"

ruta_salida = Path(salida) / nombre_salida

# Guardar
df_rec.to_csv(ruta_salida, index=False)

print(f"\nArchivo guardado en:")
print(ruta_salida)
print(f"Filas exportadas: {len(df_rec)}")