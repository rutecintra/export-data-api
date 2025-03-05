import requests
import pandas as pd
import streamlit as st

BASE_URL = "https://atendimento.agidesk.com/api/v1/datasets/companyagents"

def fetch_data(yearmonths):
    all_data = []
    for yearmonth in yearmonths:
        params = {
            "app_key": "3f24e72f72f6187215c69b4e9498a079",
            "metadata": "",
            "pretty": "",
            "full": "",
            "yearmonth": yearmonth,
            "subprocess": "",
            "page": 1
        }
        
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            total_pages = data.get("metadata", {}).get("total_pages", 1)
            
            for page in range(1, total_pages + 1):
                params["page"] = page
                response = requests.get(BASE_URL, params=params)
                if response.status_code == 200:
                    page_data = response.json().get("data", [])
                    all_data.extend(page_data)
                else:
                    st.error(f"Error on page {page} for period {yearmonth}: {response.status_code}")
        else:
            st.error(f"Error accessing period {yearmonth}: {response.status_code}")
    return all_data

st.title("API Data Query")

yearmonths = st.text_area("Enter periods (year-month) separated by commas", "2025-01, 2025-02")
yearmonths_list = [ym.strip() for ym in yearmonths.split(",") if ym.strip()]

if st.button("Search"):
    if yearmonths_list:
        data = fetch_data(yearmonths_list)
        if data:
            df = pd.DataFrame(data)
            df.to_excel("data.xlsx", index=False)
            st.success("Data saved to 'data.xlsx'")
            st.dataframe(df)
        else:
            st.warning("No data found.")
    else:
        st.error("Please enter at least one valid period.")