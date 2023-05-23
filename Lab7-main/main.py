import cv2
import numpy as np

image = cv2.imread("//Users//ezgi//Downloads//pythonPicture.jpeg")
cv2.imshow("Original Picture", image)
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

lowerBound = np.array([100, 50, 100])
upperBound = np.array([250, 250, 250])
R = cv2.inRange(image, lowerBound, upperBound)
merged = cv2.merge([B, G, R])
cv2.imshow("New", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
