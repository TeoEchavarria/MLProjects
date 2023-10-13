from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

import numpy as np

class PolynomialRegression:   
    def __init__(self, dataset, x_col, y_col, grate):

            X = dataset[x_col].values
            y = dataset[y_col].values
                    
            poly_reg = PolynomialFeatures(degree = grate+1)
            
            X_poly = poly_reg.fit_transform(X.reshape(-1, 1))
            
            lin_reg_2 = LinearRegression()
            lin_reg_2.fit(X_poly, y)
            
            X_grid = np.arange(min(X), max(X), 0.1)
            X_grid = X_grid.reshape(len(X_grid), 1)

            y_pred = lin_reg_2.predict(poly_reg.fit_transform(X_grid))
            
            train_data = pd.DataFrame({x_col :X.tolist(), y_col : y.tolist()})
            
            predict_data =  pd.DataFrame({ x_col : X_grid.reshape(1, -1)[0], y_col : y_pred.tolist()})
            

            fig, ax = plt.subplots()
            sns.scatterplot(x=x_col, y=y_col, data= train_data, color = "m")
            sns.lineplot(x=x_col, y= y_col, color='black', data= predict_data)
            plt.xlabel("Experience")
            plt.ylabel("salary")
            st.pyplot(fig)
