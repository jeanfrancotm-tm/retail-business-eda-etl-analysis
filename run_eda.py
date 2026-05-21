from src.eda.analisis import cargar_dataset, ejecutar_eda

def main():
    df = cargar_dataset()
    ejecutar_eda(df)

if __name__ == "__main__":
    main()