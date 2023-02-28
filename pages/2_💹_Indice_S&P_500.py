import streamlit as st
import pandas as pd
import numpy as np

from utils.sp500 import plot_time_series, plot_sma_graph, plot_candlestick_chart, plot_evol_volatility, plot_boxplot, plot_anual_performance, plot_daily_performance, plot_volumen

from utils.sp500_sector import price_tendency_plot

# Análisi de la serie temporal
plot_time_series()

# Gráfica de las medias móviles
plot_sma_graph()

# Gráfica de velas para ver la tendencia
plot_candlestick_chart()

# Evolución de la volatilidad
plot_evol_volatility()

# Diagrama de caja y bigotes
plot_boxplot()

# Gráfica el rendimiento anualizado
plot_anual_performance()

# Gráfica el rendimiento diario
plot_daily_performance()

# Gráfica del volumen de negociación
plot_volumen()
