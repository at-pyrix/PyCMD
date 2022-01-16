import sys
import os
from colorama import Fore as fc
os.system("")
repo_Name = sys.argv[1].replace('.js', '').strip()
flags = sys.argv[1]

if ".js" in flags:
    path = f'C:\\Programming\\Web_Projects\\Javascript\\{repo_Name}'
    _dir = path
    os.mkdir(_dir)
    os.chdir(_dir)
    with open(f'main.js', 'a+') as file_new:
        file_new.write('console.log("Hello World!");')
        file_new.close()
    print(f"{fc.LIGHTGREEN_EX}Created a new Javascript Project: {repo_Name.title()}{fc.RESET}")
    os.chdir(path)
    os.system('code .')

else:

    path = f'C:\\Programming\\Web_Projects\\Websites\\{repo_Name}'
    _dir = path

    os.mkdir(_dir)
    os.chdir(_dir)
    with open(f'index.html', 'a+') as file_new:
        file_new.write(
            f'<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>{repo_Name}</title>\n\t<link rel="stylesheet" href="style.css">\n</head>\n<body>\n\n<script src="main.js"></script>\n</body>\n</html>\n'
        )

        file_new.close()
    with open(f'style.css', 'a+') as file_new:
        file_new.write("*{\n\n\n}")
        file_new.close()
    with open(f'main.js', 'a+') as file_new:
        file_new.write('//Auto Generated\nalert("Hello World!");')
        file_new.close()
    print(f"{fc.LIGHTGREEN_EX}Created a new Web Project: {repo_Name.title()}{fc.RESET}")
    os.chdir(path)
    os.system('code .')
