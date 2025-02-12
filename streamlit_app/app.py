import streamlit as st
import os

def main():
    st.set_page_config(page_title="Face Detection", layout="wide")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Data", "EDA", "Detection"])
    
    if page == "Home":
        st.title("Human Face Detection System")
        st.write("Welcome to the face detection project!")
        
    elif page == "Data":
        st.title("Dataset Explorer")
        # Add dataset visualization later
        
    elif page == "Detection":
        st.title("Real-Time Face Detection")
        # Add detection interface later

if __name__ == "__main__":
    main()
