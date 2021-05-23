from pyfiglet import Figlet
import click
import requests
from bs4 import BeautifulSoup
from infoget.fct import scrp
from colorama import Fore


@click.command()
@click.argument('url')

def main(url):

    # print the interfaces 
    print("")
    print(Fore.GREEN + "----------------------------- Info Get -----------------------------------")
    f = Figlet(font='slant')
    print(Fore.GREEN + f.renderText('I n f o  --  G e t'))
    print(Fore.GREEN + "----------------------------- Info Get -----------------------------------")
    print("")

    print(Fore.GREEN + "[+] please wait, because this operation might take some time : ")
    print("")


    # called scarping function to extract data 
    scrp(url)



