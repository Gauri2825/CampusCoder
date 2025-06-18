import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Replace with the actual path to your background image
BG_IMAGE = get_base64_image("assets/image.jpg")


