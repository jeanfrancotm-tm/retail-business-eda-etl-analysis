import pandas as pd
from src.utils.logger import get_logger

logger = get_logger()

def limpiar_pedidos(df):

    logger.info("Inicio limpieza")

    print(f"Registros iniciales: {len(df)}")  

    # ===============================
    # 2. Aplicar limpieza sobre pedidos: eliminar espacios extra en todas las columnas string.
    # ===============================
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # ===============================
    # 3. Estandarizar la columna Categoria a un único formato consistente (sugerencia: title case).
    # ===============================
    df["Categoria"] = df["Categoria"].str.title()


    # ===============================
    # 4. Manejar los valores faltantes en Cantidad: detectarlos y eliminarlos del dataset (justificar la decisión en un comentario).
    # ===============================
    # JUSTIFICACIÓN:No se pueden calcular métricas sin cantidad
    # ===============================
    df = df.dropna(subset=["Cantidad"])
    print(f"Después de eliminar nulos en Cantidad: {len(df)}")


    # ===============================
    # 5. Separar el campo Anexo en dos nuevas columnas: RUC y Empresa.
    # ===============================
    df[["RUC", "Empresa"]] = df["Anexo"].str.split(" - ", expand=True)

    # ===============================
    # 6. Validar que el RUC tenga exactamente 11 dígitos numéricos. Eliminar los registros que no cumplan esta condición.
    # ===============================
    df = df[df["RUC"].str.match(r"^\d{11}$", na=False)]
    print(f"Después de validar RUC: {len(df)}")  

    # ===============================
    # 7. Convertir la columna Fecha a tipo datetime (formato origen: DD/MM/YYYY) y Cantidad a entero.
    # ===============================
    df["Cantidad"] = df["Cantidad"].astype(int)
    df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d/%m/%Y")

    logger.info(f"Registros finales limpieza: {len(df)}")  

    return df


def consolidar(pedidos, precios):

    print(f"Antes del merge: {len(pedidos)}")  

    df = pedidos.merge(precios, on="Codigo_Producto", how="inner")

    # ===============================
    # 8. Hacer un merge entre el dataframe de pedidos y el de precios usando Codigo_Producto como llave.
    # JUSTIFICACIÓN:inner asegura consistencia
    # ===============================
    print(f"Después del merge: {len(df)}")  

    # ===============================
    # 9. Calcular las siguientes columnas derivadas: Total_Venta = Cantidad × Precio; Total_Costo = Cantidad × Costo; Margen = Total_Venta − Total_Costo.
    # ===============================
    df["Total_Venta"] = df["Cantidad"] * df["Precio"]
    df["Total_Costo"] = df["Cantidad"] * df["Costo"]
    df["Margen"] = df["Total_Venta"] - df["Total_Costo"]

    return df