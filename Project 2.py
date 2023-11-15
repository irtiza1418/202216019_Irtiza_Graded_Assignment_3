import cv2

# Global variables
drawing = False
ix, iy = -1, -1
fx, fy = -1, -1


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = x, y
        cv2.rectangle(frame, (ix, iy), (fx, fy), (0, 0, 255), 2)
        cv2.imshow('image', frame)


image_path = input("Enter Image Path: ")
frame = cv2.imread(image_path)
cv2.imshow('image', frame)

cv2.setMouseCallback('image', draw_rectangle)

while True:
    key = cv2.waitKey(0) & 0xFF


    if key == ord('c'):  # If 'c' is pressed, crop the selected region
        if ix != -1 and iy != -1 and fx != -1 and fy != -1:
            roi = frame[iy:fy, ix:fx]
            cv2.imshow('cropped', roi)
            cv2.imwrite('C:/Users/Admin/Pictures/cropped_image.jpg', roi)
            print('Image cropped and saved')
            cv2.destroyAllWindows()  # Close all OpenCV windows
            break


    elif key == ord('r'): # If 'r' is pressed, reset the selection
        ix, iy, fx, fy = -1, -1, -1, -1
        frame = cv2.imread(image_path)
        cv2.imshow('image', frame)


    elif key == 27:  # If 'Esc' is pressed, exit
        cv2.destroyAllWindows()
        break

