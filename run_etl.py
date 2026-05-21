

from src.etl.extraccion import cargar_datos
from src.etl.transformacion import limpiar_pedidos, consolidar
from src.etl.carga import guardar, resumen



def main():
    

    pedidos, precios = cargar_datos()

    pedidos = limpiar_pedidos(pedidos)
    df = consolidar(pedidos, precios)

    resumen(df)
    guardar(df)

if __name__ == "__main__":
    main()