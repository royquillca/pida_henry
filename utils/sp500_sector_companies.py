
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

@st.cache_data
def plot_sector_companies_ts(df_sector, sector_name):
    fig = go.Figure()
    for column in df_sector.columns[1:]: # recorremos todas las columnas excepto la última (Date)
        # agregar línea de la media móvil
        fig.add_trace(go.Scatter(x=df_sector['Date'], y=df_sector[column], name=column.replace('_', ' ')))
    # Customización de los ejes y titulo
    fig.update_layout(
        title={
                "text": f'Evolución del precio de cierre ajustado del sector {sector_name}',
                "x": 0,
                "y": 0.95,
                "font": dict(size=16)
                },
            xaxis_title="Fecha",
            yaxis_title="Precio de cierre ajustado ($)",
            plot_bgcolor="white",
            height=700,
        )
    # Customizar la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='h',
            yanchor='bottom',
            y=-0.60,
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
    return fig
    # st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)

@st.cache_data
def plot_sector_companies_sma(df_sector, sector_name, window_size = 30):
    df_sector_sma = pd.DataFrame() # crear un nuevo DataFrame vacío
    df_sector_sma['Date'] = df_sector['Date'] # agregar la columna de fechas
    for column in df_sector.columns[1:]: # recorremos todas las columnas excepto la primera (Date)
        df_sector_sma[column + '_SMA'] = df_sector[column].rolling(window=window_size).mean()
    fig = go.Figure()
    for column in df_sector_sma.columns[1:]: # recorremos todas las columnas excepto la última (Date)
        # agregar línea de la media móvil
        fig.add_trace(go.Scatter(x=df_sector_sma['Date'], y=df_sector_sma[column], name=column.replace('_', ' ')))
    fig.update_layout(
        title={
                "text": f'Líneas de tendencia con SMA de {window_size} de las compañías del sector {sector_name}',
                "x": 0,
                "y": 0.95,
                "font": dict(size=16)
                },
            xaxis_title="Fecha",
            yaxis_title="Precio de cierre ajustado ($)",
            plot_bgcolor="white",
            height=700,
        )
    # Customizar la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='h',
            yanchor='bottom',
            y=-0.90,
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
    return fig
