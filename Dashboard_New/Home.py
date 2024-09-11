import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
# Load data from PostgreSQL
conn = st.connection("telecom_db")
df = conn.query("SELECT * FROM xdr_data")


#sidebar of the streamlit
with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["EDA", "User overview analysis", "User engagement analysis", "User Experience Analysis", "User Satisfaction Analysis"]
    )
if selected=="EDA":
    st.title("Telecom Data - Exploratory Data Analysis")

# Show first few rows of the dataset
    st.subheader("Initial Data")
    st.write(df.head())
    
# Option to drop or fill missing values
    st.subheader("Handle Missing Values")
    missing_column = st.selectbox("Choose a column to fill missing values", df.columns[df.isnull().any()])
    fill_method = st.radio("Fill method", ["Fill with Mean", "Fill with Median", "Drop Rows"])
    if st.button("Apply Fill"):
        if fill_method == "Fill with Mean":
            df[missing_column] = df[missing_column].fillna(df[missing_column].mean())
        elif fill_method == "Fill with Median":
            df[missing_column] = df[missing_column].fillna(df[missing_column].median())
    else:
        df = df.dropna(subset=[missing_column])
        st.success(f"{missing_column} cleaned successfully")
        # ---- 2. Descriptive Statistics ----
        st.subheader("Descriptive Statistics")
        st.write(df.describe())
        # ---- 3. Visualizations ----
        st.subheader("Data Information")
        st.write(df.isnull().sum())
        # Handset Type Distribution
        st.subheader("Handset Type Distribution")
        handset_counts = df['Handset Type'].value_counts()
        st.bar_chart(handset_counts)
        # Comparing Handset Type with another feature, e.g., Total DL (Bytes)
        st.subheader("Comparison: Handset Type vs. Total DL (Bytes)")
        df_clean = df.dropna(subset=["Handset Type", "Total DL (Bytes)"])  # Clean data
        fig, ax = plt.subplots()
        sns.boxplot(x="Handset Type", y="Handset Manufacturer", data=df_clean, ax=ax)
        plt.xticks(rotation=90)
        st.pyplot(fig)
elif selected=="User overview analysis":
    st.title("This is the task two working area")
    st.subheader("Number of xDR Sessions")
    num_sessions = df.shape[0]  # Count the number of rows
    st.write(f"Total xDR Sessions: {num_sessions}")
    
elif selected=="User engagement analysis":
    st.title("The User engagement analysis Working Area")
elif selected=="User Experience Analysis":
    st.title("The User Experience Analysis Wroking Area")
else:
    st.title("User Satisfaction Analysis Working Area")

# Set page title


