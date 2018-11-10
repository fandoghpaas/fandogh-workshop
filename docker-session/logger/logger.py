import click
from time import sleep

counter = 1
while True:
    if counter % 2 == 0:
        click.echo(str(''))
    else:
        click.echo(str(counter))
    counter += 1
    sleep(5)

