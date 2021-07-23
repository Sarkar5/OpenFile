import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
head= pyfiglet.figlet_format("Samim")
print(Fore.RED+head)
inp= input("Enter File Name:")
file= open(inp,"r")
print(file.read())
file.close()
