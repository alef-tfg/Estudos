import gspread
from oauth2client.service_account import ServiceAccountCredentials

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

@st.cache_data
def get_data():
    scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name("dashboardDieta/macros-key.json", scope)
    client = gspread.authorize(creds)
    print(client.openall())

    Macros = np.array(client.open("Macros Tracker").worksheet("Data(Macros)").get_all_values())
    Medidas = np.array(client.open("Macros Tracker").worksheet("Medidas").get_all_values())
    return Macros, Medidas

Macros, Medidas = get_data()
Macros_totais = [Macros.T [0], *Macros.T[-4:]]
Macros_totais = pd.DataFrame({items[0]: items[1:] for items in Macros_totais})
Macros_totais['Data'] = pd.to_datetime(Macros_totais['Data'])
Macros_totais.set_index('Data', inplace=True)
columns = Macros_totais.columns
Macros_totais = Macros_totais.replace({'': np.nan})
Macros_totais = Macros_totais.astype({c: 'float64' for c in columns})

Macros_week_avg = Macros_totais.resample('W-SAT').sum().map(lambda x: x/7)

options = st.multiselect('Escolha uma variável', Macros_week_avg.columns, 'CALS')

color_map = {"CALS":'slategray',"CARB":'skyblue',"PROT":'tomato', "GORD": 'gold'}

fig_macros_progression = px.line(Macros_week_avg, x=Macros_week_avg.index, y=options, line_shape='spline', color_discrete_map=color_map)
st.plotly_chart(fig_macros_progression)
MedidasDF = pd.DataFrame(Medidas[1:], columns=Medidas[0])
MedidasDF['Data'] = pd.to_datetime(MedidasDF['Data'])
MedidasDF.set_index('Data', inplace=True)
MedidasDF = MedidasDF.replace({'': np.nan})
MedidasDF['Peso_diff'] = MedidasDF.fillna(0)['Peso'].astype(float).diff()
joinedData = Macros_week_avg.join(MedidasDF, how= 'inner').dropna(subset=['Peso'])


fig_correlation = px.scatter(joinedData, y= options, x='Peso_diff', trendline="ols", color_discrete_map=color_map)
st.plotly_chart(fig_correlation)
