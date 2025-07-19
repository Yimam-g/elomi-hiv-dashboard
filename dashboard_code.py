import requests
import json
import pandas as pd

# ✅ Supabase credentials
SUPABASE_URL = "https://kipfbkztkdsvleloskma.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtpcGZia3p0a2RzdmxlbG9za21hIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE1ODYwMDksImV4cCI6MjA2NzE2MjAwOX0.v2bvnrH1whVh-lDMR5HLaxk91UHdS3cI9wQYah5ZsZg"

url = f"{SUPABASE_URL}/rest/v1/hiv_record"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("✅ HIV Records:")
    print(json.dumps(data, indent=2))

    # Load into DataFrame
    df = pd.DataFrame(data)
    print("\n🧾 Preview (head):")
    print(df.head())
else:
    print("❌ Error:", response.status_code)
    print(response.text)
