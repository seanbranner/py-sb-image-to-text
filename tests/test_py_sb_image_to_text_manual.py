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

    def test_campaign_energy(self):
        expected = "334/130"

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_arena_tokens_real(self):
        expected = "3/10"

        image_object = py_sb_capture_screen.CaptureImage(multi_screen=False)
        taoken_image = image_object.get_tokens()

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        example_campaign_energy_img_object.set_image_object(taoken_image)

        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_team_arena_tokens_real(self):
        expected = "0/10"

        image_object = py_sb_capture_screen.CaptureImage(multi_screen=True)
        token_object = image_object.get_team_tokens()

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        example_campaign_energy_img_object.set_image_object(token_object)

        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_energy_real(self):
        expected = "42/130"

        image_object = py_sb_capture_screen.CaptureImage(multi_screen=True)
        token_object = image_object.get_energy()

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        example_campaign_energy_img_object.set_image_object(token_object)

        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_doom_tower_keys_real(self):
        expected = "0/10"

        image_object = py_sb_capture_screen.CaptureImage(multi_screen=True)
        token_object = image_object.get_doom_tower_keys()

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        example_campaign_energy_img_object.set_image_object(token_object)

        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_clan_boss_keys(self):
        expected = "0/2"

        image_object = py_sb_capture_screen.CaptureImage(multi_screen=True)
        token_object = image_object.get_demon_lord_clan_boss_keys()

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        example_campaign_energy_img_object.set_image_object(token_object)

        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)

    def test_hybdra_boss_keys(self):
        expected = "3/3"

        image_object = py_sb_capture_screen.CaptureImage(multi_screen=True)
        token_object = image_object.get_hydra_clan_boss_keys()

        example_campaign_energy_img_object = py_sb_image_to_text.TextImage()
        example_campaign_energy_img_object.set_image_object(token_object)

        actual = example_campaign_energy_img_object.get_image_text()
        self.assertEqual(expected, actual)