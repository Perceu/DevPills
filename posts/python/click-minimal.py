# Click é uma lib para facilitar a 
# construção de CLI facil e pratico 
# ainda permite varias configs 
# diferentes. Leia a DOC


import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--my-name-is', default='nobody')
def what_is_your_name(my_name_is):
    click.echo(f"Hello {my_name_is}")

if __name__ == '__main__':
    cli()