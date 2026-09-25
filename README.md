# My First Streamlit App

My first Streamlit app. It was built as a homework exercise to learn the basics: displaying dataframes, writing markdown, showing code, and rendering Altair charts.

## What it does

`app.py` ("Homework 1") walks through four questions:

1. Create a dataframe with an x axis from 0 to 100 and random y values, and display it.
2. Plot a basic Altair scatterplot of that dataframe.
3. Improve the scatterplot with five documented changes: tooltips, square marks, title/size/color encoding, a mean rule on the x-axis, and a median rule on the y-axis.
4. Build an interactive bubble chart from the vega_datasets cars dataset (Horsepower vs. Miles per Gallon, sized by Acceleration).

## Install and run

```bash
git clone https://github.com/suhasaitham22/my_first_streamlit_app.git
cd my_first_streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

## Tech stack

Streamlit, Altair, pandas, NumPy, vega_datasets.
