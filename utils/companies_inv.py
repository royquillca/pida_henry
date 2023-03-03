import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go

def plot_candlestick_chart(company_name):
    df = pd.read_parquet(f'data/inv_companies/{company_name.lower()}.parquet')
    df = df.reset_index()
    # Crear la figura de velas financieras
    fig = go.Figure(
        go.Candlestick(
            x=df["Date"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Adj Close"],
            name="Candlestick",
        )
    )
    # Agregar una línea de promedio móvil de 50 días
    sma_50 = df["Adj Close"].rolling(window=50).mean()
    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=sma_50,
            name="SMA 50",
            line=dict(color="rgb(58, 208, 254)")
        )
    )
    # Agregar una línea de promedio móvil de 100 días
    sma_100 = df["Adj Close"].rolling(window=100).mean()
    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=sma_100,
            name="SMA 100",
            line=dict(color="rgb(58, 254, 104)")
        )
    )
    # Agregar una línea de promedio móvil de 100 días
    sma_200 = df["Adj Close"].rolling(window=200).mean()
    fig.add_trace(
        go.Scatter(
            x=df["Date"],
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
    return fig




def plot_anual_performance(company_name):
    df = pd.read_parquet(f'data/inv_companies/{company_name.lower()}.parquet')
    # Calcular el retorno anual
    year_return = df['Adj Close'].resample("Y").last().pct_change().to_frame().reset_index()
    year_return['Adj Close'] = year_return['Adj Close'] * 100
    # Crea columna de booleanos
    year_return['Up/Down'] = year_return['Adj Close'] > 0
    year_return['Up/Down'] = year_return['Up/Down'].replace({True: 'Subida', False: 'Caída'})
    # Definir el color basado en la columna de booleanos
    fig = px.bar(year_return, x='Date', y='Adj Close', color='Up/Down', color_discrete_sequence=['rgb(255, 119, 90)', 'rgb(127, 239, 95)'])
    # establecer el título y los títulos de los ejes
    fig.update_layout(
        title={
            'text':f"Rendimiento anualizado del precio de cierre ajustado de {company_name}",
            'x': 0,
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
            yanchor='top',
            y=1,
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
    return fig



    
def plot_boxplot(company_name):
    df = pd.read_parquet(f'data/inv_companies/{company_name.lower()}.parquet')
    # Calcular los retornos diarios del S&P 500
    df['daily_return'] = df['Adj Close'].pct_change()
    # Crear subplots
    fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=False ,vertical_spacing=0.09)
    # Crear un histograma de los retornos diarios
    histogram_fig = px.histogram(df, x='daily_return', nbins=50, labels={'daily_return': 'Retorno Diario'},color_discrete_sequence=['rgb(40, 116, 166)'], height=600, width=400)
    # Crear un boxplot de los retornos diarios
    boxplot_fig = px.box(df, x='daily_return', labels={'daily_return': 'Retorno Diario'},color_discrete_sequence=['rgb(40, 116, 166)'])
    # Agregar las gráficas al subplot
    fig.add_trace(histogram_fig['data'][0], row=1, col=1)
    fig.add_trace(boxplot_fig['data'][0], row=2, col=1)
    # Actualizar el layout del subplot
    fig.update_layout(
        title={
            'text':f"Distribución del Retorno Diario del {company_name}",
            'x': 0,
            'y': 0.95,
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
    return fig
