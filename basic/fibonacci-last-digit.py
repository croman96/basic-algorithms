# python3


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n < 2:
        return n
    else:
        fibonacci = [None] * (n + 1)
        fibonacci[0] = 0
        fibonacci[1] = 1
        for i in range(2, n+1):
            fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 10
        return fibonacci[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
