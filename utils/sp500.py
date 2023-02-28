import pandas as pd
import numpy as np
from datetime import datetime

import streamlit as st

import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.offline as pyo

# Carga de los datos
sp500_df = pd.read_parquet('data/sp500.parquet')
# La variable Date pasa a ser una columna
sp500_df = sp500_df.reset_index()
# Conversion del tipo str a datetime de la varibale Date
sp500_df['Date'] = pd.to_datetime(sp500_df['Date'])

# Tendencia del índice en el tiempo
def plot_time_series():
    # Crear la figura
    fig = px.line(sp500_df, x="Date", y=["Adj Close"], color_discrete_sequence=['rgb(40, 116, 166)'])
    # Personalizar el aspecto de la gráfica
    fig.update_layout(
        title={
            'text': 'Variación de los precios de cierre ajustado del indice S&P 500 desde el año 2000',
            'x': 0.15,
            'y': 0.99,
            'font': dict(size=16)},
        xaxis_title="Fecha (Años)",
        yaxis_title="Precio de cierre ajustado ($)",
        plot_bgcolor="white"
    )
    # Cambiar el nombre de la variable en la leyenda
    fig.update_traces(name='Precio ajustado de cierre')
    # Cambiar los nombres de la leyenda
    # fig.update_layout(legend=dict(title='Legenda:', orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
    fig.update_layout(
    legend=dict(
        title='<b>Leyenda:</b>',
        orientation='v',
        yanchor='bottom',
        y=0.01,
        xanchor='right',
        x=1,
        bgcolor='rgba(0,0,0,0)',
        font=dict(size=12)
    )
    )
    # Customizacion de las ventanas temporales
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="Último mes", step="month", stepmode="backward"),
                dict(count=6, label="Últimos 6 meses", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="Último año", step="year", stepmode="backward"),
                dict(count=5, label="Últimos 5 años", step="year", stepmode="backward"),
                dict(count=10, label="Últimos 10 años", step="year", stepmode="backward"),
                dict(step="all", label="Todo")
            ])
        )
    )
    # Mostrar la figura
    st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)


def plot_sma_graph():
    # calcular la media móvil de 200 días
    ma_200 = sp500_df['Adj Close'].rolling(window=200).mean()
    # calcular la media móvil de 100 días
    ma_100 = sp500_df['Adj Close'].rolling(window=100).mean()
    # calcular la media móvil de 50 días
    ma_50 = sp500_df['Adj Close'].rolling(window=50).mean()

    # crear la figura con plotly
    fig = go.Figure()

    # agregar la serie de precios de cierre ajustado
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=sp500_df['Adj Close'], name='Precio de cierre ajustado ($)'))

    # agregar la serie de la media móvil de 50 días
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=ma_50, name='SMA 50 días ($)'))

    # agregar la serie de la media móvil de 100 días
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=ma_100, name='SMA 100 días ($)'))

    # agregar la serie de la media móvil de 200 días
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=ma_200, name='SMA 200 días ($)'))

    # establecer el título y los títulos de los ejes
    fig.update_layout(
        title={
            'text': 'Medias móviles del S&P 500 del precio de cierre ajustado',
            'x': 0.25,
            'font': dict(size=16)},
        xaxis_title='Fecha (Años)',
        yaxis_title='Precio de cierre ajustado ($)',
        #   template="ggplot2"
        template="seaborn",
        height=600,
        width=800,
        )
    fig.update_layout(xaxis_rangeslider_visible=False)
    # Cambiar los nombres de la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='v',
            yanchor='bottom',
            y=0.01,
            xanchor='right',
            x=1,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=12)
        )
    )

    # Customizacion de las ventanas temporales
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="Último mes", step="month", stepmode="backward"),
                dict(count=6, label="Últimos 6 meses", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="Último año", step="year", stepmode="backward"),
                dict(count=5, label="Últimos 5 años", step="year", stepmode="backward"),
                dict(count=10, label="Últimos 10 años", step="year", stepmode="backward"),
                dict(step="all", label="Todo")
            ])
        )
    )
    # Mostrar la gráfica
    st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)   
    
def plot_candlestick_chart():
    # Crear la figura de velas financieras
    fig = go.Figure(
        go.Candlestick(
            x=sp500_df["Date"],
            open=sp500_df["Open"],
            high=sp500_df["High"],
            low=sp500_df["Low"],
            close=sp500_df["Adj Close"],
            name="Candlestick",
        )
    )
    # Agregar una línea de promedio móvil de 50 días
    sma_50 = sp500_df["Adj Close"].rolling(window=50).mean()
    fig.add_trace(
        go.Scatter(
            x=sp500_df["Date"],
            y=sma_50,
            name="SMA 50",
            line=dict(color="rgb(58, 208, 254)")
        )
    )
    # Agregar una línea de promedio móvil de 100 días
    sma_100 = sp500_df["Adj Close"].rolling(window=100).mean()
    fig.add_trace(
        go.Scatter(
            x=sp500_df["Date"],
            y=sma_100,
            name="SMA 100",
            line=dict(color="rgb(58, 254, 104)")
        )
    )
    # Agregar una línea de promedio móvil de 100 días
    sma_200 = sp500_df["Adj Close"].rolling(window=200).mean()
    fig.add_trace(
        go.Scatter(
            x=sp500_df["Date"],
            y=sma_200,
            name="SMA 200",
            line=dict(color="rgb(254, 202, 58)")
        )
    )
    # Personalizar el aspecto de la gráfica    
    fig.update_layout(
        title={
            'text': 'Gráfico de velas financieras del indíce S&P 500',
            'x': 0.30,
            'font': dict(size=16)
            },
        xaxis_title="Fecha",
        yaxis_title="Precio de cierre ajustado",
        hovermode="x",
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            gridcolor="rgb(184, 186, 187)",
            tickfont=dict(size=10),
        )
    )
    # Cambiar los nombres de la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='v',
            yanchor='bottom',
            y=0.01,
            xanchor='right',
            x=1,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=12)
        )
    )
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        height=650,
        plot_bgcolor='white')

    # Customizacion de las ventanas temporales
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="Último mes", step="month", stepmode="backward"),
                dict(count=6, label="Últimos 6 meses", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="Último año", step="year", stepmode="backward"),
                dict(count=5, label="Últimos 5 años", step="year", stepmode="backward"),
                dict(count=10, label="Últimos 10 años", step="year", stepmode="backward"),
                dict(step="all", label="Todo")
            ])
        )
    )

    # Mostrar la gráfica
    st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)
    
def plot_evol_volatility():
    # Calcular la volatilidad del S&P 500
    period = 30 # Dfinimos el periodo de tiempo
    sp500_vol_30 = sp500_df["Close"].pct_change().rolling(period).std() * np.sqrt(period) # Volatilidad implícita con periodo de 30 días
    sp500_vol_50 = sp500_df["Close"].pct_change().rolling(50).std() * np.sqrt(50) # Volatilidad implícita con periodo de 50 días
    sp500_vol_100 = sp500_df["Close"].pct_change().rolling(100).std() * np.sqrt(100) # Volatilidad implícita con periodo de 100 días
    sp500_vol_200 = sp500_df["Close"].pct_change().rolling(200).std() * np.sqrt(200) # Volatilidad implícita con periodo de 200 días
    # Graficar la volatilidad del S&P 500
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=sp500_vol_30, name="Vol. 30 días"))
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=sp500_vol_50, name="Vol. 50 días"))
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=sp500_vol_100, name="Vol. 100 días"))
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=sp500_vol_200, name="Vol. 200 días"))
    fig.update_layout(
        title={
            'text':"Volatilidad del S&P 500",
            'x': 0.34,
            'font': dict(size=16)
            },
        xaxis_title="Fecha (Años)",
        yaxis_title="Volatilidad",
        height=600,
    )
    fig.update_layout(
        plot_bgcolor ='white'
    )
    # Cambiar los nombres de la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='v',
            yanchor='top',
            y=1,
            xanchor='left',
            x=0.01,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=12)
        )
    )
    # Customizacion de las ventanas temporales
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="Último mes", step="month", stepmode="backward"),
                dict(count=6, label="Últimos 6 meses", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="Último año", step="year", stepmode="backward"),
                dict(count=5, label="Últimos 5 años", step="year", stepmode="backward"),
                dict(count=10, label="Últimos 10 años", step="year", stepmode="backward"),
                dict(step="all", label="Todo")
            ])
        )
    )
    # Mostrar la gráfica
    st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)
    
    
def plot_boxplot():
    # Calcular los retornos diarios del S&P 500
    sp500_df['daily_return'] = sp500_df['Adj Close'].pct_change()
    # Crear subplots
    fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=False ,vertical_spacing=0.09)
    # Crear un histograma de los retornos diarios
    histogram_fig = px.histogram(sp500_df, x='daily_return', nbins=50, labels={'daily_return': 'Retorno Diario'},color_discrete_sequence=['rgb(40, 116, 166)'], height=600, width=400)
    # Crear un boxplot de los retornos diarios
    boxplot_fig = px.box(sp500_df, x='daily_return', labels={'daily_return': 'Retorno Diario'},color_discrete_sequence=['rgb(40, 116, 166)'])
    # Agregar las gráficas al subplot
    fig.add_trace(histogram_fig['data'][0], row=1, col=1)
    fig.add_trace(boxplot_fig['data'][0], row=2, col=1)
    # Actualizar el layout del subplot
    fig.update_layout(
        title={
            'text':"Distribución del Retorno Diario del S&P 500",
            'x': 0.30,
            'y': 1,
            'font': dict(size=16)
            },
        xaxis_title="Retorno diario",
        yaxis_title="Cantidad de días",
        xaxis=dict(side='top'),
        plot_bgcolor='white',
        height=600,
        )
    fig.update_layout(xaxis=dict(side='bottom'))
    # Mostrar el gráfico
    st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)

def plot_anual_performance():
    # Calcular el retorno anual
    year_return = sp500_df.set_index('Date')['Adj Close'].resample("Y").last().pct_change().to_frame().reset_index()
    year_return['Adj Close'] = year_return['Adj Close'] * 100
    # Crea columna de booleanos
    year_return['Up/Down'] = year_return['Adj Close'] > 0
    year_return['Up/Down'] = year_return['Up/Down'].replace({True: 'Subida', False: 'Caída'})
    # Definir el color basado en la columna de booleanos
    fig = px.bar(year_return, x='Date', y='Adj Close', color='Up/Down', color_discrete_sequence=['rgb(255, 119, 90)', 'rgb(127, 239, 95)'])
    # establecer el título y los títulos de los ejes
    fig.update_layout(
        title={
            'text':"Rendimiento anualizado de S&P 500 del precio de cierre ajustado",
            'x': 0.20,
            'y': 1,
            'font': dict(size=16)
            },
        xaxis_title='Fecha (Años)',
        yaxis_title='Retorno (%)',
        template="seaborn"
        )
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        height=600,
        plot_bgcolor='white')
    # Cambiar los nombres de la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='v',
            yanchor='bottom',
            y=0,
            xanchor='right',
            x=1,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=12)
        )
    )
    # Customizacion de las ventanas temporales
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="Último mes", step="month", stepmode="backward"),
                dict(count=6, label="Últimos 6 meses", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="Último año", step="year", stepmode="backward"),
                dict(count=5, label="Últimos 5 años", step="year", stepmode="backward"),
                dict(count=10, label="Últimos 10 años", step="year", stepmode="backward"),
                dict(step="all", label="Todo")
            ])
        )
    )
    # Mostrar la gráfica
    st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)
    
    
def plot_daily_performance():
    # Calcular el rendimiento mensual
    month_return = sp500_df.set_index('Date')['Adj Close'].resample("M").last().pct_change().to_frame().reset_index()
    month_return['Up/Down'] = month_return['Adj Close'] > 0
    month_return['Up/Down'] = month_return['Up/Down'].replace({True: 'Subida', False: 'Caida'})
    month_return['Adj Close'] = month_return['Adj Close'] * 100
    # Crear un gráfica de los rendimiento mensuales
    fig = px.bar(month_return, x='Date', y='Adj Close', labels='Retorno Mensual (%)', color='Up/Down', color_discrete_sequence=['rgb(255, 119, 90)', 'rgb(127, 239, 95)'])
    # Cambiar los nombres de la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='h',
            yanchor='bottom',
            y=1,
            xanchor='right',
            x=1))
    # Personalizar el título y los títulos de los ejes
    fig.update_layout(
        title={
            'text':'Retorno mensual de S&P 500 del precio de cierre ajustado',
            'x': 0.20,
            'y': 1,
            'font': dict(size=16)
            },
        xaxis_title='Fecha (Años)',
        yaxis_title='Retorno (%)',
        template="seaborn"
        )
    fig.update_layout(xaxis_rangeslider_visible=False, height=600,plot_bgcolor='white')
    # Customizacion de las ventanas temporales
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="Último mes", step="month", stepmode="backward"),
                dict(count=6, label="Últimos 6 meses", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="Último año", step="year", stepmode="backward"),
                dict(count=5, label="Últimos 5 años", step="year", stepmode="backward"),
                dict(count=10, label="Últimos 10 años", step="year", stepmode="backward"),
                dict(step="all", label="Todo")
            ])
        )
    )
    # Mostrar la gráfica
    st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)
    
def plot_volumen():
    # Selecciona las columnas de volumen y precio ajustado de cierre
    sales_volume = sp500_df.copy(deep=True)
    sales_volume = sales_volume[["Adj Close", "Volume"]]
    # Calcula el volumen de ventas y compras diarias
    sales_volume.loc[:, "Volumen de Ventas"] = -sales_volume["Volume"] * sales_volume["Adj Close"].diff()
    sales_volume.loc[:, "Volumen de Compras"] = sales_volume["Volume"] * abs(sales_volume["Adj Close"].diff().where(sales_volume["Adj Close"].diff() > 0, 0))

    # Crear una figura de Plotly con dos subgráficos
    fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.2)
    # Crear el gráfico de barras con los valores por debajo de cero en rojo y los valores por encima de cero en azul
    fig.add_trace(go.Bar(x=sp500_df['Date'], y=sales_volume['Volumen de Ventas'], name='Volumen de Ventas', marker_color='rgb(127, 239, 95)'), row=2, col=1)
    fig.add_trace(go.Bar(x=sp500_df['Date'], y=sales_volume['Volumen de Compras'], name='Volumen de Compras', marker_color='rgb(255, 119, 90)'),row=2, col=1)
    # Agregar un trazado para el precio de cierre en el primer subgráfico
    fig.add_trace(go.Scatter(x=sp500_df['Date'], y=sp500_df['Adj Close'], name='Precio de cierre ajustado', marker_color='rgb(40, 116, 166 )'), row=1, col=1)
    # Agregar un trazado para el volumen de ventas en el segundo subgráfico
    # fig.add_trace(go.Bar(x=sp500_df['Date'], y=sp500_df['Volume'], name='Volumen de ventas'), row=2, col=1)
    # Personalizar el diseño y las opciones de visualización de la figura
    # fig.update_layout(
    #     title='Precio de cierre y volumen de ventas del índice S&P 500',
    #     yaxis=dict(title='Precio de cierre ajustado'),
    #     yaxis2=dict(title='Volumen de transacción'),
    #     plot_bgcolor ='white')

    # Customización de la legenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>', 
            orientation='v', 
            yanchor='bottom',
            y=0.58,
            xanchor='right',
            x=1))
    fig.update_layout(
        title={
            "text": "Volumen de compras y ventas diarios del índice S&P 500",
            'x': 0.20,
            'y': 1,
            'font': dict(size=16)
            },
        xaxis_title="Fecha",
        yaxis_title="Ventas/Compras",
        plot_bgcolor='white',
        height=750,
        )
    # Personalizar la cuadrícula
    fig.update_layout(
        xaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=True
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=True
        ),
    )
    # Customizacion de las ventanas temporales
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="Último mes", step="month", stepmode="backward"),
                dict(count=6, label="Últimos 6 meses", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="Último año", step="year", stepmode="backward"),
                dict(count=5, label="Últimos 5 años", step="year", stepmode="backward"),
                dict(count=10, label="Últimos 10 años", step="year", stepmode="backward"),
                dict(step="all", label="Todo")
            ])
        )
    )
    # Mostrar la figura
    st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)