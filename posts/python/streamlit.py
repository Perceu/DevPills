"""
pip install streamlit

streamlit run run.py
"""

import streamlit as st
import pandas as pd

st.write("""
# Hello World
""")

chart_data = pd.DataFrame(
    data=[[15],[30],[90]],
    columns=['dias']
)

st.bar_chart(chart_data)