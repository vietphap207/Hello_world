import streamlit as st
import pandas as pd
import numpy as np
st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

