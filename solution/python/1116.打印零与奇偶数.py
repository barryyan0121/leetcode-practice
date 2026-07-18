from threading import Semaphore, Thread


class ZeroEvenOdd:
    def __init__(self, n: int):
        self.n = n
        self.zero_turn = Semaphore(1)
        self.odd_turn = Semaphore(0)
        self.even_turn = Semaphore(0)

    def zero(self, printNumber) -> None:
        for number in range(1, self.n + 1):
            self.zero_turn.acquire()
            printNumber(0)
            (self.odd_turn if number % 2 else self.even_turn).release()

    def even(self, printNumber) -> None:
        for number in range(2, self.n + 1, 2):
            self.even_turn.acquire()
            printNumber(number)
            self.zero_turn.release()

    def odd(self, printNumber) -> None:
        for number in range(1, self.n + 1, 2):
            self.odd_turn.acquire()
            printNumber(number)
            self.zero_turn.release()


if __name__ == "__main__":
    test_cases = [(1, "01"), (5, "0102030405")]
    for _, (n, expected) in enumerate(test_cases):
        output = []
        zero_even_odd = ZeroEvenOdd(n)
        threads = [
            Thread(target=zero_even_odd.even, args=(output.append,)),
            Thread(target=zero_even_odd.odd, args=(output.append,)),
            Thread(target=zero_even_odd.zero, args=(output.append,)),
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        assert "".join(map(str, output)) == expected
