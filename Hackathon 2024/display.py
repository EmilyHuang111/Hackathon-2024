import cv2 as cv #import open cv for image processing functionality

# Function to process an input image
def process_image(img):
    # Convert the image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Apply a blur to the grayscale image
    gray = cv.blur(gray, (1, 1))
    # Apply a median blur to the grayscale image
    gray = cv.medianBlur(gray, 1)
    return gray

# Function to display an image in a window
def display_image(img, windowName):
    # Show the image in a window with the specified name
    cv.imshow(windowName, img)
    # Wait for a key press and continue
    cv.waitKey(1)

# Function to display a video frame in a window
def display_video_frame(frame, windowName):
    # Show the video frame in a window with the specified name
    cv.imshow(windowName, frame)
    # Wait for a key press and continue
    cv.waitKey(1)
