import numpy as np

data = np.array(
    [
        [22.5, 19.0, 31.2, 28.7, 25.1],
        [17.3, 22.8, 30.5, 26.4, 21.9],
        [33.1, 29.6, 18.4, 24.0, 27.8],
        [20.2, 23.5, 31.9, 28.1, 22.6],
    ]
)

# Task 1 - Print the shape of data
print("Shape of the data: ", np.shape(data))

# Mean temperature per station
print("Mean temperature per station: ", np.mean(data, axis=0))

# Task 2 Using a boolean mask
bool_data = data > 28
print("Boolean Data: ", bool_data)

# Printing them as 1D array
result = data[bool_data]
print("1D Boolean Array: ", result)

# Task 3 Normalize the entire data
normalized = (data - data.min()) / (data.max() - data.min())
normalized_round = np.round(normalized, 2)
print("Normalized value: ", normalized_round)
