import streamlit as st
from models.lineal_model import LinealModel
from models.polynomial_regression import PolynomialRegression
from models.read_csv_model import ReadCsvModel

import pandas as pd 


class SimpleRegressionPage:
    def __init__(self):
        model = st.selectbox("Simple Models", ["Linear Regression", "Polynomial Regression"])
        dataset = st.selectbox("DataSet", ["Salary Vs Experience", "Position Salaries", "Polynomial Example",  "Otro Conjunto de Datos"])
        
        real_name_dataset = {
            "Salary Vs Experience" : "Salary_Data", 
            "Position Salaries"    : "Position_Salaries", 
            "Polynomial Example"   : "polynomial-regression", 
        }
        
        if dataset == "Otro Conjunto de Datos":
            dataset = ReadCsvModel( st.file_uploader("Otro Documento"), None)
        dataset = ReadCsvModel(real_name_dataset[dataset], "simple_regression")

        if dataset is not None:
            cols = dataset.columns.tolist()
            
            col1, col2 = st.columns(2)
            x_col = col1.selectbox('Columnas independientes (X)', cols)
            y_col = col2.selectbox('Columna dependiente (y)', cols)
        
        if model == "Polynomial Regression":
            grado = st.slider("Grado Polinomico", 0, 10, 5, 1)
        
        
        # Models  
        if model == "Linear Regression":
            LinealModel(dataset, x_col, y_col)
        elif model == "Polynomial Regression":
            PolynomialRegression(dataset, x_col, y_col, grado)


