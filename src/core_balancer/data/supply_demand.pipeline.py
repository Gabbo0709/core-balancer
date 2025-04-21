# Supply demand pipeline
import pandas as pd


def get_data() -> pd.DataFrame:
    """
    Get the data from the supply demand sheet in the excel file.
    """
    # Read the supply demand sheet from the excel file
    df = pd.read_excel(
        "data/input/Hackathon DB Final.xlsx",
        sheet_name="Supply_Demand",
        header=0,
    )
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Get all quarters from the supply demand sheet
    # These are in the first row of the sheet
    quarters = df.iloc[0].values.tolist()
    # Remove the null values from the list
    quarters = [q for q in quarters if q is not None and q != ""]
    # Remove the first row from the dataframe
    df = df.iloc[1:]
    # Get week periods from the supply demand sheet
    # These are now in the first row of the sheet
    week_periods = df.iloc[0].values.tolist()
    # Remove the null values from the list
    week_periods = [wp for wp in week_periods if wp is not None and wp != ""]
    # Remove the first row from the dataframe
    df = df.iloc[1:]
    # Get period date start from the supply demand sheet
    # These are now in the first row of the sheet
    period_date_start = df.iloc[0].values.tolist()
    # Remove the vales not in the format DD-MM-YY from the list
    period_date_start = [
        pd.to_datetime(pd.to_numeric(p), format="%d-%m-%y", errors="coerce")
        for p in period_date_start
    ]
    # Remove the null values from the list
    period_date_start = [
        p for p in period_date_start if p is not pd.NaT and p != ""
    ]
    # Remove the first row from the dataframe
    df = df.iloc[1:]
    #  Get product ids from the supply demand sheet
    # These are now in the first column of the sheet
    product_ids = df.iloc[:, 0].values.tolist().unique()
    # Set conditions
    conditions = [
        df[0] == product_id
        for product_id in product_ids
    ]
    # Get the matching rows for each product id
    matching_rows = [
        df[condition].iloc[:, 1:].values.tolist()
        for condition in conditions
    ]
    # Get the product ids
    product_ids = [
        df[condition].iloc[:, 0].values.tolist()
        for condition in conditions
    ]


