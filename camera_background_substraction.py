import cv2
import numpy as np

# capture video
# pass 0 for the default camera, 1 for another one
capture = cv2.VideoCapture(0)
backsub = cv2.createBackgroundSubtractorMOG2()

width = capture.get(3)  # float
height = capture.get(4)  # float

# describe a loop
# read video frame by frame
while True:
    ret, img1 = capture.read()
    cv2.imshow('Original Video', img1)

    # Convert to the HSV color space
    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

    # Create a mask based on medium to high Saturation and Value
    # - These values can be changed (the lower ones) to fit your environment
    mask = cv2.inRange(hsv, (0, 75, 40), (180, 255, 255))

    # mask = backsub.apply(img1, )

    # We need a to copy the mask 3 times to fit the frames
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2)

    # Create black background
    #black_bgr = np.zeros((int(height), int(width), 3), dtype="uint8")

    # if the pixels are white, use the captured video, otherwise use the mask
    #frame = np.where(mask_3d == (255, 255, 255), img1, black_bgr)


    cv2.imshow('Foreground mask', mask_3d)

    k = cv2.waitKey(30) & 0xff
    # once you inter Esc capturing will stop
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
