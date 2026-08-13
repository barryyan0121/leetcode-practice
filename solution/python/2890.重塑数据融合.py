import pandas as pd


def meltTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.melt(id_vars=["product"], var_name="quarter", value_name="sales")
