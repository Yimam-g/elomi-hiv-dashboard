import streamlit as st
import pandas as pd
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://kipfbkztkdsvleloskma.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtpcGZia3p0a2RzdmxlbG9za21hIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE1ODYwMDksImV4cCI6MjA2NzE2MjAwOX0.v2bvnrH1whVh-lDMR5HLaxk91UHdS3cI9wQYah5ZsZg"

# Initialize client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="HIV Dashboard", layout="wide")
st.title("📊 Elomi HIV Data Dashboard")

# Load data from Supabase
response = supabase.table("HIV_Record").select("*").execute()

if response.data:
    df = pd.DataFrame(response.data)

    st.subheader("🔍 Data Preview")
    st.dataframe(df)

    if 'hiv_status' in df.columns:
        st.subheader("🧪 HIV Status Distribution")
        st.bar_chart(df['hiv_status'].value_counts())

    if 'region' in df.columns:
        st.subheader("🌍 Regional Breakdown")
        st.bar_chart(df['region'].value_counts())

    if 'gender' in df.columns:
        st.subheader("👤 Gender Distribution")
        st.bar_chart(df['gender'].value_counts())

    if 'age' in df.columns:
        st.subheader("📈 Age Distribution")
        st.line_chart(df['age'].value_counts().sort_index())
else:
    st.error("❌ No data returned from Supabase.")