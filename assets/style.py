import streamlit as st


def load_custom_styles():
    st.markdown(
        """
    <style>
    /* Main background color */
    .reportview-container {
        background: #111111;
        color: #FFFFFF;
    }
    
    /* Content background */
    .main .block-container {
        background-color: #161616;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    
    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: #1A1A1A;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF;
        font-weight: 600;
    }
    
    h1 {
        font-size: 2.5rem;
        background: linear-gradient(90deg, #4285F4, #45B3E0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    h2 {
        font-size: 1.8rem;
        border-bottom: 2px solid #4285F4;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    h3 {
        font-size: 1.4rem;
        color: #4285F4;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Charts and visualizations */
    .js-plotly-plot {
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        margin-bottom: 1.5rem;
        background-color: #1E1E1E;
    }
    
    /* Cards */
    .stCard {
        border-radius: 15px;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        background-color: #1E1E1E;
        border: 1px solid #333;
    }
    
    .stCard:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Input elements */
    .stTextInput > div > div {
        background-color: #333;
        color: white;
        border-radius: 5px;
    }
    
    .stTextInput input {
        color: white;
    }
    
    .stSelectbox > div > div {
        background-color: #333;
        color: white;
        border-radius: 5px;
    }
    
    .stDateInput > div > div {
        background-color: #333;
        color: white;
        border-radius: 5px;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #4285F4;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #3574de;
        box-shadow: 0 4px 8px rgba(66, 133, 244, 0.3);
    }
    
    /* Metrics */
    .metric-container {
        background-color: #1E1E1E;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        border-left: 3px solid #4285F4;
        margin-bottom: 1rem;
    }
    
    .metric-label {
        color: #999;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
    }
    
    /* Tables */
    .stDataFrame {
        background-color: #1E1E1E;
        border-radius: 10px;
        overflow: hidden;
    }
    
    .stDataFrame table {
        border-collapse: collapse;
        width: 100%;
    }
    
    .stDataFrame th {
        background-color: #333;
        color: white;
        padding: 0.5rem 1rem;
        text-align: left;
    }
    
    .stDataFrame td {
        border-top: 1px solid #333;
        padding: 0.5rem 1rem;
    }
    
    /* Animations */
    @keyframes glow {
        0% {
            box-shadow: 0 0 5px rgba(66, 133, 244, 0.3);
        }
        50% {
            box-shadow: 0 0 20px rgba(66, 133, 244, 0.5);
        }
        100% {
            box-shadow: 0 0 5px rgba(66, 133, 244, 0.3);
        }
    }
    
    .glow-effect {
        animation: glow 2s infinite;
    }
    
    /* Status indicators */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 0.5rem;
    }
    
    .status-green {
        background-color: #34A853;
        box-shadow: 0 0 5px #34A853;
    }
    
    .status-yellow {
        background-color: #FBBC05;
        box-shadow: 0 0 5px #FBBC05;
    }
    
    .status-red {
        background-color: #EA4335;
        box-shadow: 0 0 5px #EA4335;
    }
    
    .status-blue {
        background-color: #4285F4;
        box-shadow: 0 0 5px #4285F4;
    }
    
    /* Hide hamburger menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
        unsafe_allow_html=True,
    )
