from PIL import Image

def image_to_array(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale
    image = image.convert('L')

    # Get the image dimensions
    width, height = image.size

    # Initialize a 2D array to store the pixel values
    pixels = [[0 for x in range(width)] for y in range(height)]

    # Iterate over the pixels of the image
    for y in range(height):
        for x in range(width):
            # Get the pixel value (0-255)
            pixel_value = image.getpixel((x, y))

            # Convert the pixel value to 0 or 1
            if pixel_value == 255:
                pixels[y][x] = 1
            else:
                pixels[y][x] = 0

    # Return the 2D array of pixel values
    return pixels
