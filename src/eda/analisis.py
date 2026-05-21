import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import DATASET_FINAL, OUTPUT_EDA

sns.set(style="whitegrid")


def cargar_dataset():
    return pd.read_csv(DATASET_FINAL)


def preparar_directorio():
    os.makedirs(OUTPUT_EDA, exist_ok=True)


# ===============================
# 11. ANÁLISIS UNIVARIADO
# ===============================
def analisis_univariado(df):

    plt.figure(figsize=(10,6))
    df["Cantidad"].plot(kind="hist", bins=10)
    plt.title("Distribución de Cantidad")
    plt.xlabel("Cantidad")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_EDA, "hist_cantidad.png"))
    plt.close()

    plt.figure()
    df["Categoria"].value_counts().plot(kind="bar")
    plt.title("Distribución por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_EDA, "bar_categoria.png"))
    plt.close()


# ===============================
# 12. ANÁLISIS BIVARIADO
# ===============================
def analisis_bivariado(df):

    data = df.groupby("Categoria")["Total_Venta"].sum()

    plt.figure(figsize=(10,6))
    data.plot(kind="bar")
    plt.title("Total de Ventas por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Venta Total (S/)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_EDA, "ventas_categoria.png"))
    plt.close()


# ===============================
# 13. ANÁLISIS MULTIVARIADO
# ===============================
def analisis_multivariado(df):

    pivot = pd.pivot_table(
        df,
        values="Total_Venta",
        index="Empresa",
        columns="Categoria",
        aggfunc="sum"
    )

    '''plt.figure()
    sns.heatmap(pivot, annot=True, fmt=".0f")'''
    plt.figure(figsize=(12,8))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="coolwarm")
    plt.title("Empresa vs Categoría vs Venta")
    plt.xlabel("Categoría")
    plt.ylabel("Empresa")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_EDA, "heatmap.png"))
    plt.close()


# ===============================
# 14. RESPUESTAS DE NEGOCIO
# ===============================
def preguntas_negocio(df):

    print("\n===== 14. RESPUESTAS DE NEGOCIO =====")

    cat = df.groupby("Categoria")["Margen"].sum().idxmax()
    print(f"Categoría más rentable: {cat}")

    prov = df.groupby("Empresa")["Margen"].sum().idxmax()
    print(f"Proveedor más rentable: {prov}")

    prod = df.groupby("Producto")["Margen"].sum().idxmax()
    print(f"Producto a priorizar: {prod}")


# ===============================
# 15. CONCLUSIONES
# ===============================
def conclusiones():

    print("\n===== CONCLUSIONES =====")

    print("""
Se observa que la rentabilidad depende del margen y no solo del volumen de ventas.
Se recomienda priorizar productos con mayor margen, fortalecer proveedores más rentables
y enfocar estrategias comerciales en categorías con mayor contribución económica.
""")


# ===============================
# EJECUCIÓN
# ===============================
def ejecutar_eda(df):

    preparar_directorio()

    analisis_univariado(df)
    analisis_bivariado(df)
    analisis_multivariado(df)
    preguntas_negocio(df)
    conclusiones()

    print("\nEDA completo generado en la carpeta Reporte")


