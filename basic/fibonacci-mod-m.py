# python3


def fibonacci_number(n):
    fibonacci = [None] * (n + 1)
    fibonacci[0] = 0
    fibonacci[1] = 1
    for i in range(2, n+1):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    return fibonacci[n]


def pisano_period(n, m):
    if n < 2:
        return n
    else:
        fibonacci = [None] * n
        pisano = [None] * n

        fibonacci[0] = 0
        fibonacci[1] = 1

        pisano[0] = 0
        pisano[1] = 1

        flag = False

        for i in range(2, n+1):
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
            pisano[i] = fibonacci[i] % m

            if pisano[i] == 0:
                flag = True
            elif pisano[i] == 1 and flag:
                return pisano[:-2]
            else:
                flag = False


def fibonacci_number_again(n, m):
    period_length = len(pisano_period(n, m))
    
    return fibonacci_number(n % period_length) % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
