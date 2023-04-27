import os
import sys

from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

LOAD_TRUNCATED_IMAGES = True

# Configurações da imagem
IMAGE_WIDTH = 1080
IMAGE_HEIGHT = 1080
FONT_SIZE = 30
FONT_TITLE = 50
PADDING = 50

font = ImageFont.truetype('statics/FiraCode.ttf', FONT_SIZE)
font_title = ImageFont.truetype('statics/FiraCode.ttf', FONT_TITLE)

powered_by = Image.open('statics/powered.png').convert('RGBA')
lang_logo = Image.open('statics/python.png').convert('RGBA')

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

# Configurações do código
CODE = []
post = sys.argv[1]
with open(f'posts/{post}.py', 'r') as f:
    CODE = f.readlines()

CODE.append(' ')

if len(CODE)<=0 and len(CODE)>30:
    raise Exception('seu algoritmo deve conter até 30 linhas')

# Configurações do Pygments
formatter = ImageFormatter(style="dracula", line_number_bg='#282a36', font='Fira Code', font_size=FONT_SIZE)

# Destino da imagem final
image_dest = f'build/{post}.png'
image_cape_dest = f'build/capa_{post}.png'

# Gerar imagem com o trecho de código
code = highlight(''.join(CODE), PythonLexer(), formatter)
with open('build/codigo.png', 'wb') as f:
    f.write(code)

# Redimensionar imagem
img = Image.open('build/codigo.png')



# Redimensionar a imagem para caber nas dimensões desejadas
img_width, img_height = img.size
if img_width > IMAGE_WIDTH - PADDING * 2:
    ratio = (IMAGE_WIDTH - PADDING * 2) / img_width
    img_width = int(img_width * ratio)
    img_height = int(img_height * ratio)

if img_height > IMAGE_HEIGHT - PADDING * 2:
    ratio = (IMAGE_HEIGHT - PADDING * 2) / img_height
    img_width = int(img_width * ratio)
    img_height = int(img_height * ratio)

img = img.resize((img_width, img_height))

# Criar imagem final com bordas em estilo polaroid
final_image = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT), (0, 0, 0, 255))
draw = ImageDraw.Draw(final_image)
draw.rounded_rectangle((PADDING - 25, PADDING - 25, IMAGE_WIDTH - PADDING + 25, IMAGE_HEIGHT - PADDING + 25), radius=10, fill='white', outline='#ccc', width=3)
draw.rounded_rectangle((PADDING, PADDING, IMAGE_WIDTH - PADDING, IMAGE_HEIGHT - PADDING - 100), radius=10, fill='#282a36', outline='#F0F0F0', width=5)
draw.text((PADDING+10, IMAGE_HEIGHT - PADDING - 100), "@perceubertoletti.dev", font=font, fill=(100, 100, 100))
final_image.paste(powered_by, (IMAGE_WIDTH - PADDING - 180, IMAGE_HEIGHT - PADDING - 90), powered_by)

cape = final_image.copy()

final_image.paste(img, (PADDING+5, PADDING+5))

draw.rounded_rectangle((PADDING, PADDING, IMAGE_WIDTH - PADDING, IMAGE_HEIGHT - PADDING - 100), radius=10, outline='#F0F0F0', width=5)


draw_cape = ImageDraw.Draw(cape)
draw_cape.text((PADDING+25, PADDING+25), "Code Snippet", font=font, fill=(200, 200, 200))

text_width, text_height = get_text_dimensions(post, font_title)
draw_cape.text(((IMAGE_WIDTH-text_width)//2, int(IMAGE_HEIGHT/2)+100), post.title(), font=font_title, fill=(200, 200, 200))

width_logo, height_logo = lang_logo.size
cape.paste(lang_logo, (int(IMAGE_WIDTH/2)-int(width_logo/2), int(IMAGE_HEIGHT/2)-200), lang_logo)

cape.save(image_cape_dest)
final_image.save(image_dest)