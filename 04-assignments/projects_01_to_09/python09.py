# %%writefile app.py
# import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)

  st.subheader("Data Preview")
  st.write(df.head())

  st.subheader("Data Summary")
  st.write(df.describe())

  st.subheader("Filtered Data")
  columns = df.columns.tolist()
  selected_columns = st.selectbox("Select column to filter by",columns)

  unique_values = df[selected_columns].unique()
  selected_values = st.selectbox("Select value", unique_values)

  filtered_df = df[df[selected_columns] == selected_values]
  st.write(filtered_df)

  st.subheader("Plot Data")

  x_column = st.selectbox("Select x-axis column", df.columns)
  y_column = st.selectbox("Select y-axis column", df.columns)

  if st.button("Generate Plot"):
    st.line_chart(filtered_df.set_index (x_column)[y_column])
  else:
    st.write("Waiting for file upload")


# from pyngrok import ngrok
# # Terminate open tunnels if exist
# # Set up a new tunnel
# public_url = ngrok.connect(port='8501')
# print(f"Public URL: {public_url}")
# ngrok.kill()
