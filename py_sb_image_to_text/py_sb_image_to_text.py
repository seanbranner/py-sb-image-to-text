from PIL import Image, ImageEnhance, ImageOps, ImageGrab, ImageStat
from pathlib import Path
import pytesseract

project_dir = Path(__file__).parents[1]
package_dir = project_dir.joinpath('py_sb_image_to_text')
resource_dir = project_dir.joinpath('resources')

# pytesseract.pytesseract.tesseract_cmd = r"D:\Documents\Projects\Python\py-sb-image-to-text\py_sb_image_to_text\resources\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class TextImage:

    def __init__(self):
        self.image_text = None
        self.image_path = None
        print(self.image_path)
        self.image_object = None

    def set_image_object(self, image_objext):
        self.image_object = image_objext

    def set_image_path(self, image_path):
        self.set_image_object(Image.open(self.image_path))
        self.image_path = image_path

    def get_image_text(self):
        print('running image to text')
        self.invert_image(self.image_object)
        return pytesseract.image_to_string(self.image_object).strip()

    def invert_image(self, img):
        size = width, height = img.size
        img = ImageOps.invert(img.convert('RGB'))
        # img.show()

        if img.mode == 'RGBA':
            img.load()
            r, g, b, a = img.split()
            img = img.merge('RGB', (r, g, b))
        return img
    #
    # def imgBlackAndWhite(img):
    #     en = ImageEnhance.Color(img)
    #     img = en.enhance(0.0)
    #     return True
