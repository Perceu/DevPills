import os
import typer
from generator.main import Pub
from generator.templates.polaroidPython import PolaroidPython
from generator.templates.polaroidPhp import PolaroidPhp
from generator.settings import Settings
from pathlib import Path


app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def render_python(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/python/{post_name}.py"
    path = Path(post_path)
    if (path.is_file()):
        pub = Pub(post_name, post_path, PolaroidPython)
        pub.generate()
    else:
        post_path = f"{Settings.BASE_PATH}/posts/python/{post_name}/"
        files = os.listdir(post_path)
        for index, file in enumerate(files):
            if file.startswith('__'):
                continue
            pub = Pub(f"{post_name}{index}", f"{post_path}{file}", PolaroidPython)
            pub.generate()

@app.command()
def render_php(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/php/{post_name}.php"
    pub = Pub(post_name, post_path, PolaroidPhp)
    pub.generate()
    
if __name__ == "__main__":
    app()