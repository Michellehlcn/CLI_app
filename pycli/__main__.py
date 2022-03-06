import sys
from funcmodule import my_function
import click
from os import listdir
@click.command()
@click.option("--name",prompt="Data input - Which json file? Please provide the name and the end point. Eg. purchases_v1.json", help="Please provide the name and end point, eg. purchases_v1.json")

def main(name):
    list_ = []
    filenames = listdir(f'.')
    for filename in filenames:
        if filename.endswith('.json'):
            file = f'{filename}'
            list_.append(file)
    while name not in list_:
        click.echo('Incorrect file name given: {}'.format(name))
        name = click.prompt('Please enter file name')
    else:
        my_function(name)
               

if __name__ == '__main__':
    main()
