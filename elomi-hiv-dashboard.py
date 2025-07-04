import streamlit as st
import pandas as pd
from supabase import create_client, Client
from datetime import datetime

# Supabase credentials
SUPABASE_URL = "https://kipfbkztkdsvleloskma.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtpcGZia3p0a2RzdmxlbG9za21hIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE1ODYwMDksImV4cCI6MjA2NzE2MjAwOX0.v2bvnrH1whVh-lDMR5HLaxk91UHdS3cI9wQYah5ZsZg"
TABLE_NAME = "HIV_Record"

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Streamlit page setup
st.set_page_config(page_title="📊 Elomi HIV Dashboard", layout="wide")
st.title("📊 Elomi HIV Data Dashboard")

# Load data
response = supabase.table(TABLE_NAME).select("*").execute()

if not response.data:
    st.error("❌ No data returned from Supabase.")
    st.stop()

# Convert to DataFrame
df = pd.DataFrame(response.data)

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
region_filter = st.sidebar.selectbox("Region", ["All"] + sorted(df["region"].dropna().unique()))
gender_filter = st.sidebar.selectbox("Gender", ["All"] + sorted(df["gender"].dropna().unique()))
status_filter = st.sidebar.selectbox("HIV Status", ["All"] + sorted(df["hiv_status"].dropna().unique()))

# Filter the data
filtered_df = df.copy()
if region_filter != "All":
    filtered_df = filtered_df[filtered_df["region"] == region_filter]
if gender_filter != "All":
    filtered_df = filtered_df[filtered_df["gender"] == gender_filter]
if status_filter != "All":
    filtered_df = filtered_df[filtered_df["hiv_status"] == status_filter]

# Summary statistics
st.markdown("### 📌 Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(filtered_df))
col2.metric("HIV Positive", (filtered_df["hiv_status"] == "Positive").sum())
col3.metric("HIV Negative", (filtered_df["hiv_status"] == "Negative").sum())

# Charts
st.markdown("### 📊 Visualizations")
if "hiv_status" in filtered_df.columns:
    st.bar_chart(filtered_df["hiv_status"].value_counts())
if "region" in filtered_df.columns:
    st.bar_chart(filtered_df["region"].value_counts())
if "gender" in filtered_df.columns:
    st.bar_chart(filtered_df["gender"].value_counts())
if "age" in filtered_df.columns:
    st.line_chart(filtered_df["age"].value_counts().sort_index())

# Editable data table
st.markdown("### 🧾 Data Table")
st.data_editor(filtered_df, use_container_width=True, num_rows="dynamic")

# Download button
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_hiv_data.csv",
    mime="text/csv"
)
