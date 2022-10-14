import cv2

# To read image from disk, we use
# cv2.imread function, in below method,
# TASK 1: img = cv2.imread("geeksforgeeks.png", cv2.IMREAD_COLOR)

	
img = cv2.imread("maxresdefault.jpg", cv2.IMREAD_COLOR)
 




# Drawing some rectangle
cv2.rectangle(img, (10, 10), (100, 100), (255, 0, 0), 3)
cv2.rectangle(img, (120, 120), (150, 150), (255, 0, 0), 5)
cv2.rectangle(img, (200, 300), (962, 457), (255, 0, 0), -1)


# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow('image', img)
 
# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
#       cv2.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
#           cv2.destroyAllWindows()

# To finalize, we will wait for the user to press any key on the keyboard and, when that happens, destroy the window and end the program.

cv2.waitKey(0)
cv2.destroyAllWindows()