import cv2
import numpy as np
import pyvirtualcam


def resized(frame):
    resized = cv2.resize(frame, perspective_size)
    return resized


def get_perspective_size(size):
    re = (int)(size / 2)  # resize input video to square

    ra = 16 / 9  # video's ratio to assure non-distortion
    pw = (int)(re * ra)  # perspective width

    return (pw, re)


def have_same_length(cam1, cam2, cam3, cam4):
    len1 = cam1.get(cv2.CAP_PROP_FRAME_COUNT)
    len2 = cam2.get(cv2.CAP_PROP_FRAME_COUNT)
    len3 = cam3.get(cv2.CAP_PROP_FRAME_COUNT)
    len4 = cam4.get(cv2.CAP_PROP_FRAME_COUNT)

    if (len1 != len2) or (len1 != len3) or (len1 != len4):
        return False
    return True


def cleaning_up():
    cam_front.release()
    cam_back.release()
    cam_right.release()
    cam_left.release()
    cv2.destroyAllWindows()
    # result.release()

    # stop the program
    exit()


perspective_size = get_perspective_size(270)

# # 1. Capture videos from 4 cameras

# # the numbers (0, 1, 2, 3, 4) are variable and represent the camera used
# cam_front = cv2.VideoCapture(0)
# cam_back = cv2.VideoCapture(1)
# cam_right = cv2.VideoCapture(2)
# cam_left = cv2.VideoCapture(3)

### OR

# # 2. Read synchronized video streams showing an object perspectives
cam_front = cv2.VideoCapture('cube_perspectives/front/cube-front.avi')
cam_back = cv2.VideoCapture('cube_perspectives/back/cube-back.avi')
cam_right = cv2.VideoCapture('cube_perspectives/right/cube-right.avi')
cam_left = cv2.VideoCapture('cube_perspectives/left/cube-left.avi')
#
# cam_front = cv2.VideoCapture('videos/Nigel.mp4')
# cam_back = cv2.VideoCapture('videos/Nigel.mp4')
# cam_right = cv2.VideoCapture('videos/Nigel.mp4')
# cam_left = cv2.VideoCapture('videos/Nigel.mp4')

# check streams for length
if not have_same_length(cam_front, cam_back, cam_right, cam_left):
    print('Videos uploaded do not have the same length')
    print('Please try again')
    cleaning_up()

# w - width of a resized perspective
# h - height of a resized perspective
w, h = perspective_size

# final video size
final_size = w + h + h

# resulting video
fps = 24
result = cv2.VideoWriter('Nigel.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (final_size, final_size))

with pyvirtualcam.Camera(width=final_size, height=final_size, fps=60) as cam:
    while (cam_front.isOpened()):
        ret_front, front = cam_front.read()
        ret_back, back = cam_back.read()
        ret_right, right = cam_right.read()
        ret_left, left = cam_left.read()

        try:
            # modify perspectives
            final_front = resized(front)
            final_back = resized(back)
            final_right = resized(right)
            final_left = resized(left)
        except cv2.error:
            # the camera is still open but no frames are coming
            break

        # # display any perspective
        # cv2.imshow('front', final_front)
        # cv2.imshow('back', final_back)
        # cv2.imshow('right', final_right)
        # cv2.imshow('left', final_left)

        # create a black background
        output = np.zeros((final_size, final_size, 3), dtype="uint8")

        # top img
        output[0: h, h: h + w] = final_front
        # left img (rotated 90°)
        output[h: h + w, 0: h] = np.rot90(final_left, 1)
        # right img (rotated 270°)
        output[h: h + w, h + w: h + w + h] = np.rot90(final_right, 3)
        # bottom img (rotated 180°)
        output[h + w: h + w + h, h: h + w] = np.rot90(final_back, 2)

        # # When we use 4 cameras to capture videos, we assume the object has a green screen behind it.
        # # Therefore, we need to replace those pixels with black. Uncomment this section when using cameras
        # output[np.all(output == (0, 255, 0), axis=-1)] = (0, 0, 0)

        # # 3 OPTIONS:
        # 1. display output
        # cv2.imshow('pyramid', output)

        # 2. send output to virtual camera
        cam.send(output)
        cam.sleep_until_next_frame()

        # # 3. write it to file
        result.write(output)

        # press Q to end the streaming
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cleaning_up()
