
import nmap
import os
from colorama import Fore
from pyfiglet import Figlet


def dtc(scan) :

    print("")
    print(Fore.GREEN + "----------------------------- Info Get ------------------------------------")
    f = Figlet(font='slant')
    print(f.renderText("I n f o  --  G e t"))
    print(Fore.GREEN + "----------------------------- Info Get ------------------------------------")
    print("")

    print("[+] please wait, because this operation might take some time : ")
    print("")

    print(Fore.GREEN + " [+]" + Fore.WHITE + " Welcome to the velnurebeleties scanner : ")

    print("")
    print(os.system('nmap -sV --script-args=vulscan.nse '+scan))
