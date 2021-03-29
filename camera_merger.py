import cv2


# capture video
# pass 0 for the default camera, 1 or 2 for another one
cap = cv2.VideoCapture(1)

# describe a loop
# read video frame by frame
while True:
    ret, img1 = cap.read()
    # cv2.imshow('Original Video', img)

    # flip for truning(fliping) frames of video
    img2 = cv2.flip(img1, -1)
    # cv2.imshow('Flipped video', img2)

    # concatenating vertically, one over another
    final = cv2.vconcat([img1, img2])
    cv2.imshow('Merged flipped videos', final)

    # concatenating horizontally, one over another
    # final = cv2.hconcat([img1, img2])

    k = cv2.waitKey(30) & 0xff
    # once you inter Esc capturing will stop
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
