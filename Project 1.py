import cv2
import numpy as np

def resize_image(input_image_path, output_image_path, new_width, new_height):
    original_image = cv2.imread(input_image_path)
    resized_image = cv2.resize(original_image, (new_width, new_height))
    cv2.imwrite(output_image_path, resized_image)
    print("Image resized")

def rotate_image(input_image_path, output_image_path, angle):
    original_image = cv2.imread(input_image_path)
    height, width = original_image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))
    cv2.imwrite(output_image_path, rotated_image)
    print(f"Image rotated by {angle} degrees")

def color_filter(input_image_path, output_image_path, lower_color, upper_color):
    original_image = cv2.imread(input_image_path)
    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

    lower_color = np.array(lower_color, dtype=np.uint8)
    upper_color = np.array(upper_color, dtype=np.uint8)

    color_mask = cv2.inRange(hsv_image, lower_color, upper_color)
    filtered_image = cv2.bitwise_and(original_image, original_image, mask=color_mask)
    cv2.imwrite(output_image_path, filtered_image)
    print("Image filtered")


input_image_path = input("Enter the path to the input image: ")

# Resize
resized_image_path = "resized_image.jpg"
new_width = int(input("Enter the new width: "))
new_height = int(input("Enter the new height: "))
resize_image(input_image_path, resized_image_path, new_width, new_height)

# Rotate
rotated_image_path = "rotated_image.jpg"
rotation_angle = float(input("Enter the rotation angle in degrees: "))
rotate_image(resized_image_path, rotated_image_path, rotation_angle)

# Color filter
color_output_path = "filtered_image.jpg"
lower_hue = int(input("Enter the lower hue value (0-179): "))
upper_hue = int(input("Enter the upper hue value (0-179): "))
lower_saturation = int(input("Enter the lower saturation value (0-255): "))
upper_saturation = int(input("Enter the upper saturation value (0-255): "))
lower_value = int(input("Enter the lower value/brightness value (0-255): "))
upper_value = int(input("Enter the upper value/brightness value (0-255): "))
lower_color = (lower_hue, lower_saturation, lower_value)
upper_color = (upper_hue, upper_saturation, upper_value)
color_filter(rotated_image_path, color_output_path, lower_color, upper_color)

# Display the final output
output1 = cv2.imread(resized_image_path)
cv2.imshow("Output1", output1)
output2 = cv2.imread(rotated_image_path)
cv2.imshow("Output2", output2)
output3 = cv2.imread(color_output_path)
cv2.imshow("Output3", output3)
cv2.waitKey(0)
cv2.destroyAllWindows()





