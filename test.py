import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
st.write(dir(conn))
df = conn.read().iloc[:,:13]
st.write(df.head())
try:
    st.write('spreadsheet', conn._spreadsheet)
except:
    st.write('spreadsheet', conn._spreadsheet())
try:
    st.write('client1', conn.client)
except:
    st.write('client2', conn.client())
st.write('worksheet', conn._worksheet)
st.write(conn.client().open('ml_training_prop_cond_dscr_20231228').sheet1)
