import pandas as pd


def calc_volatility(df, period):
    # Calcular los cambios porcentuales diarios en el precio de la acción
    daily_returns = df['Close'].pct_change()

    # Calcular la volatilidad según el período especificado
    if period == 'anual':
        volatility = daily_returns.resample('Y').std().iloc[-1] * (252 ** 0.5)
    elif period == 'semestral':
        volatility = daily_returns.resample('6M').std().iloc[-1] * (252 ** 0.5)
    elif period == 'trimestral':
        volatility = daily_returns.resample('Q').std().iloc[-1] * (252 ** 0.5)
    else:
        raise ValueError(f"El período {period} no es válido.")

    # Retornar la volatilidad calculada
    return volatility

def calc_agr(df):
    daily_returns = df["Close"].pct_change()
    # Calcular la tasa de crecimiento anual promedio
    annual_average_growth_rate = daily_returns.mean() * 252
    return annual_average_growth_rate



def calculate_cumulative_return(df, period):
    # Selecciona los datos de precios de cierre ajustados para el período de tiempo seleccionado
    df = df.reset_index()
    df_period = df.loc[df['Date'] >= pd.Timestamp.today() - pd.tseries.offsets.DateOffset(months=int(period[:-1])*6)]
    
    # Resample a precios de cierre ajustados mensuales
    df_return = df_period.resample('M', on='Date').last()
    
    # Calcula los retornos mensuales y acumulados
    df_return['return'] = df_return['Adj Close'].pct_change()
    df_return['cumulative_return'] = (1 + df_return['return']).cumprod()
    
    cumulative_return = df_return['cumulative_return'][-1]
    # Imprime la rentabilidad acumulada
    # print(f"Rentabilidad acumulada en los últimos {period}: {cumulative_return}")

    return cumulative_return