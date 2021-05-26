
import click

from infoget.get_info import scrp
from infoget.get_scan import scn
from infoget.get_detect import dtc




@click.command()

@click.option('-g','--gathering',help= " : this options is using for gathering information")

@click.option('-s','--scan',help= " : this options is using for scanning ip")

@click.option('-d','--detection',help= " : this options is using for detection vulnerability")


def main(gathering,scan,detection):

    """ simple tool for gathering information , scanning port and other ... """

    if gathering :
        scrp(gathering)

    if scan :
        scn(scan) 

    if detection :
        dtc(detection)


