def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)

if __name__ == "__main__":
    print(sum_digits(0))
    print(sum_digits(7))
    print(sum_digits(-456))
    print(power(2, 0))
    print(power(2, 10))
    print(power(2, -2))