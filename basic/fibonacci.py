# python3


def fibonacci_number(n):

    if n < 2:
        return n
    else:
        fibonacci = [None] * (n + 1)
        fibonacci[0] = 0
        fibonacci[1] = 1
        for i in range(2, n+1):
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        return fibonacci[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
