# 3D Hologram Pyramid Rendering
####by COMP0016_2020_21_Team3

###

### Opening this project:
- if you open this project in PyCharm, you will have no problem with dependencies and the program is ready to run.
- if you choose to run this program by terminal, follow the steps:
 
        # create virtual environment
        virtualenv .venv 
    
        # enter virtual environment
        source .venv/bin/activate
    
        # install required packages
        pip install -r requirements.txt
    

### Usage:

####This program has 2 input options:

**warning:** there should always be only 1 option uncommented at any time

1. Use 4 cameras from different perspectives:
    - uncomment this section and comment the second one
    - *cv2.VideoCapture(0)* method takes an integer number as an argument. That number represents the camera index that can be found as follows:
      - camera_id + domain_offset (CAP_*) id of the video capturing device to open. To open default camera using default backend just pass 0.(https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a5d5f5dacb77bbebdcbfb341e3d4355c1)
    - input the camera index accordingly to the variable name: e.g., for *cam_front* use the camera that captures from front
    - uncomment the part that changes the green screen to black pixels
    
2. Use 4 videos:
    - make sure that the videos used are synchronized and have the same length
    - uncomment this section and comment the first one
    - *cv2.VideoCapture('cube_perspectives/front/cube-front.avi')* method also takes a path as an argument. Make sure to match the perspective with the variable name.
    
####Following, this program has further 3 output options:

*Note: in this case it doesn't matter how many options are uncommented*

1. Save the video to a .avi file. To use it, uncomment the lines containing the **result** variable - e.g.:
   
        result.release() # found in cleaning_up() method

2. Display the video in a different window by uncommenting this line:

        cv2.imshow('pyramid', output)

3. Send the video to a virtual camera by uncommenting:

        cam.send(output)
        cam.sleep_until_next_frame()
    - this will send the video stream to a client such as OBS(this is the one we used, but any virtual camera should work)
    - Use OBS to create a Video source and select *OBS virtual camera*.
    - run the program and the video should appear in OBS instantly.
    

