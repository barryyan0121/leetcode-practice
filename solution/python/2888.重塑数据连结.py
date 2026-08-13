import pandas as pd
from pandas.testing import assert_frame_equal


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], ignore_index=True)


class Solution:
    def concatenateTables(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        return concatenateTables(df1, df2)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame({"student_id": [1, 2], "name": ["Ada", "Grace"]}),
            pd.DataFrame({"student_id": [3], "name": ["Linus"]}),
            pd.DataFrame(
                {"student_id": [1, 2, 3], "name": ["Ada", "Grace", "Linus"]}
            ),
        )
    ]

    solver = Solution()
    for index, (df1, df2, expected) in enumerate(test_cases):
        actual = solver.concatenateTables(df1.copy(), df2.copy())
        assert_frame_equal(actual, expected), f"case {index} failed"
