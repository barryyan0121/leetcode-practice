# @lc app=leetcode.cn id=2305 lang=python3


class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        cookies.sort(reverse=True)
        loads = [0] * k
        answer = sum(cookies)

        def search(index: int, current_max: int) -> None:
            nonlocal answer
            if current_max >= answer:
                return
            if index == len(cookies):
                answer = current_max
                return
            used = set()
            for child in range(k):
                if loads[child] in used:
                    continue
                used.add(loads[child])
                loads[child] += cookies[index]
                search(index + 1, max(current_max, loads[child]))
                loads[child] -= cookies[index]
                if loads[child] == 0:
                    break

        search(0, 0)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.distributeCookies, ([8, 15, 10, 20, 8], 2), 31),
        (solution.distributeCookies, ([6, 1, 3, 2, 2, 4, 1, 2], 3), 7),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2305 题 "公平分发饼干" 所有测试用例通过')
