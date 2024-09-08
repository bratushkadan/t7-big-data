import math
import sys


def calc_area(shape: str, *measurements):
    if shape == "circle":
        return {"circle": math.pi * measurements[0] ** 2}
    if shape == "square":
        return {"square": measurements[0] ** 2}
    if shape == "rectangle":
        return {"square": measurements[0] * measurements[1]}
    raise Exception(f"no implementaion of calc_area() for such shape {shape}")


if __name__ == "__main__":
    shape = sys.argv[1]
    measurements = list(map(float, sys.argv[2:]))
    print(calc_area(shape, *measurements))
