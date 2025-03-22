import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_mock_data():
    """Generate mock data for dashboard demonstration

    This function creates a structured dataset that represents the various
    metrics and indicators needed for the Custodian Operations Dashboard.

    Returns:
        dict: A dictionary containing all the mock data needed for the dashboard
    """

    # Set random seed for reproducibility
    np.random.seed(42)

    # Current date for reference
    today = datetime.now().date()

    # Create date range for past 30 days
    date_range = [today - timedelta(days=i) for i in range(30)]
    date_range.reverse()  # Earliest to latest

    # KPI data
    kpi_data = {
        "pending_exports_surat": 87,
        "pending_exports_mumbai": 46,
        "pending_imports_surat": 52,
        "pending_imports_mumbai": 38,
        "delayed_exports": 14,
        "delayed_imports": 9,
        "delayed_exports_surat": 9,
        "delayed_exports_mumbai": 5,
        "delayed_imports_surat": 6,
        "delayed_imports_mumbai": 3,
        "customs_hold_surat": 22,
        "customs_hold_mumbai": 6,
        "weight_surat": "8,500 Carats & 230 Kg",
        "weight_mumbai": "6,300 Carats & 185 Kg",
        "processing_efficiency": 92,
        "efficiency_trend": 3.5,
    }

    # Stock breakdown data
    stock_breakdown = pd.DataFrame(
        {
            "location": [
                "Surat",
                "Surat",
                "Surat",
                "Mumbai, Sahar",
                "Mumbai, Sahar",
                "Mumbai, Sahar",
            ],
            "commodity_type": [
                "Diamonds (Natural)",
                "Diamonds (Lab-Grown)",
                "Jewelry",
                "Diamonds (Natural)",
                "Diamonds (Lab-Grown)",
                "Jewelry",
            ],
            "weight": [5200, 3300, 230, 4100, 2200, 185],
        }
    )

    # Efficiency data for last 7 days
    efficiency_dates = [today - timedelta(days=i) for i in range(6, -1, -1)]

    export_efficiency = [88, 89, 91, 87, 92, 94, 93]
    import_efficiency = [85, 86, 88, 90, 89, 91, 92]

    efficiency_data = pd.DataFrame(
        {
            "date": efficiency_dates * 2,
            "type": ["Export"] * 7 + ["Import"] * 7,
            "efficiency": export_efficiency + import_efficiency,
        }
    )

    # Export commodity data
    export_commodity = pd.DataFrame(
        {
            "location": [
                "Surat",
                "Surat",
                "Surat",
                "Surat",
                "Mumbai, Sahar",
                "Mumbai, Sahar",
                "Mumbai, Sahar",
            ],
            "commodity": [
                "Natural Diamonds",
                "Lab-Grown Diamonds",
                "Gold Jewelry",
                "Silver Jewelry",
                "Natural Diamonds",
                "Lab-Grown Diamonds",
                "Gold Jewelry",
            ],
            "type": [
                "Rough",
                "Polished",
                "Studded",
                "Plain",
                "Rough",
                "Polished",
                "Studded",
            ],
            "weight": [2800, 1400, 120, 110, 2200, 1100, 95],
        }
    )

    # Import commodity data
    import_commodity = pd.DataFrame(
        {
            "location": [
                "Surat",
                "Surat",
                "Surat",
                "Mumbai, Sahar",
                "Mumbai, Sahar",
                "Mumbai, Sahar",
            ],
            "commodity": [
                "Natural Diamonds",
                "Lab-Grown Diamonds",
                "Gold Jewelry",
                "Natural Diamonds",
                "Lab-Grown Diamonds",
                "Gold Jewelry",
            ],
            "type": ["Rough", "Rough", "Plain", "Rough", "Rough", "Plain"],
            "weight": [3200, 1800, 150, 2500, 1400, 125],
        }
    )

    # Export summary
    export_summary = {
        "total_weight": "6,500 Carats & 325 Kg",
        "total_value": "64.5 Million",
        "highest_weight": "520 Carats",
        "highest_value": "3.2 Million",
    }

    # Import summary
    import_summary = {
        "total_weight": "8,900 Carats & 275 Kg",
        "total_value": "78.2 Million",
        "highest_weight": "680 Carats",
        "highest_value": "4.5 Million",
    }

    # Transit data
    transit_data = {
        "surat_to_mumbai": {
            "in_transit": 38,
            "pending_carting": 5,
            "received_today": 52,
        },
        "mumbai_to_surat": {
            "in_transit": 44,
            "pending_transport": 8,
            "received_today": 50,
        },
    }

    # Customs data
    customs_data = {
        "export": {"pending_leo": 6, "confirm_pctm": 4, "confirm_tp": 3},
        "import": {"pending_boe": 4, "pending_examination": 7},
    }

    # Flight data
    flight_data = {"ready_for_flight": 35, "loaded_onto_flights": 20}

    # Delivery data
    delivery_data = {"ready_for_delivery": 23, "delivered_today": 12}

    # Exception data
    exceptions = {
        "export": {"offloaded": 3, "returns": 2},
        "import": {"broken_seals": 2, "reforwarding": 4},
    }

    # Financial data
    financial_data = {
        "service_charges_today": "15,450",
        "pending_invoice": "3,200",
        "demurrage": {"pending": "7,100", "paid": "25,500"},
        "system_usage": {
            "active_users": 8,
            "pending_approvals": 12,
            "system_load": 42,
            "background_processes": 7,
        },
    }

    # Revenue data
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    export_revenue = [24500, 26300, 28700, 25900, 30200, 32100]
    import_revenue = [30100, 28500, 32400, 29800, 34600, 36800]
    service_revenue = [8200, 8600, 9100, 8900, 10300, 11400]

    revenue_data = pd.DataFrame(
        {
            "month": months * 3,
            "type": ["Export"] * 6 + ["Import"] * 6 + ["Services"] * 6,
            "amount": export_revenue + import_revenue + service_revenue,
        }
    )

    # Commodity distribution for pie chart
    commodity_distribution = pd.DataFrame(
        {
            "location": [
                "Surat",
                "Surat",
                "Surat",
                "Surat",
                "Mumbai, Sahar",
                "Mumbai, Sahar",
                "Mumbai, Sahar",
            ],
            "commodity": [
                "Natural Diamonds",
                "Lab-Grown Diamonds",
                "Gold Jewelry",
                "Silver Jewelry",
                "Natural Diamonds",
                "Lab-Grown Diamonds",
                "Gold Jewelry",
            ],
            "value": [42, 28, 18, 12, 45, 32, 23],
        }
    )

    # Date trends for last 14 days
    trend_dates = [today - timedelta(days=i) for i in range(13, -1, -1)]
    exports_trend = [45, 48, 52, 49, 55, 58, 52, 56, 60, 58, 62, 59, 65, 68]
    imports_trend = [40, 42, 45, 48, 46, 50, 52, 49, 54, 56, 53, 58, 60, 62]

    date_trends = pd.DataFrame(
        {"date": trend_dates, "exports": exports_trend, "imports": imports_trend}
    )

    # Top contributors
    top_exporters = pd.DataFrame(
        {
            "name": ["DDPL", "SRK", "Vgrown", "Paladiya Brothers", "KGK"],
            "value": [980, 850, 720, 650, 580],
        }
    )

    top_importers = pd.DataFrame(
        {
            "name": ["DDPL", "SRK", "Kiran Gems", "Paladiya Brothers", "KGK"],
            "value": [1050, 920, 780, 710, 630],
        }
    )

    top_console_agents = pd.DataFrame(
        {
            "name": ["Malca", "Sequel", "Ferrari", "BVC", "FedEx"],
            "value": [125, 110, 95, 82, 78],
        }
    )

    top_contributors = {
        "exporters": top_exporters,
        "importers": top_importers,
        "console_agents": top_console_agents,
    }

    # Location comparison
    location_comparison = pd.DataFrame(
        {
            "category": [
                "Export Parcels",
                "Import Parcels",
                "In Transit",
                "Customs Hold",
                "Ready for Delivery",
            ],
            "surat": [87, 52, 44, 22, 23],
            "mumbai": [46, 38, 38, 6, 0],
        }
    )

    # Export and import data for detailed view
    export_data = pd.DataFrame(
        {
            "parcel_id": [f"EXP{i:04d}" for i in range(1, 101)],
            "location": np.random.choice(["Surat", "Mumbai, Sahar"], 100, p=[0.7, 0.3]),
            "commodity": np.random.choice(
                [
                    "Natural Diamonds",
                    "Lab-Grown Diamonds",
                    "Gold Jewelry",
                    "Silver Jewelry",
                ],
                100,
            ),
            "weight": np.random.randint(50, 500, 100),
            "value": np.random.randint(10000, 1000000, 100) / 100,
            "status": np.random.choice(
                [
                    "Pending",
                    "In Transit",
                    "Customs Hold",
                    "Ready for Export",
                    "Exported",
                ],
                100,
                p=[0.3, 0.2, 0.1, 0.2, 0.2],
            ),
            "date": [
                today - timedelta(days=np.random.randint(0, 20)) for _ in range(100)
            ],
        }
    )

    import_data = pd.DataFrame(
        {
            "parcel_id": [f"IMP{i:04d}" for i in range(1, 101)],
            "location": np.random.choice(["Surat", "Mumbai, Sahar"], 100, p=[0.6, 0.4]),
            "commodity": np.random.choice(
                [
                    "Natural Diamonds",
                    "Lab-Grown Diamonds",
                    "Gold Jewelry",
                    "Silver Jewelry",
                ],
                100,
            ),
            "weight": np.random.randint(50, 500, 100),
            "value": np.random.randint(10000, 1000000, 100) / 100,
            "status": np.random.choice(
                [
                    "Arrived",
                    "In Transit",
                    "Customs Hold",
                    "Ready for Delivery",
                    "Delivered",
                ],
                100,
                p=[0.25, 0.2, 0.15, 0.2, 0.2],
            ),
            "date": [
                today - timedelta(days=np.random.randint(0, 20)) for _ in range(100)
            ],
        }
    )

    # Combine all data into a single dictionary
    data = {
        "kpi_data": kpi_data,
        "stock_breakdown": stock_breakdown,
        "efficiency_data": efficiency_data,
        "export_commodity": export_commodity,
        "import_commodity": import_commodity,
        "export_summary": export_summary,
        "import_summary": import_summary,
        "transit_data": transit_data,
        "customs_data": customs_data,
        "flight_data": flight_data,
        "delivery_data": delivery_data,
        "exceptions": exceptions,
        "financial_data": financial_data,
        "revenue_data": revenue_data,
        "commodity_distribution": commodity_distribution,
        "date_trends": date_trends,
        "top_contributors": top_contributors,
        "location_comparison": location_comparison,
        "export_data": export_data,
        "import_data": import_data,
    }

    return data
