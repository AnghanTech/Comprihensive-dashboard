import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import time

def load_css():
    """Add custom CSS to the dashboard"""
    # Load Google Fonts - Poppins
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
    
    # Load main CSS file
    with open('assets/style.css', 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # Add Font Awesome for better icons
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

def create_card(title, value, icon, color, prefix="", suffix="", show_trend=False, trend_value=0):
    """Create a styled card with optional trend indicator"""
    # Set prefix to ₹ if "Value" is in the title parameter
    if "Value" in title:
        prefix = "₹ "
    trend_html = ""
    if show_trend:
        trend_color = "var(--success)" if trend_value >= 0 else "var(--danger)"
        trend_icon = '<i class="fas fa-arrow-up"></i>' if trend_value >= 0 else '<i class="fas fa-arrow-down"></i>'
        trend_html = f'<span style="color:{trend_color};margin-left:8px;">{trend_icon} {abs(trend_value)}%</span>'
    
    # Map color strings to css variables
    color_map = {
        "66, 133, 244": "var(--primary-color)",
        "52, 168, 83": "var(--success)",
        "251, 188, 5": "var(--warning)",
        "234, 67, 53": "var(--danger)",
        "66, 133, 255": "var(--info)"
    }
    
    css_color = color_map.get(color, "var(--primary-color)")
    
    # Replace emoji icons with Font Awesome icons
    icon_map = {
        "📦": '<i class="fas fa-box"></i>',
        "📥": '<i class="fas fa-inbox"></i>',
        "⏱️": '<i class="fas fa-clock"></i>',
        "🛃": '<i class="fas fa-passport"></i>',
        "⚖️": '<i class="fas fa-weight"></i>',
        "📈": '<i class="fas fa-chart-line"></i>',
        "💰": '<i class="fas fa-money-bill-wave"></i>',
        "💎": '<i class="fas fa-gem"></i>',
        "🚚": '<i class="fas fa-truck"></i>',
        "✅": '<i class="fas fa-check-circle"></i>',
        "📝": '<i class="fas fa-file-alt"></i>',
        "📋": '<i class="fas fa-clipboard-list"></i>',
        "✈️": '<i class="fas fa-plane"></i>',
        "🛫": '<i class="fas fa-plane-departure"></i>',
        "⚠️": '<i class="fas fa-exclamation-triangle"></i>',
        "🔄": '<i class="fas fa-sync-alt"></i>',
        "🔍": '<i class="fas fa-search"></i>',
        "💵": '<i class="fas fa-money-bill"></i>',
        "📑": '<i class="fas fa-file-invoice"></i>',
        "👥": '<i class="fas fa-users"></i>',
        "🖥️": '<i class="fas fa-desktop"></i>',
        "⚙️": '<i class="fas fa-cogs"></i>'
    }
    
    fa_icon = icon_map.get(icon, icon)
    
    card_html = f"""
    <div class="custom-card" style="border-left: 4px solid {css_color}; background: linear-gradient(to right, var(--card-bg), rgba(26, 32, 53, 0.8));">
        <div style="display:flex;justify-content:space-between;align-items:center;">
            <div style="flex-grow:1;">
                <div style="font-size:0.9rem;color:var(--light-text);opacity:0.7;font-weight:500;">{title}</div>
                <div class="card-value">{prefix}{value}{suffix} {trend_html}</div>
            </div>
            <div class="card-icon" style="color:{css_color};">{fa_icon}</div>
        </div>
    </div>
    """
    return st.markdown(card_html, unsafe_allow_html=True)

def create_status_indicator(status, text):
    """Create a status indicator with color based on status"""
    color_map = {
        "ok": "var(--success)",      # Green
        "warning": "var(--warning)", # Yellow
        "error": "var(--danger)",    # Red
        "info": "var(--info)"        # Blue
    }
    
    icon_map = {
        "ok": '<i class="fas fa-check-circle"></i>',
        "warning": '<i class="fas fa-exclamation-triangle"></i>',
        "error": '<i class="fas fa-times-circle"></i>',
        "info": '<i class="fas fa-info-circle"></i>'
    }
    
    color = color_map.get(status.lower(), "var(--info)")
    icon = icon_map.get(status.lower(), '<i class="fas fa-circle"></i>')
    
    html = f"""
    <div style="display:flex;align-items:center;margin:8px 0;padding:8px 12px;background:var(--card-bg);border-radius:8px;border-left:3px solid {color};">
        <span style="color:{color};margin-right:10px;font-size:1.1rem;">{icon}</span>
        <span style="font-weight:500;">{text}</span>
    </div>
    """
    return st.markdown(html, unsafe_allow_html=True)

def format_number(number):
    """Format large numbers with commas"""
    return f"{number:,}"

def get_clock():
    """Get current time formatted as HH:MM:SS"""
    return datetime.now().strftime("%H:%M:%S")

def create_glowing_container(content_function, border_color="var(--primary-color)"):
    """Create a container with glowing border effect"""
    container_style = f"""
    <div class="glowing-container" style="border-color:{border_color};">
    """
    st.markdown(container_style, unsafe_allow_html=True)
    content_function()
    st.markdown("</div>", unsafe_allow_html=True)

def create_section_header(title, icon=""):
    """Create a styled section header with optional icon"""
    # Replace emoji icons with Font Awesome icons
    icon_map = {
        "📦": '<i class="fas fa-box"></i>',
        "📥": '<i class="fas fa-inbox"></i>',
        "⏱️": '<i class="fas fa-clock"></i>',
        "🛃": '<i class="fas fa-passport"></i>',
        "⚖️": '<i class="fas fa-weight"></i>',
        "📈": '<i class="fas fa-chart-line"></i>',
        "💰": '<i class="fas fa-money-bill-wave"></i>',
        "💎": '<i class="fas fa-gem"></i>',
        "🚚": '<i class="fas fa-truck"></i>',
        "✅": '<i class="fas fa-check-circle"></i>',
        "📝": '<i class="fas fa-file-alt"></i>',
        "📋": '<i class="fas fa-clipboard-list"></i>',
        "✈️": '<i class="fas fa-plane"></i>',
        "🛫": '<i class="fas fa-plane-departure"></i>',
        "⚠️": '<i class="fas fa-exclamation-triangle"></i>',
        "🔄": '<i class="fas fa-sync-alt"></i>',
        "🔍": '<i class="fas fa-search"></i>',
        "💵": '<i class="fas fa-money-bill"></i>',
        "📑": '<i class="fas fa-file-invoice"></i>',
        "👥": '<i class="fas fa-users"></i>',
        "🖥️": '<i class="fas fa-desktop"></i>',
        "⚙️": '<i class="fas fa-cogs"></i>',
        "📊": '<i class="fas fa-chart-bar"></i>',
        "🗂️": '<i class="fas fa-folder-open"></i>',
        "📱": '<i class="fas fa-mobile-alt"></i>',
        "🔔": '<i class="fas fa-bell"></i>'
    }
    
    fa_icon = icon_map.get(icon, icon)
    
    st.markdown(f"""
    <div class="section-header">
        <div class="section-title">{fa_icon} {title}</div>
    </div>
    """, unsafe_allow_html=True)

def create_commodity_chart(data, location, chart_type="bar"):
    """Create a commodity breakdown chart based on data"""
    # Custom color scheme based on our CSS variables
    custom_colors = ["#6C63FF", "#4FACFE", "#00F2FE", "#7366FF", "#00E396", "#FEB019", "#FF4560", "#00D4FF"]
    
    if chart_type == "bar":
        fig = px.bar(
            data, 
            x="commodity", 
            y="weight", 
            color="type",
            color_discrete_sequence=custom_colors,
            title=f"Commodity Distribution - {location}"
        )
    elif chart_type == "pie":
        fig = px.pie(
            data, 
            values="weight", 
            names="commodity",
            color_discrete_sequence=custom_colors,
            title=f"Commodity Distribution - {location}"
        )
    
    fig.update_layout(
        plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
        paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
        font_color="#E0E7FF",  # var(--light-text)
        title_font_size=16,
        title_font_family="Poppins",
        title_font_color="#6C63FF",  # var(--primary-color)
        margin=dict(l=10, r=10, t=40, b=10),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(
                family="Poppins",
                size=12,
                color="#E0E7FF"  # var(--light-text)
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
            color="#E0E7FF" # var(--light-text)
        )
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=0.5,
        gridcolor="rgba(255, 255, 255, 0.1)",
        tickfont=dict(
            family="Poppins",
            size=11,
            color="#E0E7FF" # var(--light-text)
        )
    )
    
    return fig

def create_line_chart(data, x_col, y_col, title, color_sequence=None):
    """Create a line chart from data"""
    if color_sequence is None:
        color_sequence = ["#6C63FF", "#4FACFE", "#00F2FE", "#7366FF"]
        
    fig = px.line(
        data,
        x=x_col,
        y=y_col,
        title=title,
        color_discrete_sequence=color_sequence
    )
    
    fig.update_layout(
        plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
        paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
        font_color="#E0E7FF",  # var(--light-text)
        title_font_size=16,
        title_font_family="Poppins",
        title_font_color="#6C63FF",  # var(--primary-color)
        margin=dict(l=10, r=10, t=40, b=10),
        legend=dict(
            font=dict(
                family="Poppins",
                size=12,
                color="#E0E7FF"  # var(--light-text)
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
            color="#E0E7FF" # var(--light-text)
        )
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=0.5,
        gridcolor="rgba(255, 255, 255, 0.1)",
        tickfont=dict(
            family="Poppins",
            size=11,
            color="#E0E7FF" # var(--light-text)
        )
    )
    
    return fig

def filter_data_by_location(data, location):
    """Filter data by selected location"""
    if location == "Both":
        return data
    return data[data["location"] == location]
