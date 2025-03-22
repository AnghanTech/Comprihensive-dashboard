import streamlit as st
import plotly.express as px
import pandas as pd
from utils import create_card, create_section_header


def render_financial_metrics(data, selected_location, selected_date):
    """Render the financial metrics section"""
    create_section_header("Financial & Service Metrics", "💰")

    # Get financial data
    financial_data = data["financial_data"]

    # Financial KPIs
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        service_charges = financial_data["service_charges_today"]
        create_card(
            "Service Charges Generated (Today)",
            service_charges,
            "💵",
            "52, 168, 83",
            prefix="₹",
        )

    with col2:
        pending_invoice = financial_data["pending_invoice"]
        create_card(
            "Pending Invoice Payments", pending_invoice, "📑", "251, 188, 5", prefix="₹"
        )

    with col3:
        pending_demurrage = financial_data["demurrage"]["pending"]
        create_card(
            "Demurrage Charges (Pending)",
            pending_demurrage,
            "⏱️",
            "234, 67, 53",
            prefix="₹",
        )

    with col4:
        paid_demurrage = financial_data["demurrage"]["paid"]
        create_card(
            "Demurrage Charges (Paid)", paid_demurrage, "✅", "66, 133, 244", prefix="₹"
        )

    # Revenue chart and System Usage
    chart_col, usage_col = st.columns([2, 1])

    with chart_col:
        # Real-Time Revenue Insights chart
        revenue_data = data["revenue_data"]

        # Custom color scheme for financial metrics
        financial_colors = [
            "#00E396",
            "#00D4FF",
            "#4FACFE",
            "#B721FF",
            "#FF4560",
            "#FF9A00",
        ]

        fig = px.bar(
            revenue_data,
            x="month",
            y="amount",
            color="type",
            title="Monthly Revenue Trends",
            color_discrete_sequence=financial_colors,
            barmode="group",
        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Revenue (₹)",
            plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
            paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
            font_color="#E0E7FF",  # var(--light-text)
            title_font_size=16,
            title_font_family="Poppins",
            title_font_color="#00E396",  # Green tint for financial data
            legend_title_text="Revenue Type",
            margin=dict(l=10, r=10, t=50, b=10),
            legend=dict(font=dict(family="Poppins", size=12, color="#E0E7FF")),
        )

        # Add grid lines with custom styling
        fig.update_xaxes(
            showgrid=True,
            gridwidth=0.5,
            gridcolor="rgba(255, 255, 255, 0.1)",
            tickfont=dict(family="Poppins", size=11, color="#E0E7FF"),
        )

        fig.update_yaxes(
            showgrid=True,
            gridwidth=0.5,
            gridcolor="rgba(255, 255, 255, 0.1)",
            tickfont=dict(family="Poppins", size=11, color="#E0E7FF"),
        )

        st.plotly_chart(fig, use_container_width=True)

    # with usage_col:
    #     create_section_header("System Usage & Performance", "💻")

    #     # Active Users
    #     active_users = financial_data["system_usage"]["active_users"]
    #     create_card("Active Users Logged In", active_users, "👥", "66, 133, 244")

    #     # Pending Approvals
    #     pending_approvals = financial_data["system_usage"]["pending_approvals"]
    #     create_card("Pending Approvals", pending_approvals, "📝", "251, 188, 5")

    #     # System load
    #     system_load = financial_data["system_usage"]["system_load"]
    #     create_card("System Load", f"{system_load}%", "🖥️", "52, 168, 83")

    #     # Background processes
    #     background_processes = financial_data["system_usage"]["background_processes"]
    #     create_card("Background Processes", background_processes, "⚙️", "66, 133, 244")

    # Separator with gradient
    st.markdown(
        """
    <div style="position:relative; height:2px; margin:30px 0; background: linear-gradient(90deg, 
                rgba(0,0,0,0) 0%, 
                rgba(79,172,254,0.8) 15%, 
                rgba(0,242,254,0.8) 50%, 
                rgba(79,172,254,0.8) 85%, 
                rgba(0,0,0,0) 100%);">
    </div>
    """,
        unsafe_allow_html=True,
    )
