import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config(
    page_title="AI Opportunity Intelligence Platform",
    layout="wide"
)

st.title("🚀 AI-Powered Infrastructure Opportunity Intelligence Platform")

conn = psycopg2.connect(
    database="opportunity_intelligence_db",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)

query = """
SELECT project_name,
       location,
       score
FROM opportunities
"""

df = pd.read_sql(query, conn)

st.subheader("Opportunity Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Opportunities", len(df))

with col2:
    st.metric("Average Score", round(df["score"].mean(), 2))

st.subheader("Opportunity Data")

st.dataframe(df)

conn.close()