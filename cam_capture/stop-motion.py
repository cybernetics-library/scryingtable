import time
import cv2
starttime=time.time()

cam = cv2.VideoCapture(1)

cv2.namedWindow("stopmotion")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("stopmotion", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    print "tick"
    img_name = "stop_motion_{}.png".format(int(time.time()))
    cv2.imwrite(img_name, frame)
    print("{} Stop motion!".format(img_name))
    img_counter += 1
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

cam.release()

cv2.destroyAllWindows()
