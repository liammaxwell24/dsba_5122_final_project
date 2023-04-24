import streamlit as st
import pandas as pd
import altair as alt
import numpy as np


contract_data = pd.read_csv('DSBA 5122_NBA Contracts Data_v4.csv')

contract_data.drop(['signed','extended'],axis=1)

st.set_page_config(layout="wide")

st.title('NBA Contract Data')

st.markdown(
"**Statistics for all NBA Players not on rookie contracts for the 2022 NBA Season.**\n"
)

tab1, tab2 = st.tabs(['Scatter Plot', 'Bar Chart'])


with tab1:
    player = st.multiselect('Select an NBA player', contract_data['name'])
    filtered_contract_data = contract_data[contract_data['name'].isin(player)]


    st.dataframe(filtered_contract_data)

    st.sidebar.header("Pick two player attributes for your scatterplot")
    x_val = st.sidebar.selectbox("Pick your x-axis",filtered_contract_data.select_dtypes(include=np.number).drop(['signed','extended','age at signing/extension','offseason_of_new_contract'], axis=1).columns.tolist())
    y_val = st.sidebar.selectbox("Pick your y-axis",filtered_contract_data.select_dtypes(include=np.number).drop(['signed','extended','age at signing/extension','offseason_of_new_contract'], axis=1).columns.tolist())

    scatter = alt.Chart(filtered_contract_data, title=f"{x_val} and {y_val}").mark_point().encode(
        alt.X(x_val,title=f'{x_val}'),
        alt.Y(y_val,title=f'{y_val}'),
        tooltip=['name','new_contract_AAV',x_val, y_val]).configure_mark(
        opacity=0.5,
        color='blue')
    st.altair_chart(scatter, theme="streamlit", use_container_width=True)
    
with tab2:
    st.sidebar.header("Pick a player attribute for your bar chart")
    z_val = st.sidebar.selectbox("Pick your attribute",filtered_contract_data.select_dtypes(include=np.number).drop(['signed','extended','age at signing/extension','offseason_of_new_contract'], axis=1).columns.tolist())
    count = st.sidebar.slider("Top K Values",min_value=5, max_value=100, value=40, step=10)
    
    bar = alt.Chart(contract_data).mark_bar().encode(y = alt.Y('name',title='name', sort = '-x'),
    x = alt.X(z_val,title=f'{z_val}'), tooltip=['name',z_val,'new_contract_AAV']).transform_window(
    rank='rank(z_val)',
    ).transform_filter(
    (alt.datum.rank < count)
    )
    

    st.altair_chart(bar, use_container_width=True) 
