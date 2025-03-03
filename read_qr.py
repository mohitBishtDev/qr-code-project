# Step 1: Import the tools
import cv2

# Step 2: Load the QR code image
image = cv2.imread("my_qr_code.png")

# Step 3: Use OpenCV to detect and read the QR code
detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(image)

# Step 4: Check if the QR code was found
if bbox is not None:
    print("QR Code Data:", data)  # Print the data inside the QR code

    # Convert bbox coordinates to integers
    bbox = bbox.astype(int)

    # Draw a blue box around the QR code
    for i in range(len(bbox)):
        point1 = tuple(bbox[i][0])  # Get the first point
        point2 = tuple(bbox[(i + 1) % len(bbox)][0])  # Get the next point (wraps around)
        cv2.line(image, point1, point2, color=(255, 0, 0), thickness=2)

    # Show the image with the blue box
    cv2.imshow("QR Code", image)
    cv2.waitKey(0)  # Wait until you press a key
    cv2.destroyAllWindows()
else:
    print("No QR code found in the image.")