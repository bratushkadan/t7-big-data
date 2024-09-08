if __name__ == "__main__":
    n = int(input("Введите число: "))
    for i in range(1, n + 1):
        for k in range(i):
            print(i, end=" ")
