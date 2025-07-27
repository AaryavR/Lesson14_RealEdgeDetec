import cv2
import numpy as np

def apply_filter(image, filter_type):
    """Apply the selected color filter or edge detection."""
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 0] = 0  # Green channel to 0
        filtered_image[:, :, 1] = 0  # Blue channel to 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Green channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
    elif filter_type == "black_white":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filtered_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    elif filter_type == "pink":
        filtered_image[:, :, 0] = 255  # Blue channel max
        filtered_image[:, :, 1] = 0    # Green channel 0
        filtered_image[:, :, 2] = 255  # Red channel max
    elif filter_type == "canny":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 50, 150)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    else:
        print("Invalid key! Please use 'r', 'g', 'b', 'c', or '.',")
        return None
    cv2.destroyAllWindows()