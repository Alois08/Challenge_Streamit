#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title('Dataset des Voitures')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars


regions = df_cars['continent'].unique()
selected_region = st.sidebar.selectbox('Sélectionner une région', regions)

filtered_df = df_cars[df_cars['continent'] == selected_region]


st.subheader(f'Données pour la région sélectionnée : {selected_region}')
st.write(filtered_df)


# In[16]:

st.subheader('Pairplot')
viz_pairplot = sns.pairplot(df_cars.sample(frac=0.1))
st.pyplot(viz_pairplot)


# In[10]:

st.subheader('Heatmap')

heatmap_fig, ax = plt.subplots()
sns.heatmap(df_cars.corr(),center=0, annot=True, cmap="coolwarm", ax=ax)

st.pyplot(heatmap_fig)


pos_corr_vars = df_cars.corr().unstack().sort_values(ascending=False).drop_duplicates().head(2)
st.write(f'Les deux variables les plus corrélées positivement : {pos_corr_vars.index[0]} et {pos_corr_vars.index[1]}')


neg_corr_vars = df_cars.corr().unstack().sort_values().drop_duplicates().head(2)
st.write(f'Les deux variables les plus corrélées négativement : {neg_corr_vars.index[0]} et {neg_corr_vars.index[1]}')
