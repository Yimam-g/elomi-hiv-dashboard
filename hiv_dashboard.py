import streamlit as st
import pandas as pd
from supabase import create_client

# Get from Streamlit secrets
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="HIV Dashboard", layout="wide")
st.title("🧬 Elomi HIV Data Dashboard")

response = supabase.table("HIV_Record").select("*").limit(1000).execute()

if response.data:
    df = pd.DataFrame(response.data)
    st.success(f"✅ Loaded {len(df)} records from Supabase.")
    st.dataframe(df)
else:
    st.error("❌ No data returned from Supabase.")
