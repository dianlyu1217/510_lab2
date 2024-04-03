import streamlit as st

st.set_page_config(
    page_title = "Penguins Explorer",
    page_icon = "xxx"
    
)

st.title("Penguins Explorer")


# app.py
import streamlit as st
import pandas as pd
import seaborn as sns



st.title("🐧 Penguins Explorer")

df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

st.write(df)

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Title and Introduction
st.title("Penguin Dataset Analysis")
st.write("This web app explores the Palmer Penguins dataset, visualizing characteristics of penguin species from Palmer Archipelago in Antarctica.")

# Data Filtering Widgets
species = st.sidebar.selectbox("Select Species", options=data["species"].unique())
island = st.sidebar.selectbox("Select Island", options=data["island"].unique())
sex = st.sidebar.selectbox("Select Sex", options=data["sex"].dropna().unique())

# Filter Data
filtered_data = data[(data["species"] == species) & (data["island"] == island) & (data["sex"] == sex)]

# Display Data
st.write("Filtered Data", filtered_data)

# Visualizations
st.header("Data Visualizations")

# Distribution of Flipper Length
fig, ax = plt.subplots()
sns.histplot(filtered_data["flipper_length_mm"].dropna(), kde=True, ax=ax)
ax.set_title("Flipper Length Distribution")
st.pyplot(fig)

# Scatter plot of Body Mass vs. Flipper Length
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x="flipper_length_mm", y="body_mass_g", hue="species", style="sex", ax=ax)
ax.set_title("Body Mass vs. Flipper Length by Species and Sex")
st.pyplot(fig)

import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Sidebar Widgets for filtering
species = st.sidebar.selectbox("Choose a Species", options=data["species"].unique(), index=0)
sex = st.sidebar.selectbox("Choose Sex", options=["All"] + list(data["sex"].dropna().unique()))

# Flipper Length Slider
min_length, max_length = int(data["flipper_length_mm"].min()), int(data["flipper_length_mm"].max())
slider = st.slider("Select Flipper Length Range", min_value=min_length, max_value=max_length, value=(min_length,max_length))
filtered_data = data[(data["flipper_length_mm"] >= slider[0]) & (data["flipper_length_mm"] <= slider[1])]

if sex != "All":
    filtered_data = filtered_data[filtered_data["sex"] == sex]

if species:
    filtered_data = filtered_data[filtered_data["species"] == species]

# Display
st.write(f"Number of Penguins: {len(filtered_data)}")
st.write(filtered_data)
