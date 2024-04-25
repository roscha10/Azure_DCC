from data_acquisition import obtener_empresas_nasdaq100, obtener_capitalizacion_mercado, obtener_datos_financieros
from azure_storage import subir_archivo_a_blob, descargar_archivo_de_blob

def main():
    # Obtener los tickers de todas las empresas del NASDAQ-100
    tickers_nasdaq100 = obtener_empresas_nasdaq100()

    # Obtener la capitalización de mercado para todas las empresas
    df_cap_nasdaq100 = obtener_capitalizacion_mercado(tickers_nasdaq100)

    # Obtener datos financieros para todas las empresas del NASDAQ-100
    df_datos_financieros_nasdaq100 = obtener_datos_financieros(tickers_nasdaq100)

    # Subir los datos financieros de todas las empresas al Blob Storage
    subir_archivo_a_blob(df_datos_financieros_nasdaq100, "datos-financieros", "datos_financieros_nasdaq100")

    # Opcional: descargar el archivo subido para verificación o uso local
    descargar_archivo_de_blob("datos-financieros/datos_financieros_nasdaq100.csv", "datos_financieros_nasdaq100_descargado.csv")

if __name__ == "__main__":
    main()
