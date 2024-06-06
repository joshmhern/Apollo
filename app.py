import streamlit as st
import pandas as pd
import numpy as np



st.write("""
    # The Grey Wolf Group Crime Model:wolf:
    ##### This model is showcases future crime prediction by crime category
         
         """)

df = pd.read_csv('Atlanta Crime December 2023 Predictions.csv')



category_filter = st.multiselect('Crime Category', options=list(df['Type'].unique()), default=list(df['Type'].unique()))

filtered_data = df[df['Type'].isin(category_filter)]

#st.write(filtered_data)


import plotly.express as px

st.write("""
    #### Crime Volume by Type and Date
         
         """)

fig = px.line(filtered_data, x= 'Date', y='Prediction', color = 'Type')


st.plotly_chart(fig)

st.write("""
         
    #### Crime Volume by Type    
         """)

bar = px.bar(filtered_data, x='Type', y='Prediction', color='Type')
st.plotly_chart(bar)

## Crime Count by Day of Week, Bar Chart
st.write("""
         
         #### Crime Volume by Day of the Week
        The day of the week with Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6
         """)
day = px.bar(filtered_data, x='Day_of_Week', y='Prediction', color='Day_of_Week')
st.plotly_chart(day)


## Crime Count by Neighborhood and Date
orig_df = pd.read_csv('atlcrime.csv', low_memory= False)

dates = orig_df[orig_df["date"].isin(['12/1/2010', '12/2/2010','12/3/2010','12/4/2010','12/5/2010','12/6/2010','12/7/2010','12/8/2010','12/9/2010','12/10/2010'])]

category_filter = st.multiselect('Date', options=list(dates['date'].unique()), default=list(dates['date'].unique()))
#date  = orig_df['date']


filtered_data = dates[dates['date'].isin(category_filter)]
st.write("""
         
         #### Crime Volume by Neighborhood
         """)
neighborhood_bar = px.bar(filtered_data, x='neighborhood', y='neighborhood', color='neighborhood')
st.plotly_chart(neighborhood_bar)
