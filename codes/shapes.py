import cv2
import numpy as np
from pymongo import MongoClient

# Replace <username>, <password>, and <dbname> with your MongoDB Atlas credentials and database name
client = MongoClient('mongodb+srv://yashgupta514:2fXMnsw2h9InLGI1@bruteforce.wqf9kmc.mongodb.net/')
# Connect to your database
db = client['bruteforce']

# Connect to your collection
collection = db['bruteforce']

# The output you want to store

def detect_shapes(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Grayscale Image", gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # cv2.imshow("Blurred Image", blurred)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # Perform edge detection
    edged = cv2.Canny(blurred, 50, 150)
    # cv2.imshow("Edged Image", edged)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # Find contours in the edged image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(f"Found {len(contours)} contours.")
    
    shapes = []
    
    for contour in contours:
        # Get the approximate polygons for the contour
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        # print(f"Approximated contour with {len(approx)} vertices.")
        
        shape_name = "Unknown"
        
        # Identify shape based on the number of vertices
        if len(approx) == 3:
            shape_name = "Triangle"
        elif len(approx) == 4:
            # Calculate aspect ratio to distinguish between square and rectangle
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            if 0.75 <= aspect_ratio <= 1.35:
                shape_name = "Square"
            else:
                shape_name = "Rectangle"
        elif len(approx) > 4:
            # Assuming the shape is a circle if the number of vertices is more than 4
            shape_name = "Circle"


# Insert the output into the collection
        collection.insert_one({"output": shape_name})

        # print("Output stored in MongoDB Atlas")

        # Get the centroid of the shape
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        
        shapes.append((shape_name, (cX, cY)))
        
    
    return shapes

# Load an example image
image = cv2.imread('drawing.png')
# if image is not None:
#     print("")
#     # print("Image loaded successfully.")
# else:
#     print("")
    # print("Failed to load image.")
    
# Detect shapes in the image
detected_shapes = detect_shapes(image)
# Print the output
# for shape, center in detected_shapes:
#     # print(f"Shape: {shape}, Center: {center}")
#     print("")