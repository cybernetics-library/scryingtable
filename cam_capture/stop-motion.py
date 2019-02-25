import time
import cv2
import os


DIRNAME = "imgs_stopmotion"
if not os.path.exists(DIRNAME):
    os.makedirs(DIRNAME)

SECONDS_PER_TICK = 30.0

starttime=time.time()

cam = cv2.VideoCapture(1)

cam.set(3,1920)

cam.set(4,1080)

cv2.namedWindow("stopmotion")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("stopmotion", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    print("tick")
    img_name = "stop_motion_{}.png".format(int(time.time()))
    cv2.imwrite(os.path.join(DIRNAME, img_name), frame)
    print("{} Stop motion!".format(os.path.join(DIRNAME, img_name)))
    img_counter += 1
    time.sleep(SECONDS_PER_TICK - ((time.time() - starttime) % SECONDS_PER_TICK))

cam.release()

cv2.destroyAllWindows()
