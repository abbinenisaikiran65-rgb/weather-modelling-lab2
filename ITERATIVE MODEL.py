import matplotlib.pyplot as plt 
import numpy as np
def quadratic_model(x, a, b, c):
  return a * x**2 + b* x + c
def generate_weather_data(start, end, num_points, a, b, c, noise_factor=10): 
  x = np.linspace(start, end, num_points) 
  y = quadratic_model(x, a, b, c) + np.random.normal(0, noise_factor, num_points)
  return x, y
def plot_weather_data(x, y, title):
  plt.scatter(x, y, label='Weather Data')
  plt.title(title)
  plt.xlabel('Time')
  plt.ylabel(Temperature')
  plt.legend()
  plt.show()
a_initial = 0.5
b initial =-5
c_initial = 20
start_time = 0
end_time = 10
num points = 100
x_data, y_initial = generate_weather_data(start_time, end_time, num_points, a_initial, b_initial, c_initial)
plot_weather_data(x_data, y_initial, 'Iterative Model: Initial Weather Data')
for iteration in range(1, num_iterations + 1):
  print(f"\nlteration {iteration}: Gather feedback and refine the model.")
  a_iterative = float(input("Enter new value for 'a': "))
  b_iterative = float(input("Enter new value for 'b': "))
  c_iterative = float(input("Enter new value for 'c': "))
  plot_weather_data(x_data, y_iterative, f'lterative Model: Iteration {iteration) Weather Data')
if iteration == num_iterations:
print(f"\nTemperature values for Iteration {iteration}:\n{y_iterative}")
plot_weather_data(x_data, y_iterative, 'Iterative Model: Final Weather Data')
