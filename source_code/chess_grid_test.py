import cv2
import numpy as np
import json

# Load the JSON file containing the square coordinates
with open('square.json', 'r') as file:
    square_dict = json.load(file)

# Load the chessboard image
image = cv2.imread('chessboard.jpg')

# Draw the square on the image
for square_key, square_coords in square_dict.items():
    polygon = np.array(square_coords, np.int32).reshape((-1, 1, 2))
    cv2.polylines(image, [polygon], True, (0, 255, 0), thickness=2)


# Display the image with the highlighted square
cv2.imshow('Board', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

