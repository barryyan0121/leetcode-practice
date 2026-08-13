import pandas as pd
from pandas.testing import assert_frame_equal


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])


class Solution:
    def createDataframe(self, student_data: list[list[int]]) -> pd.DataFrame:
        return createDataframe(student_data)


if __name__ == "__main__":
    test_cases = [
        (
            [[1, 15], [2, 11], [3, 20]],
            pd.DataFrame([[1, 15], [2, 11], [3, 20]], columns=["student_id", "age"]),
        )
    ]

    solver = Solution()
    for index, (student_data, expected) in enumerate(test_cases):
        actual = solver.createDataframe(student_data)
        assert_frame_equal(actual, expected), f"case {index} failed"
