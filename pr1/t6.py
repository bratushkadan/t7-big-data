a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
b = ["a", "b", "c", "c", "c", "b", "a", "c", "a", "a", "b", "c", "b", "a"]

if __name__ == "__main__":
    d = dict()
    for i, v in enumerate(b):
        d[v] = d.get(v, 0) + a[i]
    print(d)
