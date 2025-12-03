import cv2 # import OpenCV

image = cv2.imread("Duck.jpg") # read the image

cv2.rectangle(image, (245, 80), (355, 155), [0, 0, 155], 2) # draw a rectangle on the selected region of the image

cv2.imshow("Duck", image) # display the image in a window titled "Duck"

# wait for a key press, then close all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()