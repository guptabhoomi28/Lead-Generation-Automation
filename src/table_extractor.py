import io
import requests
import pdfplumber
import pandas as pd
from cleaner import clean_tables , clean_dataframe


PDF_URL = (
    "https://portal.mcgm.gov.in/irj/go/km/docs/documents/"
    "HomePage%20Data/NGO%20Directory%202025%20.pdf"
)


def download_pdf(url: str) -> bytes:
    response = requests.get(
        url,
        timeout=30,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response.raise_for_status()
    return response.content


def extract_tables(pdf_bytes: bytes) -> list[list[list[str]]]:
    tables = []

    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):

            page_tables = page.extract_tables()

            tables.extend(page_tables)

    return tables

def get_cleaned_data():
    print("Downloading BMC NGO Directory...")

    pdf_bytes = download_pdf(PDF_URL)

    print("Extracting tables...")

    tables = extract_tables(pdf_bytes)

    print(f"Total tables extracted: {len(tables)}")

    df = clean_tables(tables)
    df = clean_dataframe(df)

    return df

def main():
    df = get_cleaned_data()

    print("\nDataFrame shape:", df.shape)

    print("\nEmail status counts:")
    print(df["Email Status"].value_counts())

    print("\nFirst 10 rows:")
    print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()