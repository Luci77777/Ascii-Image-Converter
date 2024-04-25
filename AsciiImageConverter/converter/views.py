from django.shortcuts import render
from .utils import image_to_ascii

def convert_image(request):
    if request.method == 'POST':
        # Get the uploaded image file from the request
        image_file = request.FILES.get('image')

        # Convert the image to ASCII art
        ascii_art = image_to_ascii(image_file)

        # Render the result
        return render(request, 'result.html', {'ascii_art': ascii_art})

    return render(request, 'convert.html')
