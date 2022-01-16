from colorama import Fore as fc
import os
import sys
os.system("")
file = sys.argv[1]
os.mkdir(f'C:\\Programming\\Java_Projects\\{file}')
print(F"{fc.LIGHTGREEN_EX}Project created{fc.RESET}")
with open(f'C:\\Programming\\Java_Projects\\{file}\\Main.java', 'w') as file_new:
    file_new.write(
        'import java.util.Scanner;\n\npublic class Main {\n\tpublic static void main(String[] args) {\n\n\t\tScanner sc = new Scanner(System.in);\n\n\t\t/*Your code here*/\n\n\t\tsc.close();\n\n\t}\n}')
    path_to_file = f'C:\\Programming\\Java_Projects\\{file}'
    print(f"{fc.LIGHTGREEN_EX}Created New Java Project: {file}{fc.RESET}")
    os.chdir(path_to_file)
    os.system('code .')
    pass
