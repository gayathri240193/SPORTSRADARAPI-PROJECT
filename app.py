import streamlit as st
import pandas as pd
import pymysql
import plotly.express as px

# --- DATABASE CONNECTION ---
@st.cache_resource
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='game_analytics'
    )

# --- FETCH DATA FROM SQL ---
@st.cache_data
def fetch_table(query):
    conn = get_connection()
    return pd.read_sql(query, conn)

# Load all 6 tables
df_competitors = fetch_table("SELECT * FROM competitors")
df_rankings = fetch_table("SELECT * FROM competitor_rankings")
df_complexes = fetch_table("SELECT * FROM complexes")
df_venues = fetch_table("SELECT * FROM venues")
df_category = fetch_table("SELECT * FROM categories")
df_competition = fetch_table("SELECT * FROM competitions")

# Merge Rankings + Competitors
df_merged = pd.merge(df_rankings, df_competitors, on="competitor_id", how="left")

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filters")
country_list = df_competitors['country'].dropna().unique()
selected_country = st.sidebar.selectbox("Select Country", options=sorted(country_list))

category_list = df_category['category_name'].dropna().unique()
selected_category = st.sidebar.selectbox("Select Category", options=sorted(category_list))

# Filter merged df
filtered_df = df_merged[df_merged['country'] == selected_country]

# --- MAIN LAYOUT ---
st.title("🎾Tennis Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 All Competitor Rankings")
    st.dataframe(df_merged)

with col2:
    st.subheader("🏆 Top 10 Players")
    top10 = df_merged.sort_values("rank").head(10)
    st.dataframe(top10)

# --- EXTRA SECTIONS ---
st.markdown("---")
st.header("📍 Venues & Complexes")

venue_info = pd.merge(df_venues, df_complexes, on="complex_id", how="left")
st.dataframe(venue_info)

st.markdown("---")
st.header("📅 Competitions")

comp_info = pd.merge(df_competition, df_category, on="category_id", how="left")
filtered_comp = comp_info[comp_info['category_name'] == selected_category]
st.dataframe(filtered_comp)

# --- VISUALIZATION ---
st.markdown("---")
st.header("📈 Ranking Distribution")

fig = px.histogram(df_merged, x="country", title="Number of Players per Country", color_discrete_sequence=['#EF553B'])
st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(top10, x='name', y='points', color='points', title='Top 10 Players by Points')
st.plotly_chart(fig2, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("Created with ❤️ by [GAYATHRI.S]")
