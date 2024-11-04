import os
import typer
from generator.main import Pub
from generator.templates.polaroidPython import PolaroidPython
from generator.templates.polaroidLua import PolaroidLua
from generator.templates.polaroidGo import PolaroidGo
from generator.templates.polaroidPhp import PolaroidPhp
from generator.templates.polaroidBun import PolaroidBun
from generator.templates.polaroidRust import PolaroidRust
from pygments.lexers import get_lexer_by_name

from generator.settings import Settings
from pathlib import Path


app = typer.Typer()


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
def render_lua(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/lua/{post_name}.lua"
    path = Path(post_path)
    lexer = get_lexer_by_name('lua')
    if (path.is_file()):
        pub = Pub(post_name, post_path, PolaroidLua, lexer)
        pub.generate()
    else:
        post_path = f"{Settings.BASE_PATH}/posts/lua/{post_name}/"
        files = os.listdir(post_path)
        for index, file in enumerate(files):
            if file.startswith('__'):
                continue
            pub = Pub(f"{post_name}{index}", f"{post_path}{file}", PolaroidLua, lexer)
            pub.generate()

@app.command()
def render_php(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/php/{post_name}.php"
    path = Path(post_path)
    lexer = get_lexer_by_name('php')
    if (path.is_file()):
        pub = Pub(post_name, post_path, PolaroidPhp, lexer)
        pub.generate()
    else:
        post_path = f"{Settings.BASE_PATH}/posts/php/{post_name}/"
        files = os.listdir(post_path)
        for index, file in enumerate(files):
            if file.startswith('__'):
                continue
            pub = Pub(f"{post_name}{index}", f"{post_path}{file}", PolaroidPhp, lexer)
            pub.generate()

@app.command()
def render_go(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/go/{post_name}.go"
    path = Path(post_path)
    lexer = get_lexer_by_name('go')
    if (path.is_file()):
        pub = Pub(post_name, post_path, PolaroidGo, lexer)
        pub.generate()
    else:
        post_path = f"{Settings.BASE_PATH}/posts/go/{post_name}/"
        files = os.listdir(post_path)
        for index, file in enumerate(files):
            if file.startswith('__'):
                continue
            pub = Pub(f"{post_name}{index}", f"{post_path}{file}", PolaroidGo, lexer)
            pub.generate()

@app.command()
def render_rust(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/rust/{post_name}.rs"
    path = Path(post_path)
    lexer = get_lexer_by_name('rust')
    if (path.is_file()):
        pub = Pub(post_name, post_path, PolaroidRust, lexer)
        pub.generate()
    else:
        post_path = f"{Settings.BASE_PATH}/posts/rust/{post_name}/"
        files = os.listdir(post_path)
        for index, file in enumerate(files):
            if file.startswith('__'):
                continue
            pub = Pub(f"{post_name}{index}", f"{post_path}{file}", PolaroidRust, lexer)
            pub.generate()

if __name__ == "__main__":
    app()
