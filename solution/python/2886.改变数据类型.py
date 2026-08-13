import pandas as pd
from pandas.testing import assert_frame_equal


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students


class Solution:
    def changeDatatype(self, students: pd.DataFrame) -> pd.DataFrame:
        return changeDatatype(students)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame({"student_id": [1, 2], "grade": [90.0, 85.0]}),
            pd.DataFrame({"student_id": [1, 2], "grade": [90, 85]}),
        )
    ]

    solver = Solution()
    for index, (students, expected) in enumerate(test_cases):
        actual = solver.changeDatatype(students.copy())
        assert_frame_equal(actual, expected), f"case {index} failed"
