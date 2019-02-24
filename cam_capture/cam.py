import cv2
import time
import os


DIRNAME = "imgs_standalone"
if not os.path.exists(DIRNAME):
    os.makedirs(DIRNAME)

cam = cv2.VideoCapture(1)

cv2.namedWindow("standalone")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("camera", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "standalone_{}.png".format(int(time.time()))
        cv2.imwrite(os.path.join(DIRNAME, img_name), frame)
        print("{} Standalone!".format(os.path.join(DIRNAME, img_name)))
        img_counter += 1



cam.release()

cv2.destroyAllWindows()
