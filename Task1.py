import cv2
image = cv2.imread("istockphoto-1072769156-612x612.jpg")
cv2.imshow("My", image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New My", gray_image)
cv2.waitKey(0)

inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

blurred = cv2.GaussianBlur(inverted_image,(21,21),0)

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=130.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
 # filename = "Saved.jpg"     # for saving sketch photo in storage
 # cv2.imwrite(filename, pencil_sketch)