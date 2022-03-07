import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py_sb_image_to_text',
    version='0.0.1',
    author='Sean Branner',
    author_email='seanbranner@gmail.com',
    description='Custom tool for recognizing images and saving text.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://stash.us.dominos.com/scm/~brannes/py-dpz-stash-tools',
    project_urls = {
        "Bug Tracker": "https://stash.us.dominos.com/scm/~brannes/py-sb-image-to-text/issues"
    },
    license='MIT',
    packages=['py_sb_image_to_text'],
    install_requires=[
        'Pillow',
        'pytesseract',
        'imagesearch',
        'pyautogui',
        'numpy',
    ],
)