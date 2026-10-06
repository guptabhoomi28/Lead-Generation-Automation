from src.table_extractor import get_cleaned_data
from src.exporter import export_to_excel


def main():
    print("Starting lead generation automation...\n")

    df = get_cleaned_data()

    print(f"\nCleaned records: {len(df)}")

    export_to_excel(df)

    print("\nLead generation automation completed successfully!")


if __name__ == "__main__":
    main()