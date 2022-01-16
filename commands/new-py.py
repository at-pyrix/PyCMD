from colorama import Fore as fc
import os
import sys
file = sys.argv[1]
os.mkdir(f'C:\\Programming\\Python_Projects\\{file}')
print(f"{fc.LIGHTGREEN_EX}Project created{fc.RESET}")

with open(f'C:\\Programming\\Python_Projects\\{file}\\Main.py', 'w') as file_new:
    file_new.write('if __name__ == \'__main__\':\n\tpass')
    file_new.close()
    path_to_file = f'C:\\Programming\\Python_Projects\\{file}'
    print(f"{fc.LIGHTGREEN_EX}Created New Python Project: {file}{fc.RESET}")
    os.chdir(path_to_file)
    os.system('code .')
    pass
