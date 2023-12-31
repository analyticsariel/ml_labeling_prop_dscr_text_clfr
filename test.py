import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read().iloc[:,:13]
st.write(df.head())
st.write(conn.client.open('ml_training_prop_cond_dscr_20231228').sheet1)
st.write(dir(conn))