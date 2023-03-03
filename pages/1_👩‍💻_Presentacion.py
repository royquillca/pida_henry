import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

import streamlit as st
from utils.kpis import calc_volatility, calc_agr, calculate_cumulative_return
# from utils.

st.markdown('<h4 align="center">Análisis de inversión en el mercado bursátil - Proyecto Individual 3 de Data Analytics del Bootcamp Data Science en Soy Henry</h4>', unsafe_allow_html=True)
st.markdown('**Descripción del problema**')

st.markdown("En este proyecto simulamos una situación en donde una empresa busca invertir en el mercado bursátil y nos solicita analizarlo en detalle. Como expertos en datos, estamos en capacidad de brindar una explicación de lo que ha sucedido en este mercado en los últimos 23 años (considerando impactos positivos y negativos a partir del año 2000), recomendaciones de inversión y otra información complementaria. El foco del análisis es variado y amplio, pero nos limitamos a las empresas pertenecientes al índice SP500 (Standard & Poor's 500 Index).")

st.markdown('**Objetivos**')

st.markdown(":male-detective::mag_right::bar_chart: Desarrollar un Análisis Exploratorio de los datos (EDA) con el fin de comprender mejor los datos y encontrar patrones, outliers y/o anomalías.")

st.markdown(":computer::male-technologist::rocket: Desarrollar un Dashboard funcional usando [streamlit](https://streamlit.io/) y coherente con el análisis y la historia que queríamos relatar")

st.markdown(":chart_with_upwards_trend::chart_with_downwards_trend::handshake: Elaborar gráficos interactivos que nos permiten ver la variación de precios en el tiempo, comparar entre distintas acciones, cálculo de estadísticas bursátiles y recomendaciones basadas en el retorno y riesgo de inversión.")

st.markdown(":bar_chart::chart_with_upwards_trend::busts_in_silhouette: Proponer 3 KPIs en el desarrollo del Dashboard y deben estar relacionados con la historia que se va a contar.")


option = st.selectbox('Selecciona la compañía', ('MTD','AVGO','NVR'))

df = pd.read_parquet(f'data/inv_companies/{option.lower()}.parquet')
col1, col2, col3 = st.columns(3)
with col1:
    period_time= 'anual'
    kpi1_value = calc_volatility(df, f'{period_time}')
    st.metric(label=f"Volatilidad {period_time}", value=str(round(kpi1_value * 100, 2)) + " %")
with col2:
    kpi2_value = calc_agr(df)
    st.metric(label=f"Crecimiento promedio anual (AGR)", value=str(round(kpi2_value * 100, 2)) + " %")
    
with col3:
    period_time= '1y'
    kpi3_value = calculate_cumulative_return(df, F'{period_time}')
    st.metric(label=f"Rendimiento acumulado", value=str(round(kpi3_value * 100, 2)) + " %")

# Mostrar la imagen con personalización
st.image('assets/treplot_sp500.png')



# Información personal
st.markdown("""<p align="left"><b>Acerca del proyecto:</b></p>""",unsafe_allow_html=True)
st.markdown("""
<style>
    p {
        padding-top: 0;
        margin: 0;
    }
    p < b {
        padding-bottom: 0;
        margin: 0;
    }
    a {
        text-decoration: none;
    }
    a:hover {
        text-decoration: none;
    }
    
    .icon {
    transition: transform 0.5s;
    }

    .icon:hover {
    transform: scale(1.5);
    }
""", unsafe_allow_html=True)

st.write('<p align="center">Puedes revisar el repositorio de este proyecto <a href="https://github.com/royquillca/pida_henry">Proyecto Individual de Data Analytics (PIDA)</a>. Así mismo, te invito a que revises mis proyectos personales accediendo a mi <a href="https://royquillca.github.io/portafolio/">Portafolio</a></p>', unsafe_allow_html=True)