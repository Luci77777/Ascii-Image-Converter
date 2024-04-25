from PIL import Image, ImageOps

def image_to_ascii(image_file, width=100, rotation_angle=0):
    # Open the uploaded image
    img = Image.open(image_file)
    
    # Rotate the image
    img = img.rotate(rotation_angle, expand=True)

    # Resize the image to reduce processing time and maintain aspect ratio
    aspect_ratio = img.height / img.width
    new_width = width
    new_height = int(new_width * aspect_ratio)
    img = img.resize((new_width, new_height))

    # Convert the image to grayscale
    img = img.convert('L')

    # Define ASCII characters to represent pixel intensity
    ascii_chars = '@%#*+=-:. '

    # Define intervals for pixel intensity and corresponding ASCII characters
    interval_size = 256 // len(ascii_chars)
    intervals = [(i * interval_size, (i + 1) * interval_size - 1) for i in range(len(ascii_chars))]

    # Convert each pixel to ASCII character and insert line breaks
    ascii_art = ''
    for y in range(new_height):
        for x in range(new_width):
            pixel_value = img.getpixel((x, y))
            for i, (lower, upper) in enumerate(intervals):
                if lower <= pixel_value <= upper:
                    ascii_art += ascii_chars[i]
                    break
            else:
                ascii_art += ascii_chars[-1]  # Use the last character for out-of-range values
        ascii_art += '\n'

    return ascii_art
