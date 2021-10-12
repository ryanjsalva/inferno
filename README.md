# 🔥 Inferno

This simple app shows how a Python developer can get started using GitHub Codespaces and Copilot. This demo will:

1. Extract text from an image
2. Translate from Italian to English
3. Juxtapose the image and text

## 🗺 Take a tour
A few things to notice about the app:

1. `.devcontainer.json` defines a custom devcontainer with:
    * Language dependencies (Python 3, Node LTS)
    * GitHub Copilot extension pre-installed
    * `postcreatecommand` to write credentials from the `$INFERNO` secret to a temporary file
2. `dockerfile` installs
    * Package dependencies (pytesseract, google-cloud-translate)
    * Environment variable for the Google Cloud service account
3. `dante.png` shows the first page of Dante's Inferno in the original Italian 
4. `demo.py` shows a completed version of the demo for reference, but you'll create your own file, inferno.py

## ✋ Pre-requisites
Before running this app, you'll need to:

1. Create a [Google Cloud service key in JSON format.](https://cloud.google.com/docs/authentication/production#cloud-console)
2. Visit **Settings > Codespaces > Secrets > Create Secret** to create an `$INFERNO` secret with your Google Cloud service key.

## 🪜 Demo Steps

1. Fork this repository into a GitHub Team or Enterprise account (required for Codespaces)
2. Create a new Codespace by clicking **Code > Create Codespace**
3. Once the code editor is open, create a new file in the root directory called `inferno.py`
4. In the editor, type the following code:
```
# import the image libraries
from PIL import Image, ImageDraw
# convert image to text
import pytesseract
#  Google Cloud Translate package
from google.cloud import translate_v2
```

5. For the next several steps, try typing only the function name and see what happens. Try adding comments to see how it changes the suggestions. GitHub Copilot should be able to write the application for you with very little effort.

6. Use pytesseract to read text from the original image
```
def get_text(image) :
    """ convert the image to text in Italian """
```

7. Use Google Cloud Translate to translate the text to English
```
def translate_text(text) :
    """ translate italian to english """
```

8. Juxtapose the original image and translated text side-by-side
```
def juxtapose(image,text) :
    """create a new image with the original image on the left and the text on the right
    Make the new image twice the width of the original, but the same height.
    Display the text in white on a black background"""
```

9. Bring it all together
```
def process(image) :
    """ process the image """
```

10. Try it out on a test image
```
# try it out on dante.png
image = Image.open('dante.png')
new_image = process(image)

# save the image
new_image.save('dante_translated.png')

```

11. Run your app in the terminal by typing `python inferno.py`
12. Look for `dante_translated.png` in the root directory

Credit: @oegerikus for the original idea, @dynamicwebpaige for pairing with me