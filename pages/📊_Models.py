
import streamlit as st

from visual.simple_regression import SimpleRegressionPage


class Home:
    def __init__(self):
        st.write("""
                 # Modelos Basicos
                 
                 """)


page_names_to_funcs = {
    "—": Home,
    "Simple Regression": SimpleRegressionPage,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()