import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_RAW = os.path.join(BASE_DIR, "data", "Raw")
OUTPUT_ETL = os.path.join(BASE_DIR, "data", "Processed")
OUTPUT_EDA = os.path.join(BASE_DIR, "data", "Reporte")

PEDIDOS_PATH = os.path.join(DATA_RAW, "pedidos.csv")
PRECIOS_PATH = os.path.join(DATA_RAW, "lista_precios.xlsx")

DATASET_FINAL = os.path.join(OUTPUT_ETL, "dataset_consolidado.csv")