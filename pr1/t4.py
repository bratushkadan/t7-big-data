# не можем сделать проверку a - b == 0 для float
delta = 1e-8

if __name__ == "__main__":
    sum = 0.0
    squares_sum = 0.0
    while True:
        n = float(input())
        sum += n
        squares_sum += n**2
        if delta > sum:
            break
    print(squares_sum)
