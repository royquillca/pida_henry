import streamlit as st
import pandas as pd

from utils.kpis import calc_volatility, calc_agr, calculate_cumulative_return
from utils.companies_inv import plot_anual_performance, plot_boxplot, plot_candlestick_chart

st.title('KPIs para empresas seleccionadas')

# "MTD" : "Mettler-Toledo International Inc. (MTD)",
# "AVGO" : "Broadcom Inc. (AVGO)",
# "NVR, Inc. (NVR)" : "NVR, Inc. (NVR)"


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

fit_price_time_series = plot_candlestick_chart(option)
st.plotly_chart(fit_price_time_series, config=dict(displayModeBar=False), use_container_width=True)


fig_box_plot_distr = plot_boxplot(option)
st.plotly_chart(fig_box_plot_distr, config=dict(displayModeBar=False), use_container_width=True)

fig_anual_performance = plot_anual_performance(option)
st.plotly_chart(fig_anual_performance, config=dict(displayModeBar=False), use_container_width=True)

