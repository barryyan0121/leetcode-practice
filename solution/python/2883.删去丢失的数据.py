import pandas as pd
from pandas.testing import assert_frame_equal


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])


class Solution:
    def dropMissingData(self, students: pd.DataFrame) -> pd.DataFrame:
        return dropMissingData(students)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {
                    "student_id": [32, 217, 779],
                    "name": ["Piper", None, "Georgia"],
                    "age": [5, 19, 20],
                }
            ),
            pd.DataFrame(
                {"student_id": [32, 779], "name": ["Piper", "Georgia"], "age": [5, 20]},
                index=[0, 2],
            ),
        )
    ]

    solver = Solution()
    for index, (students, expected) in enumerate(test_cases):
        actual = solver.dropMissingData(students)
        assert_frame_equal(actual, expected), f"case {index} failed"
