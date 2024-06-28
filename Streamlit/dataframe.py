import streamlit as st
import pandas as pd
import numpy as np

df = np.zeros([5, 3])
df = pd.DataFrame(df).replace({0: np.nan})

df = st.data_editor(df)

