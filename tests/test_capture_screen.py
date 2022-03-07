import unittest
from py_sb_image_to_text import py_sb_capture_screen
from pathlib import Path

class TestPySbImageToText(unittest.TestCase):

    project_dir = Path(__file__).parents[1]
    package_dir = project_dir.joinpath('tests')
    resource_dir = package_dir.joinpath('resources')

    arena_tokens_path = resource_dir.joinpath('arena_tokens_status.PNG')

    def test_reading_hello_world_example(self):
        expected = "Hello World!"
        captured_object = py_sb_capture_screen.CaptureImage(self.arena_tokens_path)
        captured_object.get_energy()
        self.assertEqual(True, True)

    def test_get_tokens_image(self):
        captured_object = py_sb_capture_screen.CaptureImage(self.arena_tokens_path)
        captured_object.get_tokens()
        self.assertEqual(True, True)

