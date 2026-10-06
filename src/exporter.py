import pandas as pd


def prepare_leads(df):
    leads = pd.DataFrame()

    leads["Name"] = df["Name of the Institution"]
    leads["Email"] = df["Email ID"]

    leads["Location"] = df["Address"]

    leads["Phone"] = df["Contact No."]
    leads["Category"] = df["Area of Work"]
    leads["Email Status"] = df["Email Status"]

    leads["Source"] = "BMC NGO Directory 2025"

    return leads


def export_to_excel(df, filename="lead_generation_output.xlsx"):
    leads = prepare_leads(df)

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        leads.to_excel(
            writer,
            sheet_name="Leads",
            index=False
        )

        summary = pd.DataFrame({
            "Metric": [
                "Total Leads",
                "Valid Emails",
                "Invalid Emails",
                "Missing Emails"
            ],
            "Count": [
                len(leads),
                (leads["Email Status"] == "Valid").sum(),
                (leads["Email Status"] == "Invalid").sum(),
                (leads["Email Status"] == "Missing").sum()
            ]
        })

        summary.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

    print(f"Excel file created: {filename}")