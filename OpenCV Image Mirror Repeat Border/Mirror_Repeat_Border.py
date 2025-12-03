import cv2 # import OpenCV

# create different types of borders around the image
image = cv2.imread("Griaffe.jpg") # read the image
reflected_image = cv2.copyMakeBorder(image, 100, 100, 150, 150, cv2.BORDER_REFLECT) # show the reflected border image
replicated_image = cv2.copyMakeBorder(image, 120,120,120,120, cv2.BORDER_REPLICATE) # show the replicated border image
wrapped_image = cv2.copyMakeBorder(image, 300, 300, 300, 300, cv2.BORDER_WRAP) # show the wrapped border image
constanted_image = cv2.copyMakeBorder(image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, 
                                      value = (75, 100, 255)) # show the constant-color border image


cv2.imshow("Reflected Griaffe", reflected_image) # explore the reflected image to window titled "Reflected Griaffe"
cv2.imshow("Replicated Griaffe", replicated_image) # explore the replicated image to window titled "Replicated Griaffe"
cv2.imshow("Wrapped Griaffe", wrapped_image) # explore the wrapped image to window titled "Wrapped Griaffe"
cv2.imshow("Constanted Griaffe", constanted_image) # explore the constanted image to window titled "Constanted Griaffe"


cv2.waitKey(0)
cv2.destroyAllWindows()