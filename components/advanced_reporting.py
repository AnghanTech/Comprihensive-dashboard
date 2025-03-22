import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils import create_section_header, create_card


def render_advanced_reporting(data, selected_location, selected_date):
    """Render the advanced reporting and analytics section"""
    create_section_header("Advanced Reporting & Analytics", "📑")

    # First row - Commodity distribution and Date-wise trends
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        # Commodity Distribution Overview
        commodity_data = data["commodity_distribution"]

        if selected_location != "Both":
            commodity_data = commodity_data[
                commodity_data["location"] == selected_location
            ]

        # Custom futuristic color palette
        custom_colors = [
            "#6C63FF",
            "#FF6384",
            "#36A2EB",
            "#FFCE56",
            "#4BC0C0",
            "#9966FF",
            "#FF9F40",
            "#B721FF",
        ]

        fig = px.pie(
            commodity_data,
            values="value",
            names="commodity",
            title="Commodity Distribution Overview",
            color_discrete_sequence=custom_colors,
            hole=0.6,  # Larger hole for more futuristic look
        )

        fig.update_layout(
            plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
            paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
            font_color="#E0E7FF",  # var(--light-text)
            title_font_size=16,
            title_font_family="Poppins",
            title_font_color="#6C63FF",  # Purple tint for analytics data
            margin=dict(l=10, r=10, t=50, b=10),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5,
                font=dict(family="Poppins", size=11, color="#E0E7FF"),
                bgcolor="rgba(26, 32, 53, 0.3)",
            ),
        )

        # Add a glowing effect
        fig.update_traces(
            marker=dict(line=dict(color="rgba(255, 255, 255, 0.2)", width=1)),
            textinfo="percent+label",
            textfont=dict(family="Poppins", size=11, color="#ffffff"),
            hoverinfo="label+percent+value",
            textposition="inside",
        )

        st.plotly_chart(fig, use_container_width=True)

    with row1_col2:
        # Date-Wise Trends for Parcel Movement
        trends_data = data["date_trends"]

        # Custom gradients for line charts
        custom_colors = ["#4facfe", "#6C63FF"]

        fig = px.line(
            trends_data,
            x="date",
            y=["exports", "imports"],
            title="Date-Wise Trends for Parcel Movement",
            color_discrete_sequence=custom_colors,
            markers=True,  # Add markers for data points
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Number of Parcels",
            plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
            paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
            font_color="#E0E7FF",  # var(--light-text)
            title_font_size=16,
            title_font_family="Poppins",
            title_font_color="#4facfe",  # Blue tint for trend data
            margin=dict(l=10, r=10, t=50, b=10),
            legend_title_text="",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                font=dict(family="Poppins", size=11, color="#E0E7FF"),
                bgcolor="rgba(26, 32, 53, 0.3)",
            ),
        )

        # Update axes appearance
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

        # Update line styles
        fig.update_traces(
            line=dict(width=3),
            marker=dict(size=8, line=dict(width=1, color="rgba(255, 255, 255, 0.8)")),
            hovertemplate="<b>%{y}</b> parcels on %{x}<extra></extra>",
        )

        st.plotly_chart(fig, use_container_width=True)

    # Second row - Top contributors and Location comparison
    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        # Top Importers & Exporters
        create_section_header("Top Importers & Exporters", "🏆")

        tabs = st.tabs(["Top Exporters", "Top Importers", "Top Console Agents"])

        with tabs[0]:
            exporters = data["top_contributors"]["exporters"]

            # Create custom color scale for a futuristic gradient
            custom_color_scale = [
                [0, "#00F2FE"],  # Start with light blue
                [0.5, "#4FACFE"],  # Mid blue
                [1, "#0082FF"],  # End with deeper blue
            ]

            fig = px.bar(
                exporters,
                x="value",
                y="name",
                orientation="h",
                color="value",
                color_continuous_scale=custom_color_scale,
                title="Top Exporters by Volume",
            )

            fig.update_layout(
                plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
                paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
                font_color="#E0E7FF",  # var(--light-text)
                title_font_size=16,
                title_font_family="Poppins",
                title_font_color="#4FACFE",  # Blue tint for exporters
                margin=dict(l=10, r=10, t=50, b=30),
                xaxis_title="Export Volume (Kg/Carats)",
                yaxis_title="",
                coloraxis_showscale=False,
            )

            # Add grid lines for better readability
            fig.update_xaxes(
                showgrid=True,
                gridwidth=0.5,
                gridcolor="rgba(255, 255, 255, 0.1)",
                tickfont=dict(family="Poppins", size=11, color="#E0E7FF"),
            )

            fig.update_yaxes(tickfont=dict(family="Poppins", size=11, color="#E0E7FF"))

            # Add hover template
            fig.update_traces(
                hovertemplate="<b>%{y}</b>: %{x:,.0f} Kg/Carats<extra></extra>",
                marker=dict(line=dict(width=0)),
            )

            st.plotly_chart(fig, use_container_width=True)

        with tabs[1]:
            importers = data["top_contributors"]["importers"]

            # Create custom color scale for importers (purple gradient)
            custom_color_scale = [
                [0, "#A259FF"],  # Start with light purple
                [0.5, "#6C63FF"],  # Mid purple
                [1, "#B721FF"],  # End with deeper purple
            ]

            fig = px.bar(
                importers,
                x="value",
                y="name",
                orientation="h",
                color="value",
                color_continuous_scale=custom_color_scale,
                title="Top Importers by Volume",
            )

            fig.update_layout(
                plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
                paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
                font_color="#E0E7FF",  # var(--light-text)
                title_font_size=16,
                title_font_family="Poppins",
                title_font_color="#6C63FF",  # Purple tint for importers
                margin=dict(l=10, r=10, t=50, b=30),
                xaxis_title="Import Volume (Kg/Carats)",
                yaxis_title="",
                coloraxis_showscale=False,
            )

            # Add grid lines for better readability
            fig.update_xaxes(
                showgrid=True,
                gridwidth=0.5,
                gridcolor="rgba(255, 255, 255, 0.1)",
                tickfont=dict(family="Poppins", size=11, color="#E0E7FF"),
            )

            fig.update_yaxes(tickfont=dict(family="Poppins", size=11, color="#E0E7FF"))

            # Add hover template
            fig.update_traces(
                hovertemplate="<b>%{y}</b>: %{x:,.0f} Kg/Carats<extra></extra>",
                marker=dict(line=dict(width=0)),
            )

            st.plotly_chart(fig, use_container_width=True)

        with tabs[2]:
            agents = data["top_contributors"]["console_agents"]

            # Create custom color scale for console agents (green gradient)
            custom_color_scale = [
                [0, "#00E396"],  # Start with light green
                [0.5, "#08AEEA"],  # Mid teal
                [1, "#00D4FF"],  # End with light blue
            ]

            fig = px.bar(
                agents,
                x="value",
                y="name",
                orientation="h",
                color="value",
                color_continuous_scale=custom_color_scale,
                title="Most Active Console Agents",
            )

            fig.update_layout(
                plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
                paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
                font_color="#E0E7FF",  # var(--light-text)
                title_font_size=16,
                title_font_family="Poppins",
                title_font_color="#00E396",  # Green tint for agents
                margin=dict(l=10, r=10, t=50, b=30),
                xaxis_title="Number of Shipments",
                yaxis_title="",
                coloraxis_showscale=False,
            )

            # Add grid lines for better readability
            fig.update_xaxes(
                showgrid=True,
                gridwidth=0.5,
                gridcolor="rgba(255, 255, 255, 0.1)",
                tickfont=dict(family="Poppins", size=11, color="#E0E7FF"),
            )

            fig.update_yaxes(tickfont=dict(family="Poppins", size=11, color="#E0E7FF"))

            # Add hover template
            fig.update_traces(
                hovertemplate="<b>%{y}</b>: %{x:,.0f} Shipments<extra></extra>",
                marker=dict(line=dict(width=0)),
            )

            st.plotly_chart(fig, use_container_width=True)

    # with row2_col2:
    #     # Surat vs. Mumbai, Sahar Comparison
    #     create_section_header("Surat vs. Mumbai, Sahar Comparison", "📊")

    #     comparison_data = data["location_comparison"]

    #     fig = go.Figure()

    #     # Add trace for Surat - using a futuristic blue with 75% opacity
    #     fig.add_trace(go.Bar(
    #         x=comparison_data["category"],
    #         y=comparison_data["surat"],
    #         name="Surat",
    #         marker=dict(
    #             color="rgba(66, 135, 245, 0.85)",
    #             line=dict(
    #                 color="rgba(66, 135, 245, 1)",
    #                 width=1
    #             )
    #         ),
    #         hovertemplate='<b>Surat</b><br>%{x}: %{y}<extra></extra>'
    #     ))

    #     # Add trace for Mumbai - using a futuristic amber/gold with 75% opacity
    #     fig.add_trace(go.Bar(
    #         x=comparison_data["category"],
    #         y=comparison_data["mumbai"],
    #         name="Mumbai, Sahar",
    #         marker=dict(
    #             color="rgba(251, 188, 5, 0.85)",
    #             line=dict(
    #                 color="rgba(251, 188, 5, 1)",
    #                 width=1
    #             )
    #         ),
    #         hovertemplate='<b>Mumbai, Sahar</b><br>%{x}: %{y}<extra></extra>'
    #     ))

    #     fig.update_layout(
    #         title=dict(
    #             text="Surat vs. Mumbai, Sahar Stock & Movement",
    #             font=dict(
    #                 family="Poppins",
    #                 size=16,
    #                 color="#E0E7FF"
    #             ),
    #             x=0.5,
    #             y=0.95
    #         ),
    #         barmode="group",
    #         bargap=0.25,
    #         bargroupgap=0.1,
    #         plot_bgcolor="rgba(17, 24, 39, 0.8)",  # var(--dark-bg)
    #         paper_bgcolor="rgba(26, 32, 53, 0.5)",  # var(--card-bg)
    #         font_color="#E0E7FF",  # var(--light-text)
    #         margin=dict(l=20, r=20, t=70, b=50),
    #         xaxis_title="Category",
    #         yaxis_title="Count",
    #         xaxis=dict(
    #             tickfont=dict(
    #                 family="Poppins",
    #                 size=11,
    #                 color="#E0E7FF"
    #             ),
    #             showgrid=False
    #         ),
    #         yaxis=dict(
    #             tickfont=dict(
    #                 family="Poppins",
    #                 size=11,
    #                 color="#E0E7FF"
    #             ),
    #             showgrid=True,
    #             gridwidth=0.5,
    #             gridcolor="rgba(255, 255, 255, 0.1)"
    #         ),
    #         legend=dict(
    #             font=dict(
    #                 family="Poppins",
    #                 size=11,
    #                 color="#E0E7FF"
    #             ),
    #             orientation="h",
    #             yanchor="bottom",
    #             y=1.02,
    #             xanchor="right",
    #             x=1,
    #             bgcolor="rgba(26, 32, 53, 0.3)"
    #         )
    #     )

    #     st.plotly_chart(fig, use_container_width=True)

    # Report Access section
    create_section_header("Quick Access to Reports", "📊")

    # Add a futuristic description for the report section
    st.markdown(
        """
    <div style="background-color: rgba(26, 32, 53, 0.5); padding: 10px; border-radius: 10px; margin-bottom: 15px; border-left: 3px solid #6C63FF;">
        <p style="color: #E0E7FF; font-family: 'Poppins', sans-serif; margin: 0;">
            Download detailed reports in Excel format for comprehensive analysis and record-keeping. 
            All exports are secured with data integrity checks.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Custom CSS for buttons
    st.markdown(
        """
    <style>
        div[data-testid="stDownloadButton"] button {
            background: linear-gradient(90deg, rgba(108,99,255,0.2) 0%, rgba(108,99,255,0.4) 100%);
            color: white;
            border: 1px solid rgba(108,99,255,0.4);
            padding: 10px 15px;
            border-radius: 8px;
            transition: all 0.3s ease;
            font-weight: 500;
            min-height: 60px;
        }
        div[data-testid="stDownloadButton"] button:hover {
            background: linear-gradient(90deg, rgba(108,99,255,0.4) 0%, rgba(108,99,255,0.8) 100%);
            box-shadow: 0 0 10px rgba(108,99,255,0.5);
            transform: translateY(-2px);
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    report_col1, report_col2, report_col3, report_col4 = st.columns(4)

    with report_col1:
        st.download_button(
            label="📄 Export Register Details",
            data="Export register data would be here",
            file_name="export_register.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Download detailed export register for the selected date range and location",
        )

    with report_col2:
        st.download_button(
            label="📄 Import Register Details",
            data="Import register data would be here",
            file_name="import_register.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Download detailed import register for the selected date range and location",
        )

    with report_col3:
        st.download_button(
            label="📄 Lost & Found Report",
            data="Lost and found report data would be here",
            file_name="lost_found_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Download report of all parcels in the lost & found status",
        )

    with report_col4:
        st.download_button(
            label="📄 Customs Hold Report",
            data="Customs hold report data would be here",
            file_name="customs_hold_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Download report of all parcels currently on customs hold",
        )

    # Separator with gradient
    st.markdown(
        """
    <div style="position:relative; height:2px; margin:30px 0; background: linear-gradient(90deg, 
                rgba(0,0,0,0) 0%, 
                rgba(108,99,255,0.8) 15%, 
                rgba(179,97,255,0.8) 50%, 
                rgba(108,99,255,0.8) 85%, 
                rgba(0,0,0,0) 100%);">
    </div>
    """,
        unsafe_allow_html=True,
    )
