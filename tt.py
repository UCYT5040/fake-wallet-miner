import time
import random
import string
import os
from colorama import init, Fore
init(convert=True)


LicenseKey = input(Fore.RED + 'Input License Key: ')
print(Fore.CYAN + "Checking if Key is Valid...")
time.sleep(1)
print(Fore.GREEN + "Key is Valid")
time.sleep(0.5)
os.system("cls")
Wallet = input(Fore.RED + "Wallet: ")
print(Fore.CYAN + "Checking if Wallet exists... ")
time.sleep(1)
print(Fore.GREEN + "Wallet Found!")
time.sleep(0.2)
print(Fore.BLUE+ "Setting up workspace for you...")
time.sleep(3)

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

tries = 0

while(True):
    if(tries > random.randint(10000, 100000)): # chance to get fake btc
        print(Fore.CYAN +"[-]"+ Fore.RED + " bc1" + id_gen() + Fore.GREEN +" | Valid |  " + "0.0335 BTC")
        print(Fore.GREEN +"Withdrawing to your Wallet...")
        time.sleep(10)
        tries = 0
        print(Fore.GREEN + "Done!")
        time.sleep(1)
    else:
        print(Fore.CYAN +"[-]"+ Fore.RED + " bc1" + id_gen() + Fore.CYAN +" | InValid |  " + "0.0000 BTC")
        tries += 1
