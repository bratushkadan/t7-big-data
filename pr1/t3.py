import sys

ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "//": lambda x, y: x // y,
    "abs": lambda x, y: abs(x - y),
    "**": lambda x, y: x**y,
}
ops["pow"] = ops["**"]

if __name__ == "__main__":
    stra, strb, op = sys.argv[1:]
    a, b = float(stra), float(strb)
    print(ops[op](a, b))
