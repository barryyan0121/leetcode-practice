import pandas as pd
from pandas.testing import assert_frame_equal


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]


class Solution:
    def selectData(self, students: pd.DataFrame) -> pd.DataFrame:
        return selectData(students)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {
                    "student_id": [101, 53, 128],
                    "name": ["Ulysses", "William", "Henry"],
                    "age": [13, 10, 6],
                }
            ),
            pd.DataFrame({"name": ["Ulysses"], "age": [13]}, index=[0]),
        )
    ]

    solver = Solution()
    for index, (students, expected) in enumerate(test_cases):
        actual = solver.selectData(students)
        assert_frame_equal(actual, expected), f"case {index} failed"
