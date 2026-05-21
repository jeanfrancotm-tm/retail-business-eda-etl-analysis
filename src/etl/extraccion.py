import pandas as pd
from config import PEDIDOS_PATH, PRECIOS_PATH
from src.utils.logger import get_logger

logger = get_logger()

def cargar_datos():
    logger.info("Extrayendo datos...")

    # ===============================
    # 1. Cargar pedidos.csv (delimitador '|') y lista_precios.xlsx en dataframes separados.
    # ===============================
    pedidos = pd.read_csv(PEDIDOS_PATH, delimiter="|")
    precios = pd.read_excel(PRECIOS_PATH)

    logger.info(f"Pedidos cargados: {len(pedidos)} filas")
    logger.info(f"Precios cargados: {len(precios)} filas")

    return pedidos, precios