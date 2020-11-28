import numpy as np


with open("day08.txt") as f:
    file = f.read().strip()

image = np.array([int(pixel) for pixel in file]).reshape((-1, 6, 25))
layer = np.argmin((image == 0).sum((1, 2)))
result = (image[layer] == 1).sum() * (image[layer] == 2).sum()
print("Part 1:", result)

message = np.full_like(image[0], 2)
for layer in image:
    for pixel in range(len(layer.flat)):
        if message.flat[pixel] == 2 and layer.flat[pixel] != 2:
            message.flat[pixel] = layer.flat[pixel]

print("Part 2:")
for row in message:
    for col in row:
        char = "\u001b[40m \u001b[0m" if col == 0 else " "
        print(char, end="")
    print()
