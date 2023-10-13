from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

def LinealModel(dataset, x_col, y_col):

        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, 1].values
                
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
        
        regression = LinearRegression()
        
        regression.fit(X_train, y_train)
        
        y_pred = regression.predict(X_test)
        
        train_data = pd.DataFrame({x_col :[i[0] for i in X_train.tolist()], y_col : y_train.tolist()})
        
        test_data = pd.DataFrame({x_col :[i[0] for i in X_test.tolist()], y_col : y_test.tolist()})
        
        predict_data =  pd.DataFrame({ x_col : [i[0] for i  in  X_test.tolist()], y_col : y_pred.tolist()})
        

        fig, ax = plt.subplots()
        sns.scatterplot(x=x_col, y=y_col, data= train_data, color = "m")
        sns.scatterplot(x=x_col, y=y_col, data= test_data, color = "c")
        sns.lineplot(x=x_col, y= y_col, color='black', data= predict_data)
        plt.xlabel("Experience")
        plt.ylabel("salary")
        st.pyplot(fig)
