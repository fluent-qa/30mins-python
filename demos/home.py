import numpy as np
import pandas as pd
import streamlit as st

st.write("Hello Streamlit App")
st.write("## First Application")

x = st.text_input("Movie", "Star Wars")
if st.button("Submit"):
    st.write(f"your favorite movie is {x}")

data = pd.read_csv("../data/movies.csv")
st.write(data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)
