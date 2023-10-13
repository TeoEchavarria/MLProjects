import streamlit as st
from models.knn_model import KnnModel
from models.logictic_regression import LogisticRegression
from models.read_csv_model import ReadCsvModel

import pandas as pd 


class ClusteringPage:
    def __init__(self):
        model = st.selectbox("Clustering Models", ["K - Nearest Neighbors", "Logistic Regression"])
        dataset = st.selectbox("DataSet", ["Social Network Ads", "Otro Conjunto de Datos"])
        
        real_name_dataset = {
            "Social Network Ads" : "Social_Network_Ads", 
        }
        
        if dataset == "Otro Conjunto de Datos":
            dataset = ReadCsvModel( st.file_uploader("Otro Documento"), None)
        dataset = ReadCsvModel(real_name_dataset[dataset], "clustering")

        if dataset is not None:
            cols = dataset.columns.tolist()
            
            col1, col2 = st.columns(2)
            x_cols = col1.multiselect('Columnas independientes (X)', cols)
            y_col = col2.selectbox('Columna dependiente (y)', cols)
        
        
        # Models  
        if model == "K - Nearest Neighbors":
            KnnModel(dataset, x_cols, y_col)
        elif model == "Logistic Regression":
            LogisticRegression(dataset, x_cols, y_col)