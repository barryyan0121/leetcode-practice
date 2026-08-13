import pandas as pd
from pandas.testing import assert_frame_equal


def meltTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.melt(id_vars=["product"], var_name="quarter", value_name="sales")


class Solution:
    def meltTable(self, weather: pd.DataFrame) -> pd.DataFrame:
        return meltTable(weather)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {
                    "product": ["Umbrella", "SleepingBag"],
                    "quarter_1": [417, 800],
                    "quarter_2": [224, 936],
                    "quarter_3": [379, 93],
                    "quarter_4": [611, 875],
                }
            ),
            pd.DataFrame(
                {
                    "product": [
                        "Umbrella",
                        "SleepingBag",
                        "Umbrella",
                        "SleepingBag",
                        "Umbrella",
                        "SleepingBag",
                        "Umbrella",
                        "SleepingBag",
                    ],
                    "quarter": [
                        "quarter_1",
                        "quarter_1",
                        "quarter_2",
                        "quarter_2",
                        "quarter_3",
                        "quarter_3",
                        "quarter_4",
                        "quarter_4",
                    ],
                    "sales": [417, 800, 224, 936, 379, 93, 611, 875],
                }
            ),
        )
    ]

    solver = Solution()
    for index, (weather, expected) in enumerate(test_cases):
        actual = solver.meltTable(weather.copy())
        assert_frame_equal(actual, expected), f"case {index} failed"
