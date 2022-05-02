from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from colorama import Fore , Style , Back
from hexer import mHash
from datetime import datetime
import threading


def timer() :
    tcx = datetime.now().time()
    return tcx


p2shp = """
                                 ---***---
           
           ███╗    ██████╗ ██████╗ ██████╗ ██╗  ██╗██╗  ██╗    ███╗
           ██╔╝    ██╔══██╗╚════██╗██╔══██╗██║ ██╔╝██║  ██║    ╚██║
           ██║     ██████╔╝ █████╔╝██████╔╝█████╔╝ ███████║     ██║
           ██║     ██╔═══╝ ██╔═══╝ ██╔═══╝ ██╔═██╗ ██╔══██║     ██║
           ███╗    ██║     ███████╗██║     ██║  ██╗██║  ██║    ███║
           ╚══╝    ╚═╝     ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══╝
                                                                   
                                 ---***---                                         
        """

print(Fore.YELLOW + p2shp)

filename = 'p2pkh.txt'
with open(filename) as f :
    add = f.read().split()
add = set(add)
print(Fore.WHITE , '[*]All Address TYPE P2PKH Start With 1 import Now...' , Back.RED , timer() , Style.RESET_ALL , '\n')
print(
    Fore.BLUE + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(' + Fore.YELLOW + ' M M D R Z A . C o M ' + Fore.BLUE + ')~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

r = 1
cores = 2


def seek(r) :
    z = 0
    w = 0
    while True :
        txx = timer()
        hdwallet: HDWallet = HDWallet(symbol = SYMBOL)
        hdwallet.from_private_key(private_key = mHash())
        addr = hdwallet.p2pkh_address()

        print(Fore.GREEN , 'Total:' , Fore.YELLOW , str(z) , Fore.GREEN , 'Win:' , Fore.WHITE , str(w) , Fore.RED ,
              str(addr) , Back.MAGENTA , Fore.WHITE , txx , Style.RESET_ALL ,
              end = '\r')
        z += 1
        if addr in add :
            w += 1
            print(Fore.WHITE , 'Winning Wallet On Database File Imported ... [LOADED]')
            print(Fore.CYAN , 'All Details Saved On Text File Root Path ... [WRITED]')
            f = open("p2shWinerWalletDetails.txt" , "a")
            f.write('\n' , str(addr))
            f.write('\n' , str(priv))
            f.write('\n==========[PROGRAMMER BY MMDRZA.CoM]==========\n')
            f.close()
            print(Fore.MAGENTA , 'Information File Name ========> p2shWinerWalletDetails.txt [OK]')
            continue


seek(r)

t1 = Thread(target = timer)
t2 = Thread(target = timer)
t3 = Thread(target = seek , args = r)
t4 = Thread(target = seek , args = r)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
