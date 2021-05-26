import nmap
from colorama import Fore
from pyfiglet import Figlet


def scn(scan) :

    print("")
    print(Fore.GREEN + "----------------------------- Info Get ------------------------------------")
    f = Figlet(font='slant')
    print(f.renderText("I n f o  --  G e t"))
    print(Fore.GREEN + "----------------------------- Info Get ------------------------------------")
    print(Fore.GREEN + "")
    

    print("[+] please wait, because this operation might take some time : ")
    print("")

    print(Fore.GREEN + " [+]" + Fore.WHITE +" welcome to the network scanner : ")

    sc = nmap.PortScanner()
    sc.scan(scan , '1-1023')

    print(" ")
    print(sc[scan]['tcp'].keys())