import streamlit as st
import plotly.express as px
import pandas as pd

data = pd.read_csv('happy.csv')

fields = data.columns[1:]

st.title('In Search for Happiness')
x_axis = st.selectbox('Input data for x-axis', fields, index=1)
y_axis = st.selectbox('Input data for y-axis', fields, index=1)
st.subheader(f"{x_axis} and {y_axis}")

figure = px.scatter(x=data[x_axis], y=data[y_axis], labels={'x': x_axis, 'y': y_axis})
st.plotly_chart(figure)
