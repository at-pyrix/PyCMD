import os
import sys
from colorama import Fore as fc
os.system("")

file = sys.argv[1].replace(".js", "").strip()

confirmation = input(f"{fc.LIGHTCYAN_EX}Are you sure? [Y/n]{fc.RESET}\n")

if "y" in confirmation.lower():

    try:
        from subprocess import run
        output = run(
            f"curl -X DELETE -u Yasho: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 https://api.github.com/repos/Yasho022/{file}", capture_output=True).stdout
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
