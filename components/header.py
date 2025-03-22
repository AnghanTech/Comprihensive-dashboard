import streamlit as st
from datetime import datetime
import time
import os
import base64
from pathlib import Path


def get_base64_of_image(image_path):
    """Get base64 encoded string for an image"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def render_header():
    """Render the dashboard header"""
    # Header with navigation
    header_col1, header_col2, header_col3 = st.columns([2, 6, 2])

    with header_col1:
        # Logo and date/time section
        logo_path = Path("attached_assets/logo_master (2).png")
        if logo_path.exists():
            logo_base64 = get_base64_of_image(logo_path)
            logo_html = f"""
            <div style="display:flex;align-items:center;margin-bottom:10px;">
                <img src="data:image/png;base64,{logo_base64}" alt="Surat Diamond Bourse Logo" width="180px" style="filter:brightness(1.2);">
            </div>
            """
            st.markdown(logo_html, unsafe_allow_html=True)
        else:
            st.write("Surat Diamond Bourse")

        # Current date and time with Streamlit's container
        current_date = datetime.now().strftime("%d %b %Y")
        current_time = datetime.now().strftime("%H:%M:%S")
        st.markdown(
            f'<span style="font-size:14px;color:#999;">{current_date} | {current_time}</span>',
            unsafe_allow_html=True,
        )

    with header_col2:
        st.markdown(
            '<h1 class="dashboard-title"><span class="neon-accent glow">Custodian</span> <span class="neon-accent glow">Dashboard</span></h1>',
            unsafe_allow_html=True,
        )

    with header_col3:
        # User profile and notifications
        profile_html = """
        <div style="display:flex;justify-content:flex-end;align-items:center;">
            <div style="position:relative;margin-right:15px;">
                <span style="font-size:20px;cursor:pointer;">🔔</span>
                <span class="notification-badge">3</span>
            </div>
            <div style="display:flex;align-items:center;">
                <div style="background-color:#4285F4;color:white;width:32px;height:32px;border-radius:50%;display:flex;justify-content:center;align-items:center;margin-right:8px;">
                    <span>AD</span>
                </div>
                <div>
                    <div style="font-size:14px;line-height:1.2;">Admin</div>
                    <div style="font-size:12px;color:#999;line-height:1.2;">Operations Team</div>
                </div>
            </div>
        </div>
        """
        st.markdown(profile_html, unsafe_allow_html=True)

    # Search and filter section
    filter_col1, filter_col2, filter_col3 = st.columns([6, 3, 3])

    with filter_col1:
        st.text_input(
            "🔍 Search (Parcel ID, ER No, IR No, Console Agent, Airline...)",
            placeholder="Enter search term...",
        )

    with filter_col2:
        date_selection = st.date_input("Select Date:", value=datetime.now())
        if date_selection:
            st.session_state.selected_date = date_selection

    with filter_col3:
        location_options = ["Both", "Surat", "Mumbai, Sahar"]
        selected_location = st.selectbox("Location:", options=location_options, index=0)

        # Update session state if changed
        if selected_location != st.session_state.selected_location:
            st.session_state.selected_location = selected_location
            st.rerun()

    # Separator
    st.markdown(
        '<hr style="margin:10px 0 20px 0;border-color:#333;">', unsafe_allow_html=True
    )
