import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    res, frame = cam.read()

    cv2.imshow('Video streaming', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print('Close streaming')
cam.release()
cv2.destroyAllWindows()
