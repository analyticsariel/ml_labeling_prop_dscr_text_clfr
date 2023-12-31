import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read().iloc[:,:13]
st.write(df.head())
st.write(dir(conn))