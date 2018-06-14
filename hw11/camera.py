import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    res, frame = cam.read()

    csv.imshow('Video streaming', frame)
    if csv.waitKey(1) & 0xFF == ord('q'):
        break

print('Close streaming')
cam.release()
cv2.destroyAllWindows()
