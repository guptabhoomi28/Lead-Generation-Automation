import pandas as pd
import re


def clean_tables(tables):
    rows = []

    for table in tables:
        if not table:
            continue

        header = table[0]

        for row in table[1:]:
            if not row:
                continue

            if len(row) != len(header):
                continue

            rows.append(row)

    df = pd.DataFrame(rows, columns=header)

    return df

def clean_text(value):
    if pd.isna(value):
        return ""

    value = str(value)
    value = value.replace("\n" , " ")
    value = " ".join(value.split())

    return value.strip()

def clean_email(value):

    if pd.isna(value):
        return ""

    email = str(value).strip()
    email = re.sub(r"\s+(?=[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})" , "" ,email)
    email = re.sub(r"\s*/\s*" , "/" , email)
    email = re.sub(r"\s*@\s*" , "@" , email)
    email = re.sub(r"\s*\.\s*" , "." , email)

    parts = email.split("/")

    cleaned_parts =[]

    for part in parts:
        part = re.sub("\s+" , "" , part)
        cleaned_parts.append(part)


    return email

def validate_email(email):
    if not email or email.lower() in {"not specified" , "na" , "n/a" , "none" , "not available"}:
        return "Missing"

    email_regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.match(email_regex , email):
        return "Valid"

    return "Invalid"

def remove_duplicates(df):
    df = df.copy()

    df["_name_key"] = (
        df["Name of the Institution"].str.lower().str.strip()
    )

    df["_email_key"] = (
        df["Email ID"].str.lower().str.strip()
    )

    df["_email_key"] = df["_email_key"].replace("", "__missing__")

    df = df.drop_duplicates(
        subset=["_name_key", "_email_key"],
        keep="first"
    )

    df = df.drop(columns=["_name_key", "_email_key"])

    return df

def split_multiple_email(df):
    df = df.copy()

    df['Email ID'] = df['Email ID'].str.split(r"/|&")
    df=df.explode('Email ID')

    df['Email ID']= df['Email ID'].apply(clean_email)
    df['Email Status']= df['Email ID'].apply(validate_email)

    return df

def clean_dataframe(df):
    df= df.copy()

    for column in df.columns:
        df[column] = df[column].apply(clean_text)

    df['Email ID'] = df['Email ID'].apply(clean_email)
    df['Email Status'] = df['Email ID'].apply(validate_email)

    df=remove_duplicates(df)
    df=split_multiple_email(df)

    return df

