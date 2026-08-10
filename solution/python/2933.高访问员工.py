"""2933. 高访问员工"""

from collections import defaultdict


class Solution:
    def findHighAccessEmployees(self, access_times: list[list[str]]) -> list[str]:
        visits = defaultdict(list)
        for name, moment in access_times:
            visits[name].append(int(moment[:2]) * 60 + int(moment[2:]))
        answer = []
        for name, times in visits.items():
            times.sort()
            if any(
                times[index + 2] - times[index] < 60 for index in range(len(times) - 2)
            ):
                answer.append(name)
        return answer


if __name__ == "__main__":
    assert Solution().findHighAccessEmployees(
        [["a", "0549"], ["a", "0558"], ["a", "0610"]]
    ) == ["a"]
