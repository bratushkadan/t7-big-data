import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([0, 9, 4, 9, 0])

    plt.figure()
    plt.plot(a, b)
    plt.show()
