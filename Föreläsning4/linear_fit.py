import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_function(x, a, b):
    return a * x + b

def read_data(filename):
    data = np.loadtxt(filename)
    return data[:, 0], data[:, 1]

def main():
    filename = "data.txt" 
    x, y = read_data(filename)
    
    params, covariance = curve_fit(linear_function, x, y)
    a, b = params
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label='Data', color='darkorange')
    plt.plot(x, linear_function(x, a, b), label=f'Fit: y = {a:.2f}x + {b:.2f}', color='darkblue', linewidth=3)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()


