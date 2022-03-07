from PIL import Image, ImageEnhance, ImageOps, ImageGrab, ImageStat
from pathlib import Path
import pytesseract
import pyautogui
import subprocess

project_dir = Path(__file__).parents[1]
package_dir = project_dir.joinpath('py_sb_image_to_text')
resource_dir = project_dir.joinpath('resources')

# pytesseract.pytesseract.tesseract_cmd = r"D:\Documents\Projects\Python\py-sb-image-to-text\py_sb_image_to_text\resources\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# def run_windows_cmd(self, cmd):
#     # import subprocess
#     # proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
#     # (out, err) = proc.communicate()
#     # print "program output:", out
#     #
#     # print(p)
#     ###### original working way
#     # return os.popen(f'cmd /c {powershell_path} "{cmd}"').read()
#     # running_command = subprocess.call(f'cmd /c "{cmd}"')
#     ###### newest way
#
#     cmd_as_list = cmd.split(' ')
#     running_command = subprocess.check_output(
#         cmd_as_list,
#         text=True,
#     )
#     return running_command
#
# def run_powershell_cmd(cmd):
#     powershell_path = "powershell"  # Path("C:\Windows\System32\WindowsPowerShell").joinpath("v1.0\powershell.exe")
#     return run_windows_cmd(f'{powershell_path} {cmd}')
#
# def is_multi_screen():
#     cmd = "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }"
#     list_of_ip_address_and_macs = run_powershell_cmd(cmd).split('\n')
#     number_of_connected_devices = len(list_of_ip_address_and_macs)
#
#     if number_of_connected_devices > 15:
#         return True
#     else:
#         return False

class CaptureImage:

    def __init__(self,):
        sample = None
        # multi_screen = is_multi_screen()

    def get_tokens(self):
        img = ImageGrab.grab(bbox=(820+1920, 40, 900 + 1920, 80), all_screens=True)
        # img.show()
        return img

    def get_team_tokens(self):
        img = ImageGrab.grab(bbox=(1010 + 1920, 40, 1090 + 1920, 80), all_screens=True)
        return img

    def get_energy(self):
        img = ImageGrab.grab(bbox=(600 + 1920, 40, 730 + 1920, 80), all_screens=True)
        return img

    def get_doom_tower_keys(self):
        img = ImageGrab.grab(bbox=(1340 + 1920, 40, 1460 + 1918, 80), all_screens=True)
        return img

    def get_hydra_clan_boss_keys(self):
        img = ImageGrab.grab(bbox=(1105 + 1920, 40, 1200 + 1930, 80), all_screens=True)
        return img

    def get_demon_lord_clan_boss_keys(self):
        img = ImageGrab.grab(bbox=(1338 + 1920, 40, 1460 + 1918, 80), all_screens=True)
        return img
