import os
import sys

from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

# Configurações da imagem
IMAGE_WIDTH = 1080
IMAGE_HEIGHT = 1080
FONT_SIZE = 30
PADDING = 50


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
image_dest = 'build/codigo.png'

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
final_image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(final_image)


# draw.rounded_rectangle((PADDING - 25, PADDING - 25, IMAGE_WIDTH - PADDING + 25, IMAGE_HEIGHT - PADDING + 50), radius=20, fill='white', outline='white', width=3)
draw.rounded_rectangle((PADDING - 25, PADDING - 25, IMAGE_WIDTH - PADDING + 25, IMAGE_HEIGHT - PADDING + 25), radius=10, fill='white', outline='#ccc', width=3)
draw.rounded_rectangle((PADDING, PADDING, IMAGE_WIDTH - PADDING, IMAGE_HEIGHT - PADDING - 100), radius=10, fill='#282a36', outline='#F0F0F0', width=5)
# draw.rounded_rectangle((PADDING - 25, PADDING - 25, IMAGE_WIDTH - PADDING + 25, IMAGE_HEIGHT - PADDING + 50), radius=10, outline='#282a36', width=1)
final_image.paste(img, (PADDING+5, PADDING+5))
draw.rounded_rectangle((PADDING, PADDING, IMAGE_WIDTH - PADDING, IMAGE_HEIGHT - PADDING - 100), radius=10, outline='#F0F0F0', width=5)

fontsize = 30 
font = ImageFont.truetype('statics/FiraCode.ttf', fontsize)
draw.text((PADDING+10, IMAGE_HEIGHT - PADDING - 100), "@perceubertoletti.dev", font=font, fill=(100, 100, 100))

# Salvar imagem final
final_image.save(image_dest)