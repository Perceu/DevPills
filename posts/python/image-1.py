"""
Criando sua primeira imagem com pillow

pip install Pillow

"""
from PIL import Image, ImageDraw, ImageFont

FONT_COLOR = '#ffffff'
FONT_BACKGROUND = '#000000'
FONT_PATH = './statics/FiraCode.ttf'
POSITION = (50, 250)

# Declarando a fonte
font = ImageFont.truetype(FONT_PATH, 50)
final_image = Image.new('RGBA', (600, 600), FONT_COLOR)

# Declarando a classe de desenho e 
# escrevendo um texto
draw = ImageDraw.Draw(final_image)
draw.text(
        POSITION, 
        'Hello World!', 
        font=font, 
        fill=FONT_BACKGROUND
)

final_image.save(f"primeira_imagen.png")