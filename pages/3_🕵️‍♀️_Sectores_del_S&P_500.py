from utils.sp500_sector import price_trend_plot, plot_close_price_ts
import streamlit as st
import pandas as pd


dict_data = {
    "consumer_discretionary": pd.read_parquet('data/consumer_discretionary.parquet').reset_index(),
    "consumer_staples": pd.read_parquet('data/consumer_staples.parquet').reset_index(),
    "energy": pd.read_parquet('data/energy.parquet').reset_index(),
    "financials": pd.read_parquet('data/financials.parquet').reset_index(),
    "health_care": pd.read_parquet('data/health_care.parquet').reset_index(),
    "industrial": pd.read_parquet('data/industrial.parquet').reset_index(),
    "information_technology": pd.read_parquet('data/information_technology.parquet').reset_index(),
    "materials": pd.read_parquet('data/materials.parquet').reset_index(),
    "utilities": pd.read_parquet('data/utilities.parquet').reset_index(),
}

# Transformaciones
for df_name, df in zip(dict_data.keys(), dict_data.values()):
    # Conversion del tipo str a datetime de la varibale Date
    df['Date'] = pd.to_datetime(df['Date'])
    dict_data[df_name] = df
    



st.markdown('<h4 align="center">Análisis de inversión sectorial del S&P 500</h4>', unsafe_allow_html=True)




fig_ts = plot_close_price_ts(dict_data)
fig_ts.update_layout(title={'text': 'Evolución del precio de cierre ajustado de los 10 sectores del S&P 500'})
st.plotly_chart(fig_ts, config=dict(displayModeBar=False), use_container_width=True)

sector_option = st.selectbox('**Sector del S&P 500**', ('Consumer Discretionary',
                                  'Consumer Staples',
                                  'Energy',
                                  'Financials',
                                  'Health Care',
                                  'Industrial',
                                  'Information_technology',
                                  'Materials',
                                  'Utilities'))

fig_trend = price_trend_plot(sector_option)
fig_ts.update_layout(title={'text': f'Evolución del precio de cierre ajustado de los 10 sectores del S&P 500 {sector_option.replace("_", " ")}', 'x':0})
# fig_trend.update_layout(title={'text': sector_option, })
st.plotly_chart(fig_trend, config=dict(displayModeBar=False), use_container_width=True)