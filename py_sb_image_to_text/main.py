#currently takes picture snip, inverts it, adds words from picture to array and prints it
import os,sys,datetime,subprocess,time,shutil,inspect
import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui as ptg 
import pytesseract
import xlsxwriter

from PIL import Image, ImageEnhance, ImageOps
pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Python\\Python37-32\\Lib\\site-packages\\Tesseract-OCR\\tesseract'
screenWidth, screenHeight = ptg.size()

#Script detail variables and logging information
scriptPath = inspect.getfile(inspect.currentframe()) # script filename (usually with path)
scriptDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
arguments = sys.argv

