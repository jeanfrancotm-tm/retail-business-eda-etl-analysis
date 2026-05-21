import os
from config import OUTPUT_ETL, DATASET_FINAL
from src.utils.logger import get_logger

logger = get_logger()

def guardar(df):
    os.makedirs(OUTPUT_ETL, exist_ok=True)
    df.to_csv(DATASET_FINAL, index=False)
    logger.info(f"Dataset guardado en: {DATASET_FINAL}")


def resumen(df):

    print("\n===== RESUMEN FINAL EJERCICIO 1 =====")
    # ===============================
    # 10. Mostrar el resumen final: número de registros válidos, venta total, costo total y margen total.
    # ===============================
    print(f"Registros válidos: {len(df)}")  
    print(f"Venta total: S/ {df['Total_Venta'].sum():,.2f}")
    print(f"Costo total: S/ {df['Total_Costo'].sum():,.2f}")
    print(f"Margen total: S/ {df['Margen'].sum():,.2f}")