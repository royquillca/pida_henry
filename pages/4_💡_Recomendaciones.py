import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils.sp500_sector_companies import plot_sector_companies_sma, plot_sector_companies_ts



# Carga de datos
health_care = pd.read_parquet("data/sector_companies/health_care_companies.parquet")
consumer_discretionary = pd.read_parquet("data/sector_companies/consumer_discretionary_companies.parquet")
information_technology = pd.read_parquet("data/sector_companies/information_technology_companies.parquet")

st.markdown('<h4 align="center">Seleccione la gráfica de la tendencia del precios de las acciones por sector</h4>', unsafe_allow_html=True)
# Crea un st.selectbox para que el usuario seleccione la gráfica que desea ver
option = st.selectbox('',
   ('Tecnología de la Información', 'Salud', 'consumo discrecional')
)

# Dependiendo de la opción seleccionada, llama a una u otra función
if option == 'Tecnología de la Información':
    fig_ts = plot_sector_companies_ts(information_technology, 'tecnología de la información')
    st.plotly_chart(fig_ts, config=dict(displayModeBar=False), use_container_width=True)
    window_size = st.number_input('Periodo de SMA', min_value=30, max_value=500, step=10)
    fig_sma = plot_sector_companies_sma(information_technology, 'tecnología de la información', window_size)
    st.plotly_chart(fig_sma, config=dict(displayModeBar=False), use_container_width=True)
    
elif option == 'Salud':
    fig_ts = plot_sector_companies_ts(health_care, 'salud')
    st.plotly_chart(fig_ts, config=dict(displayModeBar=False), use_container_width=True)
    window_size = st.number_input('Periodo de SMA', min_value=30, max_value=500, step=10)
    fig_sma = plot_sector_companies_sma(health_care, 'salud',window_size)
    st.plotly_chart(fig_sma, config=dict(displayModeBar=False), use_container_width=True)

else:
    fig_ts = plot_sector_companies_ts(consumer_discretionary, 'consumo discrecional')
    st.plotly_chart(fig_ts, config=dict(displayModeBar=False), use_container_width=True)
    window_size = st.number_input('Periodo de SMA', min_value=30, max_value=500, step=10)
    fig_sma = plot_sector_companies_sma(consumer_discretionary, 'consumo discrecional',window_size)
    st.plotly_chart(fig_sma, config=dict(displayModeBar=False), use_container_width=True)
    