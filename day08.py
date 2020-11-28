import numpy as np


with open("day08.txt") as f:
    file = f.read().strip()

image = np.array([int(pixel) for pixel in file]).reshape((-1, 6, 25))
layer = np.argmin((image == 0).sum((1, 2)))
result = (image[layer, :, :] == 1).sum() * (image[layer, :, :] == 2).sum()
print("Part 1:", result)

message = image[-1]
for layer in range(-2, -image.shape[0], -1):
    message[layer]
