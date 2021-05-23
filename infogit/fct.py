import requests
from bs4 import BeautifulSoup
from colorama import Fore


#list final of data
#set final list of data extracted as a global variable 
global back_final , net_final , ssl_final , ip4_final , ip6_final
back_final =  []
net_final = []
ssl_final = []
ip4_final = []
ip6_final = []



def scrp(url) : # function to mget and manage data

    # get all html of url using requests
    URL = "https://sitereport.netcraft.com/?url="+url  
    res = requests.get(URL)
    src = res.content
    soup = BeautifulSoup(src,"lxml")


    #final list of data extracted 
    back_befor = []
    net_befor = []
    ssl_befor = []


    # for get special data from website using BeautifulSou
    back = soup.find_all("section",attrs={"id":"background_table_section"})
    net = soup.find_all("section",attrs={"id":"network_table_section"})
    ssl = soup.find_all("section",attrs={"id":"ssl_table_section"})


    # Remove space and other character from list --- for background list
    a = back[0].text.replace('\xa0',' ')
    back_befor.append(a.strip())
    back_befor = back_befor[0].split("\n")
    for x in back_befor:
        if x.strip():
            back_final.append(x)


        
    # Remove space and other character from list --- for network list
    a = net[0].text.replace('\xa0',' ')
    net_befor.append(a.strip())
    net_befor = net_befor[0].split("\n")
    for x in net_befor:
        if x.strip():
            net_final.append(x)




    # Remove space and other character from list --- for ssl list
    a = ssl[0].text.replace('\n', ' ')
    ssl_befor.append(a.strip())
    ssl_befor = ssl_befor[0].split("      ") 
    for x in ssl_befor:
        if x.strip():
            ssl_final.append(x)




    # Just for abbriviate name 
    back = back_final
    net = net_final
    ssl = ssl_final



    #Creat ip4 table from network table 
    for i in range(len(net)) :
        if net[i] == 'IP delegation' :
            k = i
            for x in range(k+1,len(net)) :
                ip4_final.append(net[x])
            break
        elif net[i] == 'IPv6 address' :
            if net[i+1] == 'Not Present' :
                ip6 = "Not Present"
            else :
                ip6 = net[i+1]
        else :
            pass


    #Creat ip6 table from network table if it present
    if ip6 !=  'Not Present' :
        global var
        var = 'IPv6 address ('+ip6+')'
        for i in range(len(net)) :
            if net[i] == var :
                k = i
                for x in range(k,len(net)) :
                    ip6_final.append(net[x])
                break

            else :
                pass



    # remove ip table from network table 
    for x in range(len(net)) :
        while net[-1] != 'Latest Performance' :
            net.pop()
    net.pop()

    # remove ip6 from ip4 table 
    for x in range(len(ip4_final)) :
        if ip6 != 'Not Present' :
            while ip4_final[-1] != var :
                ip4_final.pop()
            ip4_final.pop()



    # print backgound table :
    print("")
    print(Fore.GREEN + '[+] %s :'%back[0]) # title 
    print(Fore.GREEN +  "------------------------")
    print(Fore.WHITE + "Site title            ==  Not Acceptable! ")
    print(Fore.GREEN + "------------------------")
    print(Fore.WHITE + "Date first seen       ==  %s" % back[6])
    print(Fore.GREEN + "------------------------")
    print(Fore.WHITE + "Site rank             ==  %s" % back[3])
    print(Fore.GREEN + "------------------------")
    print(Fore.WHITE + "Netcraft Risk Rating  ==  %s" % back[8])
    print(Fore.GREEN + "------------------------")
    print(Fore.WHITE + "Description           ==  Not Present ")
    print(Fore.GREEN + "------------------------")
    print(Fore.WHITE + "Primary language      ==  Not Present ")
    print(Fore.GREEN + "------------------------")



    # print network table :
    print("")
    print("")
    print(Fore.GREEN + '[+] %s :'%net[0]) # title
    x , y = 1 , 2
    for i in range(len(net)//2) :
            print((Fore.GREEN + "--------------------------------------------------------"))
            print( Fore.WHITE +  "{}".format(net[x].strip() + "  ==  "+"{}".format(net[y].strip())))
            x+=2
            y+=2
    print((Fore.GREEN + "--------------------------------------------------------"))




    # print ip4 table :
    print("")
    print("")
    print(Fore.GREEN + '[+] %s :'%ip4_final[0]) # title 
    print((Fore.GREEN + "----------------------------------------------------------"))
    print( Fore.GREEN + "{}  -----  {}  -----  {}  -----  {}  ".format(ip4_final[1],ip4_final[2],ip4_final[3],ip4_final[4])) # table colon
    print((Fore.GREEN + "-------------------------------------------------------------------------------------------------------------------------------------------------"))
    a, b, c, d = 5, 6, 7, 8
    for i in range(len(ip4_final)//4-1):
        print(Fore.WHITE + "{} -- {} -- {} -- {} ".format(ip4_final[a].replace(" &rdsh; ","").strip(),ip4_final[b].strip(),ip4_final[c].replace(" &rdsh; ","").strip(),ip4_final[d].strip()))
        print((Fore.GREEN + "-------------------------------------------------------------------------------------------------------------------------------------------------"))
        a+=4
        b+=4
        c+=4
        d+=4


    # print ip6 table if it present : 
    if ip6 != 'Not Present' :
        print("")
        print("")
        print(Fore.GREEN + '[+] %s :'%ip6_final[0]) # title 
        print((Fore.GREEN + "----------------------------------------------------------"))
        print( Fore.GREEN + "{}  -----  {}  -----  {}  -----  {}  ".format(ip6_final[1],ip6_final[2],ip6_final[3],ip6_final[4])) # table colon
        print((Fore.GREEN + "-------------------------------------------------------------------------------------------------------------------------------------------------"))
        a, b, c, d = 5, 6, 7, 8
        for i in range(len(ip6_final)//4-1):
            print(Fore.WHITE + "{} -- {} -- {} -- {} ".format(ip6_final[a].replace(" &rdsh; ","").strip(),ip6_final[b].strip(),ip6_final[c].replace(" &rdsh; ","").strip(),ip6_final[d].strip()))
            print((Fore.GREEN + "-------------------------------------------------------------------------------------------------------------------------------------------------"))
            a+=4
            b+=4
            c+=4
            d+=4



    # print ssl table : 
    print("")
    print(Fore.GREEN + '[+] %s :'%ssl[0]) # title 
    print(Fore.GREEN +  "------------------------------------------------------------------------------------------------")
    print(Fore.WHITE +  ssl[1])
    print(Fore.GREEN +  "------------------------------------------------------------------------------------------------")            
