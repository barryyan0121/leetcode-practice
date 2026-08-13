import pandas as pd


def dropDuplicateCustomers(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])
