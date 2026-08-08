#
# @lc app=leetcode.cn id=1195 lang=python3
#
# [1195] 多线程 Fizz Buzz
#


# @lc code=start
from threading import Condition


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.condition = Condition()

    def _run(self, predicate, callback):
        while True:
            with self.condition:
                while self.current <= self.n and not predicate(self.current):
                    self.condition.wait()
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                callback()
                self.current += 1
                self.condition.notify_all()

    def fizz(self, printFizz: "Callable[[], None]") -> None:
        self._run(lambda value: value % 3 == 0 and value % 5 != 0, printFizz)

    def buzz(self, printBuzz: "Callable[[], None]") -> None:
        self._run(lambda value: value % 5 == 0 and value % 3 != 0, printBuzz)

    def fizzbuzz(self, printFizzBuzz: "Callable[[], None]") -> None:
        self._run(lambda value: value % 15 == 0, printFizzBuzz)

    def number(self, printNumber: "Callable[[int], None]") -> None:
        self._run(
            lambda value: value % 3 != 0 and value % 5 != 0,
            lambda: printNumber(self.current),
        )


# @lc code=end


if __name__ == "__main__":
    from threading import Thread

    test_cases = [(5, ["1", "2", "fizz", "4", "buzz"])]
    for index, (limit, expected) in enumerate(test_cases):
        output = []
        fizz_buzz = FizzBuzz(limit)
        threads = [
            Thread(target=fizz_buzz.fizz, args=(lambda: output.append("fizz"),)),
            Thread(target=fizz_buzz.buzz, args=(lambda: output.append("buzz"),)),
            Thread(
                target=fizz_buzz.fizzbuzz, args=(lambda: output.append("fizzbuzz"),)
            ),
            Thread(
                target=fizz_buzz.number, args=(lambda value: output.append(str(value)),)
            ),
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        assert output == expected, index
