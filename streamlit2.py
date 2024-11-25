import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px


st.title("Manipulation de données et creation de graphique")
choix= st.selectbox('quel dataset souhaites tu utiliser ? ', sns.get_dataset_names())
for i in sns.get_dataset_names():
    if choix == i:
        data=sns.load_dataset(i)
        st.dataframe(data)
        choix_1= st.selectbox('choisissez la colonne x ',data.columns)
        choix_2= st.selectbox('choisissez la colonne y ',data.columns)
        choix_graphique= st.selectbox('quel graphique veux tu voir ? ', ['scatter_chart','bar_chart','line_chart'])
        if choix_graphique== 'scatter_chart' :
                st.scatter_chart(x= choix_1, y=choix_2,data= data)
        elif choix_graphique== 'bar_chart' :
                st.bar_chart(x= choix_1, y=choix_2,data= data)
        else:
                st.line_chart(x= choix_1, y=choix_2,data= data)
matrice_corr= st.checkbox("Matrice de correlation")
if matrice_corr:
    
    numeric_data = data.select_dtypes(include=[np.number])  

    if not numeric_data.empty:
        corr_matrix = numeric_data.corr()
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr_matrix)
        st.write(fig)
    else:
        st.error("Il n'y a pas de colonnes numériques pour calculer la matrice de corrélation.")
