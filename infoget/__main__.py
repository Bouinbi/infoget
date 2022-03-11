
import click

from infoget.get_info import scrp

@click.command()

@click.option('-g','--gathering',help= " : this options is using for gathering information")


def main(gathering):

    """ simple tool for gathering information , scanning port and other ... """

    if gathering :
        scrp(gathering)

