import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf
from io import StringIO

def obtener_empresas_nasdaq100():
    url = 'https://en.wikipedia.org/wiki/NASDAQ-100'
    respuesta = requests.get(url) 
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    tabla = soup.find('table', {'id': 'constituents'})
    # Usar StringIO para convertir la cadena HTML en un objeto similar a un archivo
    html_string = str(tabla)
    html_io = StringIO(html_string)
    df = pd.read_html(html_io)[0]
    return df['Ticker'].tolist()

def obtener_capitalizacion_mercado(empresas):
    datos = []
    for simbolo in empresas:
        empresa = yf.Ticker(simbolo)
        info = empresa.info
        capitalizacion = info.get('marketCap')
        datos.append({'Empresa': simbolo, 'Capitalización': capitalizacion})
    return pd.DataFrame(datos)

def obtener_datos_financieros(tickers):
    datos = {}
    for ticker in tickers:
        empresa = yf.Ticker(ticker)
        hist = empresa.history(period="1d")
        info = empresa.info
        
        
        datos[ticker] = { 
            'Empresa': info.get('shortName'),
            'Último Precio': hist['Close'].iloc[-1] if not hist.empty else None,
            'Capitalización de Mercado': info.get('marketCap'),
            'Ingresos Totales': info.get('totalRevenue'),
            'EBITDA': info.get('ebitda'),
            'Flujo de Caja Libre': info.get('freeCashflow'),
            'Deuda Total': info.get('totalDebt')
        }
    return pd.DataFrame.from_dict(datos, orient='index')
