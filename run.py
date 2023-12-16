import os
import typer
from generator.main import Pub
from generator.templates.polaroidPython import PolaroidPython
from generator.templates.polaroidPhp import PolaroidPhp
from generator.templates.polaroidBun import PolaroidBun
from pygments.lexers import get_lexer_by_name

from generator.settings import Settings
from pathlib import Path


app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def render_bun(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/bun/{post_name}.ts"
    path = Path(post_path)
    lexer = get_lexer_by_name('typescript')
    if (path.is_file()):
        pub = Pub(post_name, post_path, PolaroidBun, lexer)
        pub.generate()
    else:
        post_path = f"{Settings.BASE_PATH}/posts/bun/{post_name}/"
        files = os.listdir(post_path)
        for index, file in enumerate(files):
            if file.startswith('__'):
                continue
            pub = Pub(f"{post_name}{index}", f"{post_path}{file}", PolaroidBun, lexer)
            pub.generate()

@app.command()
def render_python(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/python/{post_name}.py"
    path = Path(post_path)
    lexer = get_lexer_by_name('python')
    if (path.is_file()):
        pub = Pub(post_name, post_path, PolaroidPython, lexer)
        pub.generate()
    else:
        post_path = f"{Settings.BASE_PATH}/posts/python/{post_name}/"
        files = os.listdir(post_path)
        for index, file in enumerate(files):
            if file.startswith('__'):
                continue
            pub = Pub(f"{post_name}{index}", f"{post_path}{file}", PolaroidPython, lexer)
            pub.generate()

@app.command()
def render_php(post_name: str):
    lexer = get_lexer_by_name('php')
    post_path = f"{Settings.BASE_PATH}/posts/php/{post_name}.php"
    pub = Pub(post_name, post_path, PolaroidPhp, lexer)
    pub.generate()
    
if __name__ == "__main__":
    app()