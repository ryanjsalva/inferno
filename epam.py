# import the image libraries
from PIL import Image, ImageDraw, ImageFont
# convert image to text
import pytesseract
#  Google Cloud Translate package
from google.cloud import translate_v2

def get_text(image) :
    """ get text from the image """
    # convert image to text
    text = pytesseract.image_to_string(image)
    # print(text)
    return text

def translate_text(text) :
    """ translate from italian to english """
    # translate text
    translate_client = translate_v2.Client()
    translation = translate_client.translate(text, target_language='en')
    # print(translation)
    return translation

def juxtapose(image, text) :
    """ create a new image twice the width of the original and the same height.
    Place the original image on the left and translated text on the right.
    Display the text on a black background with red text using Roboto-Regular.ttf. """
    # create a new image twice the width of the original and the same height
    new_image = Image.new('RGB', (image.width*2, image.height), color = 'black')
    # place the original image on the left
    new_image.paste(image, (0, 0))
    # place the translated text on the right
    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype("Roboto-Regular.ttf", 20)
    draw.text((image.width, 0), text, fill = 'red', font = font)
    return new_image

def process(image) :
    """ process the image """
    # get text from the image
    text = get_text(image)
    # translate the text
    translation = translate_text(text)

    import textwrap
    # wrap the text
    wrapped_text = textwrap.fill(translation['translatedText'], width=40)

    # juxtapose the image and the translated text
    new_image = juxtapose(image, wrapped_text)
    return new_image

# try it with dante.png
image = Image.open('dante.png')
new_image = process(image)

# save the new image
new_image.save('dante_translated.png')