import streamlit as st
import plotly.express as px
import pandas as pd
from utils import create_card, create_status_indicator, create_section_header

def render_export_operations(data, selected_location, selected_date):
    """Render the export operations section"""
    create_section_header("Export Operations Dashboard", "📦")
    
    # Filter data based on selected location
    export_data = data["export_data"]
    if selected_location != "Both":
        export_data = export_data[export_data["location"] == selected_location]
    
    # Commodity-Wise Breakdown Chart
    commodity_data = data["export_commodity"]
    if selected_location != "Both":
        commodity_data = commodity_data[commodity_data["location"] == selected_location]
    
    # Custom color scheme
    custom_colors = ["#6C63FF", "#4FACFE", "#00F2FE", "#7366FF", "#00E396", "#FEB019", "#FF4560", "#00D4FF"]
    
    fig = px.bar(
        commodity_data,
        x="commodity",
        y="weight",
        color="type",
        title="Commodity-Wise Breakdown for Exports",
        color_discrete_sequence=custom_colors
    )
    
    fig.update_layout(
        xaxis_title="Commodity Type",
        yaxis_title="Weight (Kg/Carats)",
        plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
        paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
        font_color="#E0E7FF",  # var(--light-text)
        title_font_size=16,
        title_font_family="Poppins",
        title_font_color="#6C63FF",  # var(--primary-color)
        legend_title_text="Type",
        margin=dict(l=10, r=10, t=50, b=10),
        legend=dict(
            font=dict(
                family="Poppins",
                size=12,
                color="#E0E7FF"
            )
        )
    )
    
    # Add grid lines with custom styling
    fig.update_xaxes(
        showgrid=True,
        gridwidth=0.5,
        gridcolor="rgba(255, 255, 255, 0.1)",
        tickfont=dict(
            family="Poppins",
            size=11,
            color="#E0E7FF"
        )
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=0.5,
        gridcolor="rgba(255, 255, 255, 0.1)",
        tickfont=dict(
            family="Poppins",
            size=11,
            color="#E0E7FF"
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Export KPIs in two columns
    kpi_col1, kpi_col2 = st.columns(2)
    
    with kpi_col1:
        # Total Export Weight
        export_weight = data["export_summary"]["total_weight"]
        create_card("Total Export Weight", export_weight, "⚖️", "66, 133, 244")
        
        # Highest Weight Parcels
        highest_weight = data["export_summary"]["highest_weight"]
        create_card("Highest Weight Parcel", highest_weight, "📦", "251, 188, 5")
    
    with kpi_col2:
        # Total Export Value
        export_value = data["export_summary"]["total_value"]
        create_card("Total Export Value", export_value, "💰", "52, 168, 83", prefix="$")
        
        # Highest Value Parcel
        highest_value = data["export_summary"]["highest_value"]
        create_card("Highest Value Parcel", highest_value, "💎", "234, 67, 53", prefix="$")
    
    # Surat to Mumbai Movement Tracking
    if selected_location in ["Both", "Surat"]:
        create_section_header("Surat to Mumbai, Sahar Movement Tracking", "🚚")
        transit_col1, transit_col2, transit_col3 = st.columns(3)
        
        with transit_col1:
            parcels_in_transit = data["transit_data"]["surat_to_mumbai"]["in_transit"]
            create_card("Parcels in Transit to Mumbai", parcels_in_transit, "🚚", "66, 133, 244")
            
        with transit_col2:
            pending_carting = data["transit_data"]["surat_to_mumbai"]["pending_carting"]
            create_card("Pending Carting to Mumbai", pending_carting, "⏱️", "251, 188, 5")
            
        with transit_col3:
            received_today = data["transit_data"]["surat_to_mumbai"]["received_today"]
            create_card("Parcels Received in Mumbai Today", received_today, "✅", "52, 168, 83")
    
    # Customs Processing Status
    if selected_location in ["Both", "Surat"]:
        create_section_header("Customs Processing Status (Surat)", "🛃")
        customs_col1, customs_col2, customs_col3 = st.columns(3)
        
        with customs_col1:
            pending_leo = data["customs_data"]["export"]["pending_leo"]
            create_card("Pending Confirm LEO", pending_leo, "📝", "66, 133, 244")
            
        with customs_col2:
            confirm_pctm = data["customs_data"]["export"]["confirm_pctm"]
            create_card("Confirm PCTM", confirm_pctm, "📋", "251, 188, 5")
            
        with customs_col3:
            confirm_tp = data["customs_data"]["export"]["confirm_tp"]
            create_card("Confirm TP", confirm_tp, "✅", "52, 168, 83")
    
    # Mumbai Final Flight Loading
    if selected_location in ["Both", "Mumbai, Sahar"]:
        create_section_header("Mumbai, Sahar Final Flight Loading", "✈️")
        flight_col1, flight_col2 = st.columns(2)
        
        with flight_col1:
            ready_for_flight = data["flight_data"]["ready_for_flight"]
            create_card("Parcels Ready for Flight Today", ready_for_flight, "✈️", "66, 133, 244")
            
        with flight_col2:
            loaded_onto_flights = data["flight_data"]["loaded_onto_flights"]
            create_card("Parcels Loaded onto Flights Today", loaded_onto_flights, "🛫", "52, 168, 83")
    
    # Exception Handling
    create_section_header("Exception Handling", "⚠️")
    exception_col1, exception_col2 = st.columns(2)
    
    with exception_col1:
        offloaded_parcels = data["exceptions"]["export"]["offloaded"]
        create_card("Offloaded Parcels", offloaded_parcels, "⚠️", "234, 67, 53")
        
    with exception_col2:
        returns_from_airline = data["exceptions"]["export"]["returns"]
        create_card("Returns from Airline", returns_from_airline, "🔄", "251, 188, 5")
