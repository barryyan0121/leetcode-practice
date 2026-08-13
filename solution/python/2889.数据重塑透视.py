import pandas as pd
from pandas.testing import assert_frame_equal


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index="month", columns="city", values="temperature"
    ).reset_index()


class Solution:
    def pivotTable(self, weather: pd.DataFrame) -> pd.DataFrame:
        return pivotTable(weather)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {
                    "city": ["Jacksonville", "Jacksonville", "ElPaso", "ElPaso"],
                    "month": ["January", "February", "January", "February"],
                    "temperature": [13, 23, 20, 6],
                }
            ),
            pd.DataFrame(
                {
                    "month": ["February", "January"],
                    "ElPaso": [6, 20],
                    "Jacksonville": [23, 13],
                }
            ).rename_axis(columns="city"),
        )
    ]

    solver = Solution()
    for index, (weather, expected) in enumerate(test_cases):
        actual = solver.pivotTable(weather.copy())
        assert_frame_equal(actual, expected), f"case {index} failed"
