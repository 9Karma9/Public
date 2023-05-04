import yfinance as yf
from datetime import datetime, timedelta

hasta = datetime.now().strftime('%Y-%m-%d')
desde = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
def export_data_symbol(COIN=None, date_start=desde, date_end=hasta):

    yf_Ticker = yf.Ticker("{}".format(COIN))
    yf_Data = yf_Ticker.history(period="1d", interval="1m", start=date_start, end=date_end)
    yf_Data.to_csv('./{}-format.csv'.format(COIN))

export_data_symbol(COIN="^IXIC", date_start=desde, date_end=hasta)

#COIN la variable se puede modificar poniendo en simbolo, igual en symbol data solo es ajustar periodo intervalo que esten permitidos
#y las fechas las ajustas en desde en la funcion de timedelta(days=aqui pondrias los días)
#consulta los simbolos disponibles en yahoo finance










