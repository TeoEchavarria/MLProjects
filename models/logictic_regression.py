from sklearn.model_selection import train_test_split

import seaborn as sns

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import streamlit as st

class LogisticRegression:
    def __init__(self, dataset, x_col, y_col):
        X = dataset[x_col].values
        y = dataset[y_col].values
                
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
        
        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_train = sc_X.fit_transform(X_train)
        X_test = sc_X.transform(X_test)
        
        # Ajustar el modelo de Regresión Logística en el Conjunto de Entrenamiento
        from sklearn.linear_model import LogisticRegression
        classifier = LogisticRegression(random_state = 0)
        classifier.fit(X_train, y_train)

        # Predicción de los resultados con el Conjunto de Testing
        y_pred  = classifier.predict(X_test)
        
        
        col1, col2 = st.columns(2)
        
        # Representación gráfica de los resultados del algoritmo en el Conjunto de Entrenamiento
        from matplotlib.colors import ListedColormap
        X_set, y_set = X_train, y_train
        
        fig, ax = plt.subplots()
        
        X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                            np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
        ax.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                    alpha = 0.75, cmap = ListedColormap(('red', 'green')))
        plt.xlim(X1.min(), X1.max())
        plt.ylim(X2.min(), X2.max())
        for i, j in enumerate(np.unique(y_set)):
            ax.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                        c = ListedColormap(('red', 'green'))(i), label = j)
        plt.title('Clasificador (Conjunto de Entrenamiento)')
        plt.xlabel('Edad')
        plt.ylabel('Sueldo Estimado')
        plt.legend()
        
        with col1:
            st.pyplot(fig)


        # Representación gráfica de los resultados del algoritmo en el Conjunto de Testing
        X_set, y_set = X_test, y_test
        fig, ax = plt.subplots()
        X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                            np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
        ax.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                    alpha = 0.75, cmap = ListedColormap(('red', 'green')))
        plt.xlim(X1.min(), X1.max())
        plt.ylim(X2.min(), X2.max())
        for i, j in enumerate(np.unique(y_set)):
            ax.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                        c = ListedColormap(('red', 'green'))(i), label = j)
        plt.title('Clasificador (Conjunto de Test)')
        plt.xlabel('Edad')
        plt.ylabel('Sueldo Estimado')
        plt.legend()
        
        with col2:
            st.pyplot(fig)
                                