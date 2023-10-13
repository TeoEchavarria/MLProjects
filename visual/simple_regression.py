import streamlit as st
from models.lineal_model import LinealModel
from models.read_csv_model import ReadCsvModel

import pandas as pd 

class SimpleRegressionPage:
    def __init__(self):
        model = st.selectbox("Simple Models", ["Linear Regression", "Polynomial Regression"])
        dataset = st.selectbox("DataSet", ["Salary Vs Experience", "Otro Conjunto de Datos"])
        
        if dataset == "Otro Conjunto de Datos":
            dataset = ReadCsvModel( st.file_uploader("Otro Documento"), None)
        elif dataset == "Salary Vs Experience":
            dataset = ReadCsvModel("Salary_Data", "simple_regression")
            
        else:
            dataset = None
        
        if dataset is not None:
            cols = dataset.columns.tolist()
            
            if model == "Linear Regression":
                col1, col2 = st.columns(2)
                x_col = col1.selectbox('Columnas independientes (X)', cols)
                y_col = col2.selectbox('Columna dependiente (y)', cols)
            
            
        if st.button("Predecir"):
            LinealModel(dataset, x_col, y_col)

            
