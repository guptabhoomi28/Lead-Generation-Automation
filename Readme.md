# Lead Generation Automation

## Overview

This project automates the collection, cleaning, validation, and export of NGO lead data from the BMC NGO Directory 2025.

The automation downloads the publicly available BMC NGO Directory PDF, extracts tabular data, cleans the records, validates email addresses, handles duplicate records and multiple email addresses, and exports the final dataset to an Excel workbook.

## Objective

The objective of this project is to build a simple lead-generation automation pipeline that can collect publicly available organization information and convert it into a structured, usable lead dataset.

## Data Source

**Source:** BMC NGO Directory 2025

The source contains information such as:

- Institution Name
- Chairman / CEO
- Local Contact Person
- Address
- Contact Number
- Email ID
- Area of Work
- BMC working status
- Working Since
- FCRA approval
- Ward / Department

## Approach

The automation follows these steps:

1. Download the BMC NGO Directory PDF automatically.
2. Extract tables from the PDF using `pdfplumber`.
3. Convert the extracted tables into a Pandas DataFrame.
4. Clean text fields and remove unnecessary line breaks and spaces.
5. Clean and validate email addresses.
6. Remove duplicate records using organization name and email.
7. Split records containing multiple email addresses into separate rows.
8. Add an email status of Valid, Invalid, or Missing.
9. Prepare the final lead dataset.
10. Export the results to an Excel workbook.

## Project Structure

```text
lead-generation-automation/
│
├── src/
│   ├── table_extractor.py
│   ├── cleaner.py
│   ├── exporter.py
│   └── main.py
│
├── data/
│
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- Pandas
- Requests
- pdfplumber
- OpenPyXL

## Output

The automation generates:

```text
lead_generation_output.xlsx
```

The Excel workbook contains:

### Leads

- Name
- Email
- Website
- Location
- Phone
- Category
- Email Status
- Source

### Summary

- Total Leads
- Valid Emails
- Invalid Emails
- Missing Emails

## Data Cleaning

The pipeline performs basic data cleaning including:

- Removing unnecessary whitespace
- Removing PDF-generated line breaks
- Standardizing email formatting
- Detecting invalid email formats
- Identifying missing email values
- Removing duplicate organization-email combinations
- Separating multiple emails into individual records

The system does not invent or guess missing information. Records that cannot be reliably corrected are retained and marked as invalid or missing.

## Website Information

The BMC NGO Directory does not provide a dedicated Website or LinkedIn field in its extracted table structure. Therefore, the current automation does not fabricate website information and marks unavailable website information accordingly.

## How to Run

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd lead-generation-automation
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the automation

```bash
python src/main.py
```

The generated Excel file will be created automatically.

## Limitations

- Email validation checks email format; it does not verify whether a mailbox actually exists.
- Some PDF records may contain formatting errors that cannot be safely corrected automatically.
- Website and LinkedIn information is not provided by the selected source.
- Location is currently represented using the address provided by the source.

## Future Improvements

Possible improvements include:

- Website and LinkedIn enrichment
- API-based organization enrichment
- Stronger email extraction and correction
- Scheduled automated execution
- Google Sheets integration
- Lead scoring
- Email template generation
- Additional data sources

## Result

The current pipeline successfully extracts and processes hundreds of NGO records from the BMC NGO Directory and automatically generates a structured Excel lead dataset.