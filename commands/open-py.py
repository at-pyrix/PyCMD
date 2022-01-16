from colorama import Fore as fc
import sys
import os
os.system("")
file = sys.argv[1]

path_to_file = f'C:\\Programming\\Python_Projects\\{file}'
print(f"{fc.LIGHTGREEN_EX}Starting {file} with Visual Studio Code{fc.RESET}")
try:
    os.chdir(path_to_file)
    os.system('code .')
except FileNotFoundError:
    print(f"{fc.LIGHTRED_EX}File not found{fc.RESET}")