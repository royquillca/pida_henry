import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

import streamlit as st


st.subheader('**Análisis de inversión en el mercado bursátil**')
st.markdown('**Descripción del problema**')
st.markdown('**Objetivos**')

col1, col2, col3 = st.columns(3)
with col1:
    pass

with col2:
    pass
    
with col3:
    pass



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