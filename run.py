import typer
from generator.main import Pub
from generator.templates.polaroid import Polaroid
from generator.settings import Settings
app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def render_python(post_name: str):
    post_path = f"{Settings.BASE_PATH}/posts/python/{post_name}.py"
    pub = Pub(post_name, post_path, Polaroid)
    pub.generate()
    
if __name__ == "__main__":
    app()