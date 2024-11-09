import cv2 as cv #import open cv library for image processing functionality
# Importing functions for circle detection and drawing from the 'circles' module
from circles import detect_circles, draw_circle, xcorSum
# Importing functions for image processing and video frame display from the 'display_image' module
from display_image import process_image, display_video_frame
import time 
import serial 
from reader import feed

ser = serial.Serial('/dev/tty.usbserial-110', 9600)
input("")
def move(instr):
    ser.write(instr.encode())
    time.sleep(0.05)
    ser.write('S'.encode())
    time.sleep(0.3)
    
if __name__ == "__main__":
    # Open the video file for capturing frames
    capture = cv.VideoCapture(0)
    count = 0
    tic = time.perf_counter()
    
    while True:
        frame_exist, img = capture.read()
        if frame_exist:
            gray_img = process_image(img)
            circles = detect_circles(gray_img)
            xcor = xcorSum(circles)
            move('L')
            if xcor > 0:
                count+=1
            else:
                count = 0
            if count >= 8:
                break
            img_with_circle = draw_circle(img.copy(), circles)
            display_video_frame(img_with_circle, "Video with Circles")    
    # Loop to process and display each frame of the video
    count = 0
    while True:
        # Read the next frame from the video
        frame_exist, img = capture.read()

        # Check if the frame was successfully read
        if frame_exist:
            # Process the frame to grayscale
            gray_img = process_image(img)

            # Detect circles in the processed grayscale frame
            circles = detect_circles(gray_img)
            xcor = xcorSum(circles)
            if xcor == 0:
                count+=1
            elif xcor < 850:
                move('L')
                count = 0
            elif xcor > 950:
                move('R')
                count = 0
            else:
                move('F')
                count = 0               
            # Draw circles on the original frame
            img_with_circles = draw_circle(img.copy(), circles)
            if count == 5 or count == 15 or count == 25 or count == 35 or count == 45 or count== 47 or count == 48 or count == 49:
                move('F')
            if count >= 50 or time.perf_counter() - tic > 115:
                ser.write('B'.encode())
                time.sleep(10)
                ser.write('S'.encode())
                break
            # Display the original frame with circles
            display_video_frame(img_with_circles, "Video with Circles")
            if cv.waitKey(1) == ord('q'):
                move('S') 
                break
        else:
            # Break the loop if no more frames are available
            break

    # Release the video capture object
    
    capture.release()
    ser.close()
    # Close all OpenCV windows
    cv.destroyAllWindows()
