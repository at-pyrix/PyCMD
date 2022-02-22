import stat
import shutil
import sys
from colorama import Fore as fc
import os
os.system("")
file = sys.argv[1]
path = f'C:\\Programming\\Python_Projects\\{file}'

confirmation = input(f"{fc.LIGHTCYAN_EX}Are you sure? [Y/n]{fc.RESET}\n")

if "y" in confirmation:
    def on_rm_error(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)

    try:
        shutil.rmtree(path, onerror=on_rm_error)
        print(f"{fc.LIGHTGREEN_EX}Deleted {file}{fc.RESET}")
    except FileNotFoundError:
        print(f"{fc.LIGHTRED_EX}{file} not found{fc.RESET}")
    except PermissionError:
        print(f"{fc.LIGHTRED_EX}File is currently in use{fc.RESET}")
    try:
        from subprocess import run
        output = run(
            f"curl -X DELETE -u Yasho:{github_token} https://api.github.com/repos/Yasho022/{file}", capture_output=True).stdout
        output = str(output)
        if "Not Found" in output:
            print(f"{fc.LIGHTRED_EX}No Repository Named {file}{fc.RESET}")
        else:
            print(
                f"{fc.LIGHTGREEN_EX}Deleted {file} Repository from Github {fc.RESET}")
    except PermissionError:
        print(f"{fc.LIGHTRED_EX}Access Denied{fc.RESET}")

else:
    print(f"{fc.LIGHTRED_EX}Task Failed Successfully{fc.RESET}")
