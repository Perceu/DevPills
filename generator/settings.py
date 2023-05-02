import os 

class Settings():
    IMAGE_WIDTH = 1080
    IMAGE_HEIGHT = 1080
    SIZE_FONT = 30
    SIZE_FONT_TITLE = 50
    PADDING = 50
    LOAD_TRUNCATED_IMAGES = True
    BASE_PATH = os.getcwd()
    POWERED_BY = f'{BASE_PATH}/statics/powered.png'
    PYTHON_LOGO = f'{BASE_PATH}/statics/python.png'
    FONT_FACE = f'{BASE_PATH}/statics/FiraCode.ttf'
