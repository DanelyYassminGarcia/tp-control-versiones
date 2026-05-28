import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------------------------
# Script de análisis de datos climáticos
# Proyecto: tp-control-versiones
# Dataset: Global Temperature Time Series (GISTEMP)
# Integrante: Danely Yassmin Garcia
# -----------------------------------------------

# Se carga el dataset desde la carpeta /datos
df = pd.read_csv("datos/monthly.csv")

# Se extrae el año de la columna Year (formato yyyy-mm-dd)
# para poder agrupar y analizar por año
df["año"] = df["Year"].str[:4].astype(int)

# Se filtra solo el source "GCAG" para evitar duplicados
# ya que el dataset incluye dos fuentes distintas para el mismo período
df = df[df["Source"] == "GCAG"]

# --- INDICADORES ESTADÍSTICOS ---
# Se calculan los indicadores
temperatura_promedio = round(df["Mean"].mean(), 2)
temperatura_maxima = round(df["Mean"].max(), 2)
temperatura_minima = round(df["Mean"].min(), 2)

print("=== INDICADORES CLIMÁTICOS GLOBALES ===")
print(f"Temperatura promedio global  : {temperatura_promedio} °C")
print(f"Temperatura máxima registrada: {temperatura_maxima} °C")
print(f"Temperatura mínima registrada: {temperatura_minima} °C")

# --- GRÁFICO: Evolución de temperatura anual ---
# Agrupamos por año para visualizar la tendencia temporal
temperatura_anual = df.groupby("año")["Mean"].mean()

plt.figure(figsize=(12, 5))
plt.plot(temperatura_anual.index, temperatura_anual.values,
         marker="o", color="tomato", linewidth=2, markersize=4)
plt.title("Evolución de la Temperatura Promedio Anual - GISTEMP", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Anomalía de Temperatura (°C)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Se guarda en la carpeta /resultados 
os.makedirs("resultados", exist_ok=True)
plt.savefig("resultados/grafico_temperatura.png", dpi=150)
plt.show()
print("✅ Gráfico guardado en resultados/grafico_temperatura.png")
