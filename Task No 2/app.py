import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

st.title("📊 Global Superstore Business Dashboard")

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("D:\Internship\Task No 2\Datasets/superstore.csv", encoding='latin1')
    return df

df = load_data()

# -------------------------
# DATA CLEANING
# -------------------------
df.dropna(inplace=True)

# Convert date columns
df['Order.Date'] = pd.to_datetime(df['Order.Date'])
df['Ship.Date'] = pd.to_datetime(df['Ship.Date'])

# -------------------------
# SIDEBAR FILTERS
# -------------------------
st.sidebar.header("🔍 Filters")

region = st.sidebar.multiselect("Select Region", df['Market'].unique(), default=df['Market'].unique())
category = st.sidebar.multiselect("Select Category", df['Category'].unique(), default=df['Category'].unique())
subcategory = st.sidebar.multiselect("Select Sub-Category", df['Sub.Category'].unique(), default=df['Sub.Category'].unique())

# Apply filters
filtered_df = df[
    (df['Market'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub.Category'].isin(subcategory))
]

# -------------------------
# KPIs
# -------------------------
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()

col1, col2 = st.columns(2)

col1.metric("💰 Total Sales", f"{total_sales:,.0f}")
col2.metric("📈 Total Profit", f"{total_profit:,.0f}")

# -------------------------
# TOP 5 CUSTOMERS
# -------------------------
st.subheader("🏆 Top 5 Customers by Sales")

top_customers = (
    filtered_df.groupby('Customer.Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

fig, ax = plt.subplots()
top_customers.plot(kind='bar', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# -------------------------
# CATEGORY SALES
# -------------------------
st.subheader("📦 Sales by Category")

category_sales = filtered_df.groupby('Category')['Sales'].sum()

fig2, ax2 = plt.subplots()
category_sales.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# -------------------------
# PROFIT BY SUB-CATEGORY
# -------------------------
st.subheader("📊 Profit by Sub-Category")

profit_subcat = filtered_df.groupby('Sub.Category')['Profit'].sum().sort_values()

fig3, ax3 = plt.subplots(figsize=(10,5))
profit_subcat.plot(kind='barh', ax=ax3)
st.pyplot(fig3)