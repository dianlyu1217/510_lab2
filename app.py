import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Boston House Explorer",
    page_icon="🏠"
)


def load_data():
    url = "BostonHousing.csv"
    data = pd.read_csv(url)
    return data


def descript():
    st.title("BostonHousing Dataset Analysis")
    st.write("This web app explores and visually analyzes the BostonHousing dataset")
    with st.expander("Click to see detailed dataset description"):
        st.write("""
        CRIM - per capita crime rate by town\n
        ZN - proportion of residential land zoned for lots over 25,000 sq.ft.\n
        INDUS - proportion of non-retail business acres per town.\n
        CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)\n
        NOX - nitric oxides concentration (parts per 10 million)\n
        RM - average number of rooms per dwelling\n
        AGE - proportion of owner-occupied units built prior to 1940\n
        DIS - weighted distances to five Boston employment centres\n
        RAD - index of accessibility to radial highways\n
        TAX - full-value property-tax rate per $10,000\n
        PTRATIO - pupil-teacher ratio by town\n
        B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town\n
        LSTAT - % lower status of the population\n
        MEDV - Median value of owner-occupied homes in $1000's
        """)


data = load_data()

# slider filter
st.sidebar.header("Filter Options")
crimMin, crimMax = int(data["crim"].min()), int(data["crim"].max())  # 犯罪率
slider = st.sidebar.slider("Crime Rate", min_value=crimMin, max_value=crimMax, value=(crimMin, crimMax))
filtered_data = data[(data["crim"] >= slider[0]) & (data["crim"] <= slider[1])]

# select filter
chas = st.sidebar.selectbox("Charles River dummy variable", options=["All"] + list(data["chas"].unique()))  # 是否临河
if chas != "All":
    filtered_data = filtered_data[filtered_data["chas"] == chas]
rad = st.sidebar.selectbox("Accessibility to Radial Highways",
                           options=["All"] + list(data["rad"].unique()))  # 辐射状公路可达性指数
if rad != "All":
    filtered_data = filtered_data[filtered_data["rad"] == rad]
age = st.sidebar.selectbox("Age of Home Range",
                           options=["All"] + ["0+"] + ["10+"] + ["20+"] + ["30+"] + ["40+"] + ["50+"] + ["60+"] + [
                               "70+"] + ["80+"] + ["90+"])  # 房龄
if age == "All":
    pass
elif age == "0+":
    filtered_data = filtered_data[(filtered_data["age"] >= 0) & (filtered_data["age"] < 10)]
elif age == "10+":
    filtered_data = filtered_data[(filtered_data["age"] >= 10) & (filtered_data["age"] < 20)]
elif age == "20+":
    filtered_data = filtered_data[(filtered_data["age"] >= 20) & (filtered_data["age"] < 30)]
elif age == "30+":
    filtered_data = filtered_data[(filtered_data["age"] >= 30) & (filtered_data["age"] < 40)]
elif age == "40+":
    filtered_data = filtered_data[(filtered_data["age"] >= 40) & (filtered_data["age"] < 50)]
elif age == "50+":
    filtered_data = filtered_data[(filtered_data["age"] >= 50) & (filtered_data["age"] < 60)]
elif age == "60+":
    filtered_data = filtered_data[(filtered_data["age"] >= 60) & (filtered_data["age"] < 70)]
elif age == "70+":
    filtered_data = filtered_data[(filtered_data["age"] >= 70) & (filtered_data["age"] < 80)]
elif age == "80+":
    filtered_data = filtered_data[(filtered_data["age"] >= 80) & (filtered_data["age"] < 90)]
elif age == "90+":
    filtered_data = filtered_data[(filtered_data["age"] >= 90) & (filtered_data["age"] < 100)]

# Show Data Set
descript()
originData, filteredDate = st.columns(2)  # Creates two columns
with originData:
    st.header("Origin Dataset")
    st.write(data)
    st.download_button(
        label="Download Origin Dataset",
        data=data.to_csv(index=False).encode('utf-8'),
        file_name='origin_data.csv',
        mime='text/csv',
        on_click=None,
        args=None,
        kwargs=None,
        disabled=False,
        key=None
    )
with filteredDate:
    st.header("Filtered Dataset")
    st.write(filtered_data)
    st.download_button(
        label="Download Filtered Dataset",
        data=filtered_data.to_csv(index=False).encode('utf-8'),
        file_name='filtered_data.csv',
        mime='text/csv',
        on_click=None,
        args=None,
        kwargs=None,
        disabled=False,
        key=None
    )
# Show Data Visualize
fig1, ax1 = plt.subplots()
sns.histplot(filtered_data["crim"].dropna(), kde=True, ax=ax1)
ax1.set_title("Crim Distribution")

fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_data, x="rm", y="medv", ax=ax2)
ax2.set_title("Median House Value vs. Average Number of Rooms")
ax2.set_xlabel("Average Number of Rooms (RM)")
ax2.set_ylabel("Median Value of Owner-Occupied Homes (MEDV, $1000's)")

st.header("Data Visualizations")
figL, figR = st.columns(2)
with figL:
    st.pyplot(fig1)
with figR:
    st.pyplot(fig2)