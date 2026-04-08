#
# @lc app=leetcode.cn id=578 lang=python3
# @lcpr version=30203
#
# [578] 查询回答率最高的问题
#

import sys
import os
from collections import defaultdict
from fractions import Fraction

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def highestAnswerRateQuestion(
        self, survey_log: List[Dict[str, Any]]
    ) -> List[Dict[str, int]]:
        counts: Dict[int, List[int]] = defaultdict(lambda: [0, 0])
        for row in survey_log:
            qid = row["question_id"]
            counts[qid][1] += 1
            if row["action"] == "answer":
                counts[qid][0] += 1

        best_qid = None
        best_rate = None
        for qid, (answered, shown) in counts.items():
            if shown == 0:
                continue
            rate = Fraction(answered, shown)
            if (
                best_rate is None
                or rate > best_rate
                or (rate == best_rate and qid < best_qid)
            ):
                best_rate = rate
                best_qid = qid

        return [{"survey_log": best_qid}] if best_qid is not None else []


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.highestAnswerRateQuestion,
            (
                [
                    {
                        "uid": 5,
                        "action": "show",
                        "question_id": 285,
                        "answer_id": None,
                        "q_num": 1,
                        "timestamp": 123,
                    },
                    {
                        "uid": 5,
                        "action": "answer",
                        "question_id": 285,
                        "answer_id": 124124,
                        "q_num": 1,
                        "timestamp": 124,
                    },
                    {
                        "uid": 5,
                        "action": "show",
                        "question_id": 369,
                        "answer_id": None,
                        "q_num": 2,
                        "timestamp": 125,
                    },
                    {
                        "uid": 5,
                        "action": "skip",
                        "question_id": 369,
                        "answer_id": None,
                        "q_num": 2,
                        "timestamp": 126,
                    },
                ],
            ),
            [{"survey_log": 285}],
        ),
        (
            solution.highestAnswerRateQuestion,
            (
                [
                    {
                        "uid": 1,
                        "action": "show",
                        "question_id": 1,
                        "answer_id": None,
                        "q_num": 1,
                        "timestamp": 1,
                    },
                    {
                        "uid": 1,
                        "action": "answer",
                        "question_id": 1,
                        "answer_id": 11,
                        "q_num": 1,
                        "timestamp": 2,
                    },
                    {
                        "uid": 2,
                        "action": "show",
                        "question_id": 2,
                        "answer_id": None,
                        "q_num": 1,
                        "timestamp": 3,
                    },
                    {
                        "uid": 2,
                        "action": "answer",
                        "question_id": 2,
                        "answer_id": 22,
                        "q_num": 1,
                        "timestamp": 4,
                    },
                ],
            ),
            [{"survey_log": 1}],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)
