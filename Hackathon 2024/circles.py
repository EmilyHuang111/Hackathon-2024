import cv2 as cv
import numpy as np

# Function to detect circles in a processed image
def detect_circles(processed_img):
    # Get the number of rows in the processed image
    rows = processed_img.shape[0]

    # Use HoughCircles to detect circles in the processed image
    circles = cv.HoughCircles(processed_img, cv.HOUGH_GRADIENT,
                              dp=1, minDist=rows / 8,
                              param1=20, param2=35,
                              minRadius=260, maxRadius=280)
    return circles

def xcorSum(circles):
    xcor = 0
    tt = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            tt+=1
            xcor += circle[0]
    else:
        return 0
    return xcor/tt
            
# Function to draw circles on an input image
def draw_circle(img, circles):
    # Check if any circles are detected
    if circles is not None:
        # Convert circle coordinates to integer
        circles = np.uint16(np.around(circles))

        # Loop through detected circles
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            print(str(circle[0]) + " " + str(circle[1]))
            # Draw a small dot at the center of the circle
            cv.circle(img, center, 1, (0, 0, 255), 10)

            # Draw the circle outline
            radius = circle[2]
            cv.circle(img, center, radius, (0, 255, 0), 10)

        return img  # Return the image with drawn circles
    else:
        return img  # Return the original image if no circles are detected
