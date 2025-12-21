

import numpy as np
import matplotlib.pyplot as plt

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

def generate_weather_data(start, end, num_points, a, b, c, noise_factor=10):
    x = np.linspace(start, end, num_points)
    y = quadratic_model(x, a, b, c) + np.random.normal(0, noise_factor, num_points)
    return x, y

def plot_weather_data(x, y, title):
    plt.scatter(x, y, label="Weather Data")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.title(title)
    plt.legend()
    plt.show()

a = 0.5
b = -5
c = 20

start_time = 0
end_time = 10
num_points = 100

x_data, y_data = generate_weather_data(start_time, end_time, num_points, a, b, c)
plot_weather_data(x_data, y_data, "Waterfall Model: Weather Data")

