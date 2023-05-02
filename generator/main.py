from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from generator.settings import Settings

class Pub():

    def __init__(self, title, post_path, template) -> None:
        self.title = title
        self.post_path = post_path
        self.template = template
        pass

    def gerar_img_codigo(self):

        CODE = []
        with open(self.post_path, 'r') as f:
            CODE = f.readlines()
        CODE.append(' ')

        if len(CODE)<=0 and len(CODE)>30:
            raise Exception('seu algoritmo deve conter até 30 linhas')

        # Configurações do Pygments
        formatter = ImageFormatter(style="dracula", line_number_bg='#282a36', font='Fira Code', font_size=Settings.SIZE_FONT)
        code = highlight(''.join(CODE), PythonLexer(), formatter)

        with open(f'{Settings.BASE_PATH}/build/codigo.png', 'wb') as f:
            f.write(code)
        
        return Image.open(f'{Settings.BASE_PATH}/build/codigo.png')

    def generate(self):
        img_codigo = self.gerar_img_codigo()
        gerador = self.template(self.title, img_codigo, f"{Settings.BASE_PATH}/build/{self.title}")
        gerador.run()
