import sys
import os
import json
from colorama import Fore as fc, Back as bg, Style as st, init
init(autoreset=True)

with open('json/config.json', 'r') as file:
    config = json.load(file)
    file.close()

editor = config['text-editor']

pycmd_path = os.path.realpath(os.getcwd())

if '-e' in sys.argv:
    editor = 'Explorer'

print('Opening PYCMD Source Code with '+ fc.CYAN + editor)

if editor == 'Explorer':
    os.system(f'explorer {pycmd_path}')
elif editor == 'Visual Studio Code':
    os.system(f'code {pycmd_path}')
elif editor == 'Vim':
    os.system(f'vim {pycmd_path}')
elif editor == 'Sublime Text':
    os.system(f'subl {pycmd_path}')
elif editor == 'Atom':
    os.system(f'atom {pycmd_path}')
elif editor == 'Emacs':
    os.system(f'emacs {pycmd_path}')
elif editor == 'Nano':
    os.system(f'nano {pycmd_path}')