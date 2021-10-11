# import the image libraries
from PIL import Image, ImageDraw
# convert image to text
import pytesseract
#  Google Cloud Translate package
from google.cloud import translate_v2

def get_text(image) :
    """ convert the image to text in Italian """
    # convert image to text
    text = pytesseract.image_to_string(image, lang='ita')

    # remove newlines
    text = text.replace('\n', ' ')

    # remove extra spaces
    text = ' '.join(text.split())

    return text

def translate_text(text) : 
    """ translate italian to english """
    # translate text
    translate_client = translate_v2.Client()
    translation = translate_client.translate(text, target_language='en')
    return translation['translatedText']

# unit test for translate_text(text)
def test_translate_text() :
    """ test the translation function """
    text = 'ciao'
    translation = translate_text(text)
    assert translation == 'hello'

def juxtapose(image,text) :
    """create a new image with the original image on the left and the text on the right
    Make the new image twice the width of the original, but the same height.
    Display the text in white on a black background"""
    # create a new image twice the width of the original, but the same height
    new_image = Image.new('RGB', (image.width * 2, image.height), 'black')

    # paste the original image on the left
    new_image.paste(image, (0, 0))

    # get a font
#    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)

    # get a drawing context
    draw = ImageDraw.Draw(new_image)

    # draw the text
    draw.text((image.width+30, 0), text, fill='white')

    return new_image

def process(image) :
    """ process the image """
    # convert image to text
    text = get_text(image)

    # translate italian to english
    text = translate_text(text)

    import textwrap
    # wrap the text
    text = textwrap.fill(text, width=40)

    # juxtapose the image with the text
    new_image = juxtapose(image, text)

    return new_image

# try it out on a test image
image = Image.open('dante.png')
new_image = process(image)

# save the image
new_image.save('dante_translated.png')
