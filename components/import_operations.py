import streamlit as st
import plotly.express as px
import pandas as pd
from utils import create_card, create_status_indicator, create_section_header

def render_import_operations(data, selected_location, selected_date):
    """Render the import operations section"""
    create_section_header("Import Operations Dashboard", "📥")
    
    # Filter data based on selected location
    import_data = data["import_data"]
    if selected_location != "Both":
        import_data = import_data[import_data["location"] == selected_location]
    
    # Commodity-Wise Breakdown Chart
    commodity_data = data["import_commodity"]
    if selected_location != "Both":
        commodity_data = commodity_data[commodity_data["location"] == selected_location]
    
    # Custom color scheme with a different palette than exports
    custom_colors = ["#00F2FE", "#4FACFE", "#6C63FF", "#7366FF", "#00E396", "#FEB019", "#FF4560", "#00D4FF"]
    
    fig = px.bar(
        commodity_data,
        x="commodity",
        y="weight",
        color="type",
        title="Commodity-Wise Breakdown for Imports",
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
        title_font_color="#4FACFE",  # Slightly different color than export
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
    
    # Import KPIs in two columns
    kpi_col1, kpi_col2 = st.columns(2)
    
    with kpi_col1:
        # Total Import Weight
        import_weight = data["import_summary"]["total_weight"]
        create_card("Total Import Weight", import_weight, "⚖️", "66, 133, 244")
        
        # Highest Weight Parcels
        highest_weight = data["import_summary"]["highest_weight"]
        create_card("Highest Weight Parcel", highest_weight, "📦", "251, 188, 5")
    
    with kpi_col2:
        # Total Import Value
        import_value = data["import_summary"]["total_value"]
        create_card("Total Import Value", import_value, "💰", "52, 168, 83", prefix="$")
        
        # Highest Value Parcel
        highest_value = data["import_summary"]["highest_value"]
        create_card("Highest Value Parcel", highest_value, "💎", "234, 67, 53", prefix="$")
    
    # Mumbai to Surat Movement Tracking
    if selected_location in ["Both", "Mumbai, Sahar"]:
        create_section_header("Mumbai, Sahar to Surat Movement Tracking", "🚚")
        transit_col1, transit_col2, transit_col3 = st.columns(3)
        
        with transit_col1:
            parcels_in_transit = data["transit_data"]["mumbai_to_surat"]["in_transit"]
            create_card("Parcels in Transit to Surat", parcels_in_transit, "🚚", "66, 133, 244")
            
        with transit_col2:
            pending_transport = data["transit_data"]["mumbai_to_surat"]["pending_transport"]
            create_card("Pending Transport from Mumbai", pending_transport, "⏱️", "251, 188, 5")
            
        with transit_col3:
            received_today = data["transit_data"]["mumbai_to_surat"]["received_today"]
            create_card("Parcels Received in Surat Today", received_today, "✅", "52, 168, 83")
    
    # Customs Processing Status
    if selected_location in ["Both", "Surat"]:
        create_section_header("Customs Processing Status (Surat)", "🛃")
        customs_col1, customs_col2 = st.columns(2)
        
        with customs_col1:
            pending_boe = data["customs_data"]["import"]["pending_boe"]
            create_card("Pending BOE Approvals", pending_boe, "📝", "66, 133, 244")
            
        with customs_col2:
            pending_examination = data["customs_data"]["import"]["pending_examination"]
            create_card("Pending Customs Examination", pending_examination, "🔍", "251, 188, 5")
    
    # Final Customer Delivery
    if selected_location in ["Both", "Surat"]:
        create_section_header("Final Customer Delivery (Surat)", "🚚")
        delivery_col1, delivery_col2 = st.columns(2)
        
        with delivery_col1:
            ready_for_delivery = data["delivery_data"]["ready_for_delivery"]
            create_card("Parcels Cleared & Ready for Delivery", ready_for_delivery, "✅", "66, 133, 244")
            
        with delivery_col2:
            delivered_today = data["delivery_data"]["delivered_today"]
            create_card("Parcels Delivered to Customers Today", delivered_today, "🚚", "52, 168, 83")
    
    # Exception Handling
    create_section_header("Exception Handling", "⚠️")
    exception_col1, exception_col2 = st.columns(2)
    
    with exception_col1:
        broken_seals = data["exceptions"]["import"]["broken_seals"]
        create_card("Parcels with Broken Seals", broken_seals, "🔴", "234, 67, 53")
        
    with exception_col2:
        reforwarding = data["exceptions"]["import"]["reforwarding"]
        create_card("Reforwarding Cases", reforwarding, "🔄", "251, 188, 5")
