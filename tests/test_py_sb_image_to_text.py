import unittest
from py_sb_image_to_text import py_sb_image_to_text,py_sb_capture_screen
from pathlib import Path

class TestPySbImageToText(unittest.TestCase):

    project_dir = Path(__file__).parents[1]
    package_dir = project_dir.joinpath('tests')
    resource_dir = package_dir.joinpath('resources')
    example_hello_world_img_path = resource_dir.joinpath("example_hello_world.PNG")
    example_bastion_arena_tokens_img_path = resource_dir.joinpath("example_bastion_arena_tokens.PNG")
    example_campaign_energy_img_path = resource_dir.joinpath("example_campaign_energy.PNG")

    def test_reading_hello_world_example(self):
        expected = "Hello World!"

        example_hello_world_img_object = py_sb_image_to_text.TextImage(self.example_hello_world_img_path)
        actual = example_hello_world_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_reading_arena_tokens(self):
        expected = "10/10"

        example_arena_tokens_img_object = py_sb_image_to_text.TextImage(self.example_bastion_arena_tokens_img_path)
        actual = example_arena_tokens_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_campaign_energy(self):
        expected = "334/130"

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_arena_tokens_real(self):
        expected = "4/10"

        image_object = py_sb_capture_screen.CaptureImage()
        taoken_image = image_object.get_tokens()

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        example_campaign_energy_img_object.set_image_object(taoken_image)

        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)
