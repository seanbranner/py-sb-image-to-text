from PIL import Image, ImageEnhance, ImageOps, ImageGrab, ImageStat
from pathlib import Path
import pytesseract
import pyautogui

project_dir = Path(__file__).parents[1]
package_dir = project_dir.joinpath('py_sb_image_to_text')
resource_dir = project_dir.joinpath('resources')

pytesseract.pytesseract.tesseract_cmd = r"D:\Documents\Projects\Python\py-sb-image-to-text\py_sb_image_to_text\resources\Tesseract-OCR\tesseract.exe"


class CaptureImage:

    def __init__(self):
        sample = None


    def get_energy(self):
        im = pyautogui.screenshot(region=(600, 35, 120, 40))
        return True

    def get_tokens(self):
        return ImageGrab.grab(bbox=(820, 40, 900, 80), all_screens=True)