import numpy as np

array = np.random.randint(low=0, high=1000, size=(5, 5), dtype=int)

print(f"Full array: {array} \n")

print(f"2nd Row, 3rd Column: {array[1][2]} \n")

print(f"Sum of array: {np.sum(array)} \n")

print(f"Mean of each row: {np.mean(array, axis=1)} \n")

print(f"Max value of each column: {np.max(array, axis=0)}")