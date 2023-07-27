import streamlit as st

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image('WHO.jpg')
    with col3:
        st.write(' ')

st.markdown("<h1 style='text-align: center; color: #336699;'>WHO Covid-19 Data Analysis Dashboard</h1>", unsafe_allow_html=True)

# Description
st.header('Description')
st.markdown('''
This app is created to analyze the Covid-19 data.
''')


