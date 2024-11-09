import cv2 as cv #import open cv library for image processing functionality
# Importing functions for circle detection and drawing from the 'circles' module
from circles import detect_circles, draw_circle, xcorSum
# Importing functions for image processing and video frame display from the 'display_image' module
from display_image import process_image, display_video_frame
import time 
import serial 

if __name__ == "__main__":
    # Open the video file for capturing frame
    cam = cv.VideoCapture(0)
    ser = serial.Serial('/dev/tty.usbserial-1110', 9600)

    # Loop to process and display each frame of the video
    while True:
        # Read the next frame from the video
        frame_exist, img = cam.read()

        # Check if the frame was successfully read
        if frame_exist:
            # Process the frame to grayscale
            gray_img = process_image(img)

            # Detect circles in the processed grayscale frame
            circles = detect_circles(gray_img)
            
            xcor = xcorSum(circles)
            command = 'R'
            if xcor < 1000:
                command = 'L'
            elif xcor < 1400:
                command = 'U'
                ser.write(command.encode())
                distance = int(ser.readline().decode('utf-8')) 
                command = 'S'
                print(distance)
                ser.write(command.encode())
                command = 'F'
                if distance < 16:
                    ser.write(command.encode())
                    time.sleep(2)
                    command = 'S'
                    ser.write(command.encode())
                    command = 'B'
                    ser.write(command.encode())
                    time.sleep(2)
                    command = 'S'
                    ser.write(command.encode())
                    break
            ser.write(command.encode())
            
            time.sleep(0.025) 
            command = "S"
            time.sleep(0.01)
            ser.write(command.encode())    
            # Draw circles on the original frame
            img_with_circles = draw_circle(img.copy(), circles)

            # Display the original frame with circles
            display_video_frame(img_with_circles, "Video with Circles")
            if cv.waitKey(1) == ord('q'):
                command = 'S'
                ser.write(command.encode())
                ser.close()
                break
        else:
            # Break the loop if no more frames are available
            break

    # Release the video capture object
    capture.release()
    # Close all OpenCV windows
    cv.destroyAllWindows()
