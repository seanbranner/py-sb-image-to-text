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

    def __init__(self,multi_screen=False):
        sample = None
        self.multi_screen = multi_screen
        
    def get_adjusted_coordinates(self,coordinate):
        if self.multi_screen:
            return (coordinate[0]+1920,coordinate[1])
        return coordinate

    def get_tokens(self):
        top_left_corner = (823, 40)
        bottom_right_corner = (900, 75)
        img = self.grab_and_return_image(top_left_corner,bottom_right_corner)
        img.show()
        return img

    def grab_and_return_image(self,top_left_coordinate,bottom_right_coordinate):
        top_left_corner = self.get_adjusted_coordinates(top_left_coordinate)
        bottom_right_corner = self.get_adjusted_coordinates(bottom_right_coordinate)
        img = ImageGrab.grab(
            bbox=(
                top_left_corner[0],
                top_left_corner[1],
                bottom_right_corner[0],
                bottom_right_corner[1]
            ),
            all_screens=True
        )
        return img

    def get_team_tokens(self):
        top_left_corner = (1010, 40)
        bottom_right_corner = (1090, 80)
        img = self.grab_and_return_image(top_left_corner,bottom_right_corner)
        return img

    def get_energy(self):
        top_left_corner = (600, 40)
        bottom_right_corner = (730, 80)
        img = self.grab_and_return_image(top_left_corner,bottom_right_corner)
        return img

    def get_doom_tower_keys(self):
        top_left_corner = (1340, 40)
        bottom_right_corner = (1455, 80)
        img = self.grab_and_return_image(top_left_corner,bottom_right_corner)
        img.show()
        return img

    def get_hydra_clan_boss_keys(self):
        top_left_corner = (1105, 40)
        bottom_right_corner = (1200, 80)
        img = self.grab_and_return_image(top_left_corner,bottom_right_corner)
        return img

    def get_demon_lord_clan_boss_keys(self):
        top_left_corner = (1338, 40)
        bottom_right_corner = (1460, 80)
        img = self.grab_and_return_image(top_left_corner,bottom_right_corner)
        return img
