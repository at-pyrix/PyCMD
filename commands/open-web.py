import sys
import os
from colorama import Fore as fc
os.system("")
file = sys.argv[1].replace(".js", "").strip()
flag = sys.argv[1]

if ".js" in flag:
    path_to_file = f'C:\\Programming\\Web_Projects\\Javascript\\{file}'
else:
    path_to_file = f'C:\\Programming\\Web_Projects\\Websites\\{file}'
print(f"{fc.LIGHTGREEN_EX}Starting {file} with Visual Studio Code{fc.RESET}")

try:
    os.chdir(path_to_file)
    os.system('code .')
except FileNotFoundError:
    print(f"{fc.LIGHTRED_EX}Project not found {fc.RESET}")
