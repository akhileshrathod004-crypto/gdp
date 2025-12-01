import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="India GDP Dashboard",
    page_icon="💹",
    layout="centered"
)

# ---------- CSS: Dark blue + glowing text ----------
st.markdown("""
<style>
body {
    background-color: #0a0a3f !important;
}
[data-testid="stAppViewContainer"] {
    background-color: #0a0a3f !important;
}

.glow-header {
    color: #ff4c4c;
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    text-shadow: 0 0 5px #ff4c4c, 0 0 10px #ff4c4c, 0 0 20px #ff4c4c;
}

.glow-subheader {
    color: #ffffff;
    font-size: 20px;
    text-align: center;
    text-shadow: 0 0 5px #ffffff, 0 0 10px #ffffff, 0 0 20px #ffffff;
}

.glow-footer {
    color: #ffff4c;
    font-size: 16px;
    text-align: center;
    text-shadow: 0 0 5px #ffff4c, 0 0 10px #ffff4c, 0 0 20px #ffff4c;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<h1 class="glow-header">🇮🇳 India GDP Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="glow-subheader">GDP Visualization for 2022, 2023, and 2024</p>', unsafe_allow_html=True)

# ---------- GDP DATA ----------
data = {
    "Year": [2022, 2023, 2024],
    "GDP (USD Trillion)": [3.73, 4.07, 4.45]  # Example GDP numbers
}
df = pd.DataFrame(data)

# ---------- PLOTLY BAR CHART ----------
fig = px.bar(
    df,
    x="Year",
    y="GDP (USD Trillion)",
    text="GDP (USD Trillion)",
    title="India GDP (2022-2024)",
    color="GDP (USD Trillion)",
    color_continuous_scale=px.colors.sequential.Blues
)
fig.update_layout(
    plot_bgcolor='#0a0a3f',
    paper_bgcolor='#0a0a3f',
    font_color='white',
    title_font_color='yellow'
)
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

st.plotly_chart(fig, use_container_width=True)

# ---------- FOOTER ----------
st.markdown('<p class="glow-footer">Data Source: IMF / Estimates</p>', unsafe_allow_html=True)
