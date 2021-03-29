import cv2


# capture video
# pass 0 for the default camera, 1 for another one
cap = cv2.VideoCapture(1)

# describe a loop
# read video frame by frame
while True:
    ret, img1 = cap.read()
    cv2.imshow('Original Video', img1)

    # flip for truning(fliping) frames of video
    img2 = cv2.flip(img1, -1)
    cv2.imshow('Flipped video', img2)

    k = cv2.waitKey(30) & 0xff
    # once you inter Esc capturing will stop
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
