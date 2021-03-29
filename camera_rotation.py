import cv2


# capture video
# pass 0 for the default camera, 1 for another one
cap = cv2.VideoCapture(1)

# describe a loop
# read video frame by frame
while True:
    ret, img1 = cap.read()
    cv2.imshow('Original Video', img1)

    # rotate frames
    img2 = cv2.rotate(img1, rotateCode=cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('Rotated video', img2)

    k = cv2.waitKey(30) & 0xff
    # once you inter Esc capturing will stop
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
