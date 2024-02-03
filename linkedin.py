import segno
from PIL import Image, ImageDraw, ImageFont
qrcode = segno.make_qr("https://www.linkedin.com/in/farhansadeekde110/").save('linkedin.png', scale = 10, border = 5, dark = 'darkred')


# Open the generated QR code image
image = Image.open("linkedin.png")
draw = ImageDraw.Draw(image)

# Define the text to be written
text = "Linkedin"
font = ImageFont.truetype("arial.ttf", 35)  # You may need to change the font and size

# Calculate the size of the text
text_width, text_height = draw.textsize(text, font)

# Calculate the position to place the text at the bottom center
image_width, image_height = image.size

# Define border sizes
top_border = 0
bottom_border = 50  # Adjust this value to increase or decrease the bottom border
side_border = 0

# Create a new image with extended bottom border
new_image = Image.new("RGB", (image_width, image_height + bottom_border), color="white")
new_image.paste(image, (0, 0))

# Draw the text on the new image
draw = ImageDraw.Draw(new_image)
text_position = ((image_width - text_width) // 2, image_height + bottom_border - text_height - 20)  # Adjust 10 for padding
draw.text(text_position, text, font=font, fill="black")

# Save the modified image
new_image.save("linkedin.png")
