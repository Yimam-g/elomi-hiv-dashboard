from supabase import create_client, Client
import streamlit as st
import pandas as pd

# Supabase connection
SUPABASE_URL = "https://kipfbkztkdsvleloskma.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtpcGZia3p0a2RzdmxlbG9za21hIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE1ODYwMDksImV4cCI6MjA2NzE2MjAwOX0.v2bvnrH1whVh-lDMR5HLaxk91UHdS3cI9wQYah5ZsZg"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Streamlit layout
st.set_page_config(page_title="Elomi HIV Data Dashboard", layout="wide")
st.title("📊 Elomi HIV Data Dashboard")

# Fetch data
try:
    response = supabase.table("HIV_Record").select("*").execute()
    data = response.data

    if data:
        df = pd.DataFrame(data)
        st.success(f"✅ Loaded {len(df)} records from Supabase.")
        st.dataframe(df)

        if "hiv_status" in df.columns:
            st.subheader("🧬 HIV Status Distribution")
            st.bar_chart(df["hiv_status"].value_counts())

        if "region" in df.columns:
            st.subheader("🌍 Regional Breakdown")
            st.bar_chart(df["region"].value_counts())

        if "gender" in df.columns:
            st.subheader("👥 Gender Distribution")
            st.bar_chart(df["gender"].value_counts())

    else:
        st.warning("⚠️ Supabase returned no data. Check your table or permissions.")

except Exception as e:
    st.error(f"❌ Error fetching data: {e}")
