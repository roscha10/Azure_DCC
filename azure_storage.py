import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import pandas as pd

# Suponemos que el nombre del contenedor está configurado como una variable de entorno o está definido en otro lugar
CONTAINER_NAME = 'marketdata'

def subir_archivo_a_blob(dataframe, directorio, nombre_archivo):
    # Asumimos que la conexión se establece en el entorno
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    
    csv_data = dataframe.to_csv(index=False, encoding='utf-8')
    blob_name = f'{directorio}/{nombre_archivo}.csv'
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(csv_data, blob_type="BlockBlob", overwrite=True)
    print(f'El archivo {blob_name} ha sido subido exitosamente.')

def descargar_archivo_de_blob(blob_name, local_file_name):
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    
    blob_client = container_client.get_blob_client(blob_name)
    with open(local_file_name, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    print(f'El archivo {blob_name} ha sido descargado como {local_file_name}')