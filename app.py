import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Skincare Product Recommender", layout="centered")

# Title
st.title("Skincare Product Recommender")
st.write("Select your skin type to get recommended skincare products!")

# Load dataset
try:
    df = pd.read_excel("skincare_100_rows.xlsx")
except FileNotFoundError:
    st.error("Dataset not found! Make sure 'skincare_100_rows.xlsx' is in the same folder as app.py.")
    st.stop()

# User selects skin type
skin_type = st.selectbox("Select your Skin Type:", df["Skin_Type"].unique())

# Filter products based on skin type
recommended = df[df["Skin_Type"] == skin_type]

# Display recommended products
if not recommended.empty:
    st.subheader(f"Recommended Products for {skin_type} skin:")
    st.dataframe(recommended[["Product_Code", "Product_Name", "Brand", "Category"]].reset_index(drop=True))
else:
    st.warning("No products found for this skin type.")

# Download CSV button
csv = recommended.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Recommendations as CSV",
    data=csv,
    file_name=f'recommended_products_{skin_type}.csv',
    mime='text/csv'
)
