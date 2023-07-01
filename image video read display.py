import cv2
print("package imported")
#------ to read and display image ------
# img = cv2.imread("resources/300980.jpg")
# cv2.imshow("output", img)
# cv2.waitKey(1000)

#------ to read video -------
# cap = cv2.VideoCapture("resources/Rec 0001.mp4")

#------- to capture video from cam ----------
cap = cv2.VideoCapture(1)
cap.set(10, 100) # to set brightness

#-------- to display video from file or camera -----
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
