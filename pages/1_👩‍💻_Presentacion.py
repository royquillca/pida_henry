import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

import streamlit as st
from utils.kpis import calc_volatility, calc_agr, calculate_cumulative_return
# from utils.

st.subheader('**Análisis de inversión en el mercado bursátil**')
# st.markdown('**Descripción del problema**')
# st.markdown('**Objetivos**')



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
st.markdown("""<p align="center"><b>Sígueme en mis redes sociales en:</b></p>""",unsafe_allow_html=True)
st.markdown("""
<style>
    .social-media {
        display:flex;
        justify-content: space-between;
        # justify-content: center;
        # justify-content: space-around;
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
    
</style>
<div class="social-media">
    <a href="https://github.com/royquillca" target="blank">
        <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="royquillca" height="15" width="20" class="icon"> royquillca
    </a>
    <a href="https://linkedin.com/in/royquillca" target="blank">
        <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="royquillca" height="15" width="20" class="icon"> royquillca
    </a>
    <a href="https://www.instagram.com/royquillca/" target="blank">
        <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="@royquillca" height="15" width="20" class="icon"> @royquillca
    </a>
    <a href="https://www.youtube.com/@royquillca" target="blank">
        <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="@roquidev" height="15" width="20" class="icon"> @royquillca
    </a>
    <a href="https://twitter.com/royquillca" target="blank" >
        <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="royquillca" height="15" width="20" class="icon"> @royquillca
    </a>
</div>
""", unsafe_allow_html=True)

st.write('<p align="center">Puedes revisar mis proyectos personales accediendo al link: <a href="https://royquillca.github.io/portafolio/">Portafolio</a></p>', unsafe_allow_html=True)