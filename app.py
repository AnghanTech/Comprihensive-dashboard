import streamlit as st
import datetime
import pandas as pd
from components.header import render_header
from components.status_overview import render_status_overview
from components.export_operations import render_export_operations
from components.import_operations import render_import_operations
from components.financial_metrics import render_financial_metrics
from components.advanced_reporting import render_advanced_reporting
from components.footer import render_footer
from utils import load_css
from data.generate_data import generate_mock_data

# Page configuration
st.set_page_config(
    page_title="Custodian Operations Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
load_css()

# Session state initialization
if 'selected_location' not in st.session_state:
    st.session_state.selected_location = "Both"
    
if 'selected_date' not in st.session_state:
    st.session_state.selected_date = datetime.datetime.now().date()

if 'data' not in st.session_state:
    st.session_state.data = generate_mock_data()

# Main dashboard layout
def main():
    # Header component
    render_header()
    
    # Main content with sections
    render_status_overview(st.session_state.data, st.session_state.selected_location, st.session_state.selected_date)
    
    # Two column layout for Export and Import operations
    col1, col2 = st.columns(2)
    
    with col1:
        render_export_operations(st.session_state.data, st.session_state.selected_location, st.session_state.selected_date)
    
    with col2:
        render_import_operations(st.session_state.data, st.session_state.selected_location, st.session_state.selected_date)
    
    # Financial metrics section
    render_financial_metrics(st.session_state.data, st.session_state.selected_location, st.session_state.selected_date)
    
    # Advanced reporting and analytics
    render_advanced_reporting(st.session_state.data, st.session_state.selected_location, st.session_state.selected_date)
    
    # Footer with system status
    render_footer()

if __name__ == "__main__":
    main()
