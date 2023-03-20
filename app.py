from re import T
from turtle import circle, color, title
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

st.header('Homework 1')

st.markdown(
"*QUESTION 1*: In previous homeworks you created dataframes from random numbers.\n"
"Create a dataframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')
x_limit = 100
x_axis = np.arange(0,x_limit,1)
y_data = np.random.random(100)
df= pd.DataFrame({'x':x_axis,
                    'y':y_data})
st.dataframe(df)                      


st.markdown(
"*QUESTION 2*: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_point(point=True).encode(x = 'x',y = 'y')

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"*QUESTION 3*: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1 : Added Tooltip
- Change 2 : Scatterplot points are changed to squares
- Change 3 : Added Title, Size, Color
- Change 4 : Mean of points on X-axis is added
- Change 5 : Median of points on y-axis is added
""")
scatter = alt.Chart(df, title = 'Scatter Plot').mark_square(clip=True).encode(x = 'x',y = 'y',size = 'y',
                           color = 'x', tooltip = ['x','y'])
median = (alt.Chart(df).mark_rule().encode(y = "median(y):Q" , color=alt.value('red')))

mean = (alt.Chart(df).mark_rule().encode(x = "mean(x):Q" , color=alt.value('white')))
st.altair_chart(scatter+median+mean, use_container_width=True)


st.markdown(
"*QUESTION 4*: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The 2 changes I made were:
- Change 1 : Created interactive graph
- Change 2 : Added color
"""
)
            
source = data.cars()

bubble = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    size='Acceleration',color=alt.value('red'), tooltip = ['Horsepower','Miles_per_Gallon']
).interactive()

st.altair_chart(bubble)
