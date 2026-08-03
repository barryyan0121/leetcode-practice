# @lc app=leetcode.cn id=1723 lang=python3


class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        jobs.sort(reverse=True)
        workers = [0] * k
        answer = sum(jobs)

        def search(index: int, current: int) -> None:
            nonlocal answer
            if current >= answer:
                return
            if index == len(jobs):
                answer = current
                return
            used = set()
            for worker in range(k):
                if workers[worker] in used:
                    continue
                used.add(workers[worker])
                workers[worker] += jobs[index]
                search(index + 1, max(current, workers[worker]))
                workers[worker] -= jobs[index]
                if workers[worker] == 0:
                    break

        search(0, 0)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minimumTimeRequired, ([3, 2, 3], 3), 3),
        (solution.minimumTimeRequired, ([1, 2, 4, 7, 8], 2), 11),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1723 题 "完成所有工作的最短时间" 所有测试用例通过')
