"""2881. 创建新列"""

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees


if __name__ == "__main__":
    employees = pd.DataFrame({"name": ["Piper", "Grace"], "salary": [4548, 28150]})
    expected = pd.DataFrame({"name": ["Piper", "Grace"], "salary": [4548, 28150], "bonus": [9096, 56300]})
    assert createBonusColumn(employees).equals(expected)
    print("测试用例通过")
