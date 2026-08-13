"""2877. 从表中创建DataFrame"""

import pandas as pd


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])


if __name__ == "__main__":
    student_data = [[1, 15], [2, 11], [3, 20]]
    expected = pd.DataFrame(student_data, columns=["student_id", "age"])
    assert createDataframe(student_data).equals(expected)
    print("测试用例通过")
