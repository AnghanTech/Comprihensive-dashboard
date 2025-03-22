import streamlit as st
import random


def render_footer():
    """Render the dashboard footer with system status"""
    # st.markdown("### 📌 System & Support")

    # System health status
    col1, col2 = st.columns([1, 3])

    # with col1:
    #     # Randomly choose a system status for demo purposes
    #     status_options = ["ok", "warning", "error"]
    #     weights = [0.8, 0.15, 0.05]  # 80% chance of OK, 15% warning, 5% error
    #     system_status = random.choices(status_options, weights=weights, k=1)[0]

    #     status_color = {
    #         "ok": "#34A853",  # Green
    #         "warning": "#FBBC05",  # Yellow
    #         "error": "#EA4335",  # Red
    #     }

    #     status_text = {
    #         "ok": "All Systems Operational",
    #         "warning": "Minor Issues Detected",
    #         "error": "Critical System Errors",
    #     }

    #     # Use a Streamlit container with custom styling
    #     with st.container():
    #         st.markdown(
    #             f"""
    #         <div style="background-color:rgba(26, 32, 53, 0.8);border-radius:10px;padding:15px;margin:5px 0;box-shadow:0 8px 24px rgba(0, 0, 0, 0.15);border-left:3px solid {status_color[system_status]};">
    #             <div style="display:flex;align-items:center;">
    #                 <div style="font-size:1.8rem;margin-right:15px;color:{status_color[system_status]};">
    #                     {"✅" if system_status == "ok" else "⚠️" if system_status == "warning" else "🛑"}
    #                 </div>
    #                 <div>
    #                     <div style="font-size:1.2rem;font-weight:bold;color:{status_color[system_status]};font-family:'Poppins',sans-serif;">{status_text[system_status]}</div>
    #                     <div style="font-size:0.8rem;color:#AAA;">Last checked: {random.randint(1, 59)} minutes ago</div>
    #                 </div>
    #             </div>
    #         </div>
    #         """,
    #             unsafe_allow_html=True,
    #         )

    # Use Streamlit columns for the support section
    with col2:
        # Create three columns for the support section
        support_col1, support_col2, support_col3 = st.columns(3)

        with support_col1:
            with st.container():
                st.markdown(
                    """
                <div style="background-color:rgba(26, 32, 53, 0.8);border-radius:10px;padding:15px;box-shadow:0 8px 24px rgba(0, 0, 0, 0.15);height:100%;border-left:3px solid #6C63FF;">
                    <div style="font-size:1.1rem;margin-bottom:10px;color:#6C63FF;font-weight:600;font-family:'Poppins',sans-serif;">
                        <i class="fas fa-headset"></i> Contact Support
                    </div>
                    <div style="color:#E0E7FF;">
                        <div style="padding:4px 0;cursor:pointer;">Email: custodian.it@sdbbourse.com</div>
                        <div style="padding:4px 0;cursor:pointer;">Phone: 0261 691 6920</div>
                        <div style="padding:4px 0;cursor:pointer;">Available: 24/7</div>
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        with support_col2:
            with st.container():
                st.markdown(
                    """
                <div style="background-color:rgba(26, 32, 53, 0.8);border-radius:10px;padding:15px;box-shadow:0 8px 24px rgba(0, 0, 0, 0.15);height:100%;border-left:3px solid #6C63FF;">
                    <div style="font-size:1.1rem;margin-bottom:10px;color:#6C63FF;font-weight:600;font-family:'Poppins',sans-serif;">
                        <i class="fas fa-book"></i> Help Resources
                    </div>
                    <div style="color:#E0E7FF;">
                        <div style="padding:4px 0;cursor:pointer;">User Manual</div>
                        <div style="padding:4px 0;cursor:pointer;">FAQs</div>
                        <div style="padding:4px 0;cursor:pointer;">Video Tutorials</div>
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        # with support_col3:
        #     with st.container():
        #         st.markdown(
        #             """
        #         <div style="background-color:rgba(26, 32, 53, 0.8);border-radius:10px;padding:15px;box-shadow:0 8px 24px rgba(0, 0, 0, 0.15);height:100%;border-left:3px solid #6C63FF;">
        #             <div style="font-size:1.1rem;margin-bottom:10px;color:#6C63FF;font-weight:600;font-family:'Poppins',sans-serif;">
        #                 <i class="fas fa-bolt"></i> Quick Actions
        #             </div>
        #             <div style="color:#E0E7FF;">
        #                 <div style="padding:4px 0;cursor:pointer;">Reset Dashboard</div>
        #                 <div style="padding:4px 0;cursor:pointer;">Clear Cache</div>
        #                 <div style="padding:4px 0;cursor:pointer;">Report an Issue</div>
        #             </div>
        #         </div>
        #         """,
        #             unsafe_allow_html=True,
        #         )

    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)

    # Copyright and version information
    st.markdown(
        """
    <div style="text-align:center;padding:20px 0;color:#AAA;font-size:0.8rem;">
        <div>Custodian Dashboard v2.0.1 | © 2025 SDB Diamond Bourse</div>
            </div>
    """,
        unsafe_allow_html=True,
    )
