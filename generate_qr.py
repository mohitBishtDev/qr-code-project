# Step 1: Import the tools
import pyqrcode
import png

# Step 2: Create the QR code
# This is the link or text you want to turn into a QR code
link = "https://medium.com/p/12743ca0a9d9/edit"

# Step 3: Generate the QR code
qr_code = pyqrcode.create(link)

# Step 4: Save the QR code as an image
qr_code.png("my_qr_code.png", scale=6)  # Saves as "my_qr_code.png"
print("QR code generated and saved as 'my_qr_code.png'!")