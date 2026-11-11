import time

def fib_rec(n):
    return n if n < 2 else fib_rec(n - 1) + fib_rec(n - 2)

def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    start = time.perf_counter()
    fib_loop(40)
    print("Давталт:", time.perf_counter() - start, "сек")

    start = time.perf_counter()
    fib_rec(40)
    print("Рекурс:", time.perf_counter() - start, "сек")