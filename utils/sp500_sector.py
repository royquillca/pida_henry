import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# Tendencia del índice en el tiempo
@st.cache_data
def price_trend_plot(sector_name):
    df = pd.read_parquet(f'data/{sector_name.lower().replace(" ", "_")}.parquet').reset_index()
    df['Date'] = pd.to_datetime(df['Date'])
    fig = go.Figure()
           
    # Crear la figura
    fig = px.line(df, x="Date", y=["Adj Close"])
    # Personalizar el aspecto de la gráfica
    fig.update_layout(
        title={
            "text": f"Precio de cierre ajustado de {sector_name.replace('_',' ').title()}",
            "x": 0.25,
            "y": 1,
            "font": dict(size=16)
            },
        xaxis_title="Fecha (Años)",
        yaxis_title="Precio de cierre ajustado ($)",
        plot_bgcolor="white",
        height=500,
    )
    # Cambiar el nombre de la variable en la leyenda
    fig.update_traces(name=f"Precio ajustado de cierre {sector_name.replace('_',' ').title()}")
    # Cambiar los nombres de la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>', 
            orientation='v',
            yanchor='bottom',
            y=0.05,
            xanchor='right',
            x=1,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=12)
            ))
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
def plot_close_price_ts(dict_data):
    fig = go.Figure()

    for df_name, df in dict_data.items():
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Adj Close'], name=f"P. Aj. de {df_name.replace('_', ' ').title()}"))

    fig.update_layout(
        title="Precio de cierre ajustado de todas las acciones",
        xaxis_title="Fecha",
        yaxis_title="Precio de cierre ajustado ($)",
        plot_bgcolor="white",
        xaxis_rangeslider_visible=False,
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

    # Customizar la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='h',
            yanchor='bottom',
            y=-0.65,
            xanchor='left',
            x=0.01,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=12)
        )
    )
    # Mostrar la gráfica
    return fig
    # st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)