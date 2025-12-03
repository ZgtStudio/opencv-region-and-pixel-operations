import cv2 # import OpenCV

image = cv2.imread("Deer.jpg") # read the image

# section the area and copy this another place
section = image[300:600,400:700]
image[400:700,500:800] = section

# filter the section area
image[300:600,400:700] = (0, 155, 200)

cv2.imshow("Deer", image) # show the image in a window titled "Deer"

# wait for a key press and then close all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()