"""2883. 删去丢失的数据"""

import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])


if __name__ == "__main__":
    students = pd.DataFrame({"student_id": [32, 217, 779], "name": ["Piper", None, "Georgia"], "age": [5, 19, 20]})
    expected = students.iloc[[0, 2]]
    assert dropMissingData(students).equals(expected)
    print("测试用例通过")
