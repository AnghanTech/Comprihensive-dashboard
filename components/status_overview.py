import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils import create_card, format_number, create_section_header

def render_status_overview(data, selected_location, selected_date):
    """Render the real-time status overview section"""
    create_section_header("Real-Time Status Overview", "📊")
    
    # Filter data based on selected location and date
    filtered_data = data["kpi_data"]
    
    # First row of KPI cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Total Pending Exports
        if selected_location == "Both":
            value = f"Surat: {filtered_data['pending_exports_surat']} | Mumbai: {filtered_data['pending_exports_mumbai']}"
        elif selected_location == "Surat":
            value = format_number(filtered_data['pending_exports_surat'])
        else:
            value = format_number(filtered_data['pending_exports_mumbai'])
            
        create_card("Total Pending Exports", value, "📦", "66, 133, 244")
        
    with col2:
        # Total Pending Imports
        if selected_location == "Both":
            value = f"Surat: {filtered_data['pending_imports_surat']} | Mumbai: {filtered_data['pending_imports_mumbai']}"
        elif selected_location == "Surat":
            value = format_number(filtered_data['pending_imports_surat'])
        else:
            value = format_number(filtered_data['pending_imports_mumbai'])
            
        create_card("Total Pending Imports", value, "📥", "52, 168, 83")
        
    with col3:
        # Delayed Shipments
        if selected_location == "Both":
            value = f"Export: {filtered_data['delayed_exports']} | Import: {filtered_data['delayed_imports']}"
        else:
            location_key = "surat" if selected_location == "Surat" else "mumbai"
            export_key = f"delayed_exports_{location_key}"
            import_key = f"delayed_imports_{location_key}"
            value = f"Export: {filtered_data[export_key]} | Import: {filtered_data[import_key]}"
            
        create_card("Delayed Shipments", value, "⏱️", "251, 188, 5")
        
    with col4:
        # Parcels in Customs Hold
        if selected_location == "Both":
            value = f"Surat: {filtered_data['customs_hold_surat']} | Mumbai: {filtered_data['customs_hold_mumbai']}"
        elif selected_location == "Surat":
            value = format_number(filtered_data['customs_hold_surat'])
        else:
            value = format_number(filtered_data['customs_hold_mumbai'])
            
        create_card("Parcels in Customs Hold", value, "🛃", "234, 67, 53")
    
    # Second row of KPI cards
    col1, col2 = st.columns(2)
    
    with col1:
        # Total Weight in Custodian Strong Rooms
        if selected_location == "Both":
            value = f"Surat: {filtered_data['weight_surat']} | Mumbai: {filtered_data['weight_mumbai']}"
        elif selected_location == "Surat":
            value = filtered_data['weight_surat']
        else:
            value = filtered_data['weight_mumbai']
            
        create_card("Total Weight in Custodian Strong Rooms", value, "⚖️", "66, 133, 244")
        
    with col2:
        # Parcel Processing Efficiency
        efficiency = filtered_data['processing_efficiency']
        trend = filtered_data['efficiency_trend']
        create_card("Parcel Processing Efficiency (Last 7 Days)", f"{efficiency}%", "📈", "52, 168, 83", show_trend=True, trend_value=trend)
    
    # Stock Breakdown and Processing Efficiency charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Stock Breakdown by Location & Commodity Type
        stock_data = data["stock_breakdown"]
        
        # Filter by location if needed
        if selected_location != "Both":
            stock_data = stock_data[stock_data["location"] == selected_location]
        
        # Custom color scheme
        custom_colors = ["#6C63FF", "#4FACFE", "#00F2FE", "#7366FF", "#00E396"]
        
        fig = px.bar(
            stock_data,
            x="commodity_type",
            y="weight",
            color="location",
            barmode="group",
            title="Stock Breakdown by Location & Commodity Type",
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
            legend_title_text="Location",
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
        
    with chart_col2:
        # Parcel Processing Efficiency (Last 7 Days)
        efficiency_data = data["efficiency_data"]
        
        # Custom color scheme
        custom_colors = ["#6C63FF", "#4FACFE", "#00F2FE", "#7366FF"]
        
        fig = px.line(
            efficiency_data,
            x="date",
            y="efficiency",
            color="type",
            title="Parcel Processing Efficiency (Last 7 Days)",
            color_discrete_sequence=custom_colors
        )
        
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Efficiency (%)",
            plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
            paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
            font_color="#E0E7FF",  # var(--light-text)
            title_font_size=16,
            title_font_family="Poppins",
            title_font_color="#6C63FF",  # var(--primary-color)
            legend_title_text="Type",
            legend=dict(
                font=dict(
                    family="Poppins",
                    size=12,
                    color="#E0E7FF"
                )
            )
        )
        
        # Add thicker line and custom markers
        fig.update_traces(
            line=dict(
                width=3,
                shape='spline',  # Makes the line curved
                smoothing=1.3
            ), 
            mode="lines+markers", 
            marker=dict(
                size=8,
                line=dict(
                    width=2,
                    color="#111827"  # var(--dark-bg)
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
    
    # Separator
    st.markdown('<hr style="margin:30px 0;border-color:rgba(108, 99, 255, 0.2);border-width:1px;">', unsafe_allow_html=True)
