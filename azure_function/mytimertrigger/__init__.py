# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprint) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints
#

import azure.functions as func # type: ignore
import logging
import sys
from pathlib import Path

# Añadir el directorio de data_processing al path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / 'data_processing'))

#vamos a importar la funcion main() cun un alias para diferenciarla
from main import process_data

def main(mytimer: func.TimerRequest) -> None:
    if mytimer.past_due:
        logging.info('The timer is past due!')
    logging.info('Timer trigger function ran at midnight')

    # Ejecutar el proceso principal de carga de datos
    process_data()