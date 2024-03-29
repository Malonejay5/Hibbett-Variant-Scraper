import time
import colorama
import requests 
import json
from bs4 import BeautifulSoup as soup
import urllib3
from colorama import Fore
urllib3.disable_warnings()
colorama.init(autoreset=True)

####################################################
# SIZES AND VARIANT EXAMPLE FOR LEN()

variant = '44326536'
sizes = ['050','055','060','065','070','075','080','085','090','095','100','105','110','115','120','125','130','140']
gsSized = ['035', '040', '045', '050', '055', '060', '065', '070']
Yeezysizes = ['050','060','070','080','090','100','110','120','130','140','150','160']
YeezyGS = ['040', '050', '060', '070']

####################################################


# user agent to stop intstant flag my permiterX
user_agent = {'User-agent': 'Mozilla/5.0'}

####################################################

# USER INPUTS

print("----------------------------------------------------")
print(Fore.CYAN + "Hibbett Variant Scraper For Filipi Bot" + " " + Fore.GREEN +"v.1.0.2")
print("----------------------------------------------------")
inpPID = input(Fore.LIGHTCYAN_EX + 'Enter PID,COLOR'+Fore.WHITE +': ')
print("---------------")
# Split Pid,Color by ','
Pid = inpPID.split(',')[0]
Color = inpPID.split(',')[1]

inpSizing = input('1)'+ ' ' + Fore.LIGHTCYAN_EX + 'Adult Sizing' + ' ' + Fore.WHITE + '2)' + ' ' + Fore.LIGHTCYAN_EX + 'Grade-School' + ' '+ Fore.WHITE + '3)' + ' ' + Fore.LIGHTCYAN_EX + 'Yeezys' + ' ' + Fore.WHITE + '4)' +  ' ' + Fore.LIGHTCYAN_EX + 'Yeezy Grade-School' + ' '  + Fore.WHITE + '[1/2/3/4]? : ')
print("---------------")




####################################################

if inpSizing == '1':


    inpTitle = input("Enter Product Name: ")
    print("-----------------")

    variantTXT = open(inpTitle +'.txt', 'a')
    variantTXT.write(inpTitle)
    variantTXT.write("\n")
    variantTXT.write(inpPID)
    variantTXT.write("\n")

    print("Finding Variants...")

    # Single singe size out of size group
    for size in sizes:
        mainURL = 'https://www.hibbett.com'
        adultLink = 'https://www.hibbett.com/product?pid={}&dwvar_{}_size=0{}&dwvar_{}_color={}'.format(Pid, Pid, size ,Pid ,Color)
        
        
        
        s = requests.Session()
        r = s.get(adultLink, timeout=30, headers= user_agent, verify=False)
        time.sleep(3)
        data = soup(r.content, 'html.parser')
        time.sleep(3)
        
        soupVar = data.find_all('input', attrs= {"name": "pid"})
        trueSizing = size[0]+ size[1] + "." + size[2]
        for value in soupVar:
            if len(value['value']) != len(variant):
                print(Fore.YELLOW + ('Size: {} Not Available... Trying Next Size ').format(trueSizing))
            else:
                    
                    variantTXT.write(trueSizing + ':' + ' ' + value['value'] )
                    variantTXT.write('\n')
                    print(Fore.GREEN +("Size: {} is Done!").format(trueSizing))

####################################################
# GS SIZING IS SELECTED

else: 
    if inpSizing == "2":

        inpTitle = input("Enter Product Name: ")
        print("-----------------")

        # Makes a .txt File with Variants Name the Product Title

        variantTXT = open(inpTitle +'.txt', 'a')
        variantTXT.write(inpTitle)
        variantTXT.write("\n")
        variantTXT.write(inpPID)
        variantTXT.write("\n")

        print("Finding Variants...")

            # Single singe size out of size group
        for gsSize in gsSized:
            gsLink = 'https://www.hibbett.com/product?pid={}&dwvar_{}_size=0{}&dwvar_{}_color={}'.format(Pid, Pid, gsSize ,Pid ,Color)

            
            s = requests.Session()
            r = s.get(gsLink, timeout=30, headers= user_agent, verify=False)
            
            time.sleep(3)
            data = soup(r.content, 'html.parser')
            time.sleep(3)


            soupVar = data.find_all('input', attrs= {"name": "pid"})
            soupTitle = data.find_all('div', attrs={"class":"product-name"})
            trueGsSizing = gsSize[1] + "." + gsSize[2]
            for value in soupVar:
                if len(value['value']) != len(variant):
                    print(Fore.YELLOW + ('Size: {} Not Available... Trying Next Size ').format(trueGsSizing))
                else:

                    
                    variantTXT.write(trueGsSizing + ':' + value['value'] )
                    variantTXT.write('\n')
                    print(Fore.GREEN + ("Size: {} is Done!").format(trueGsSizing))


####################################################
# YEEZY IS SELECTED


    elif inpSizing == '3':
            


        inpTitle = input("Enter Product Name: ")
        print("-----------------")

        variantTXT = open(inpTitle +'.txt', 'a')
        variantTXT.write(inpTitle)
        variantTXT.write("\n")
        variantTXT.write(inpPID)
        variantTXT.write("\n")

        print("Finding Variants...")

        # Single singe size out of size group
        for size in Yeezysizes:
            mainURL = 'https://www.hibbett.com'
           
            YeezyadultLink = 'https://www.hibbett.com/product?pid={}&dwvar_{}_size=2{}&dwvar_{}_color={}'.format(Pid, Pid, size ,Pid ,Color)
            
            
            s = requests.Session()
            r = s.get(YeezyadultLink, timeout=30, headers= user_agent, verify=False)
            time.sleep(3)
            data = soup(r.content, 'html.parser')
            time.sleep(3)

            soupVar = data.find('script', attrs= {"type": "application/ld+json"})
        
            findData = json.loads(soupVar.text)

            trueSizing = size[0]+ size[1] + "." + size[2]
            for sku in findData:
                findSku = sku['sku']
                print(findSku)

                if len(findSku) != len(variant):
                    print(Fore.YELLOW + ('Size: {} Not Available... Trying Next Size ').format(trueSizing))
                else:
                        
                        variantTXT.write(trueSizing + ':' + ' ' + findSku )
                        variantTXT.write('\n')
                        print(Fore.GREEN +("Size: {} is Done!").format(trueSizing))

####################################################
# YEEZY (gs) IS SELECTED

    elif inpSizing == '4':
            


        inpTitle = input("Enter Product Name: ")
        print("-----------------")

        variantTXT = open(inpTitle +'.txt', 'a')
        variantTXT.write(inpTitle)
        variantTXT.write("\n")
        variantTXT.write(inpPID)
        variantTXT.write("\n")

        print("Finding Variants...")

        # Single singe size out of size group
        for size in YeezyGS:
            mainURL = 'https://www.hibbett.com'
           
            YeezyGSLink = 'https://www.hibbett.com/product?pid={}&dwvar_{}_size=0{}&dwvar_{}_color={}'.format(Pid, Pid, size ,Pid ,Color)
            
            
            s = requests.Session()
            r = s.get(YeezyGSLink, timeout=30, headers= user_agent, verify=False)
            time.sleep(3)
            data = soup(r.content, 'html.parser')
            time.sleep(3)

            soupVar = data.find('script', attrs= {"type": "application/ld+json"})
        
            findData = json.loads(soupVar.text)
            
            trueSizing = size[0]+ size[1] + "." + size[2]
            for sku in findData:
                findSku = sku['sku']
                print(findSku)

                if len(findSku) != len(variant):
                    print(Fore.YELLOW + ('Size: {} Not Available... Trying Next Size ').format(trueSizing))
                else:
                        
                        variantTXT.write(trueSizing + ':' + ' ' + findSku )
                        variantTXT.write('\n')
                        print(Fore.GREEN +("Size: {} is Done!").format(trueSizing))
                    
