# Command handler for the create command
from github import Github
from colorama import Fore as fc, Back as bg, init
import sys
import msvcrt
import json
import itertools
import textwrap
import os
from dotenv import load_dotenv
from pycmd.utils.pycmd import argparse, execute
import threading
import re
import time
import cursor

init(autoreset=True)
load_dotenv()


argument, flags = argparse(sys.argv)

if "." not in argument:
    argument = "untitled.unknown"
    # This will classify it as "Unknown Project"

project_name = re.sub("\W|^(?=\d)", "_", argument.split(".")[0])

with open("json/config.json", "r") as file:
    config = json.load(file)
    file.close()

extension = ""
boiler_plate = ""

if ".py" in argument:
    extension = ".py"
    language = "python"
    boiler_plate = f"""
    # {project_name}
    
    def main():
        # Write your code here
        pass
        
    if __name__ == '__main__':
        main()
    """

elif ".js" in argument or ".nodejs" in argument:
    extension = ".js"
    language = "node.js"
    boiler_plate = f"// {project_name}\n"

elif ".java" in argument:
    extension = ".java"
    language = "java"
    boiler_plate = f"""
    // {project_name}
    
    import java.util.Scanner;
    
    class {project_name} {{
    
        public static void main(String[] args) {{
            
            Scanner scanner = new Scanner(System.in);
            
            // Write your code here
            
            scanner.close();
        }}
    }}   
    """

elif ".html" in argument or ".css" in argument or ".web" in argument:
    language = "web"
    boiler_plate = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_name}</title>
        <script src="index.js"></script>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <!-- Write your code here -->
    </body>
    </html>
    """

elif ".rs" in argument:
    language = "rust"

elif ".cpp" in argument or ".c++" in argument:
    extension = ".cpp"
    language = "c++"

    boiler_plate = f"""
    // {project_name}
    
    int main() {{
    // Write your code here
}}
    """

elif ".go" in argument:
    extension = ".go"
    language = "go"

    boiler_plate = f"""
    // {project_name}
    
    package main
    
    func main() {{
        // Write your code here
    }}
    """

elif ".ts" in argument:
    extension = ".ts"
    language = "typescript"
    boiler_plate = f"// {project_name}\n"

elif ".cs" in argument and not ".css" in argument:
    extension = ".cs"
    language = "c#"
    boiler_plate = f"""
    // {project_name}
    
    using System;
    
    class {project_name} {{    
        static void Main(string[] args)
        {{
            // Write your code here
        }}
    }}
    """

else:
    print(
        textwrap.dedent(
            f"""
    {bg.RED}ERR{bg.RESET} {fc.RESET}Unknown project type.
    See the list of projects below:
    
    {fc.LIGHTBLUE_EX}.py{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Python Project
    {fc.LIGHTBLUE_EX}.js{fc.LIGHTBLACK_EX}   -  {fc.GREEN}JavaScript Project
    {fc.LIGHTBLUE_EX}.java{fc.LIGHTBLACK_EX} -  {fc.GREEN}Java Project
    {fc.LIGHTBLUE_EX}.html{fc.LIGHTBLACK_EX} -  {fc.GREEN}Web Project
    {fc.LIGHTBLUE_EX}.rs{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Rust Project
    {fc.LIGHTBLUE_EX}.cpp{fc.LIGHTBLACK_EX}  -  {fc.GREEN}C++ Project
    {fc.LIGHTBLUE_EX}.go{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Go Project
    {fc.LIGHTBLUE_EX}.ts{fc.LIGHTBLACK_EX}   -  {fc.GREEN}TypeScript Project
    {fc.LIGHTBLUE_EX}.cs{fc.LIGHTBLACK_EX}   -  {fc.GREEN}C# Project
    """
        )
    )
    exit(1)


try:
    root_folder = config["projects"][f"{language}_projects_path"]
except KeyError:
    print(
        bg.RED
        + "ERR"
        + bg.RESET
        + " "
        + f"{language.title()} Projects path is not specified."
    )
    print(
        bg.BLUE
        + "INFO"
        + bg.RESET
        + " "
        + f"Please add the path to the config.json file or run the {fc.CYAN}pycmd setup projects{fc.RESET} command."
    )
    exit(1)

project_path = os.path.join(root_folder, project_name)

end = False
text = ""

# Inspired from: https://stackoverflow.com/a/22029635
def animate():
    cursor.hide()
    for c in itertools.cycle(["⠟", "⠯", "⠷", "⠾", "⠽", "⠻"]):
        if end:
            break
        sys.stdout.write("\r" + fc.LIGHTYELLOW_EX + c + fc.RESET + f" {text}")
        sys.stdout.flush()
        time.sleep(0.07)
    cursor.show()


def git_init(name, private: bool = False):

    load_anim = threading.Thread(target=animate)
    load_anim.daemon = True

    token = os.environ.get("GITHUB_TOKEN")

    gh = Github(token)
    user = gh.get_user()
    public_priv = "private" if private else "public"

    print(
        f"\n{fc.MAGENTA}Initializing {public_priv} repository: {fc.LIGHTYELLOW_EX}{name}"
    )

    global text, end
    text = "Creating repository"

    load_anim.start()
    try:
        user.create_repo(name, private=private)
    except Exception as e:
        end = True
        err_message = ("{" + str(e).split("{", 1)[1].rsplit("}", 1)[0] + "}").replace(
            "'", '"'
        )
        err_message = json.loads(err_message)
        
        print("\r" + bg.RED + "ERR" + bg.RESET + " " + err_message["message"] + " " * 20)
        for i in err_message['errors']:
            if i['message']:
                print(bg.BLUE + "INFO" + bg.RESET + " " + i['message'])
        print()
        exit(1)
    else:
        commands = [
            {"git init": "Initializing git"},
            {
                f"git remote add origin https://github.com/{user.login}/{project_name}.git": "Connecting to remote repository"
            },
            {"git add -A": "Adding files"},
            {'git commit -m "Initial commit"': "Committing files"},
            {"git push -u origin master": "Pushing files to remote"},
        ]
        for i in commands:
            command = list(i.keys())[0]
            description = i[command]
            execute(command, True, True)
            text = description + " " * 20

        end = True
        load_anim.join()
        print(fc.GREEN + "\rSuccessfully initialized git" + " " * 20)


boiler_plate = textwrap.dedent(boiler_plate).strip()

print()

if "-l" in flags or "-local" in flags:
    print(f"Git: {fc.RED}Not Initializing")
else:
    private = True if "-p" in flags or "-private" in flags else False
    print(
        f"Git: {fc.GREEN}Initializing {fc.LIGHTBLUE_EX}private {fc.GREEN}repository"
        if private
        else f"Git: {fc.GREEN}Initializing {fc.LIGHTBLUE_EX}public {fc.GREEN}repository"
        + fc.RESET
    )
    
    
# If you want to never get this warning, change this line to:

"""

`if '-y' not in flags:`

# Change to:

`if False:`

"""
    
if "-y" not in flags:

    def listen_to_keyboard():
        while not time_over:
            key = msvcrt.getch()
            if key == b"n":
                global cancelled
                print(fc.RED + "\rCancelled" + " " * 50)
                cancelled = True
                exit(1)
            elif key == b"y":
                global continued
                print(
                    "\r" + fc.YELLOW + "Creating project in " + project_path + " " * 50
                )
                continued = True
                break

    print(
        f"Press {fc.CYAN}Y{fc.RESET} to continue or {fc.CYAN}N{fc.RESET} to cancel.\n"
    )
    cancelled = False
    time_over = False
    continued = False
    threading.Thread(target=listen_to_keyboard).start()
    for i in range(5, 0, -1):
        if cancelled:
            exit(0)
        if continued:
            break
        sys.stdout.write(
            "\r"
            + bg.BLUE
            + "INFO"
            + bg.RESET
            + " "
            + f'Creating {language} project "{project_name}" in {fc.CYAN}{i}{fc.RESET} seconds'
        )
        time.sleep(1)
    time_over = True

print(fc.MAGENTA + "\rCreating Directories..." + " " * 50)

try:
    os.mkdir(project_path)
    os.chdir(project_path)
except Exception as e:
    print(bg.RED + "\rERR" + bg.RESET + " " + str(e).split("] ")[1] + " " * 20)
    exit(1)

if language == "web":
    with open("index.html", "w") as file:
        file.write(boiler_plate)
        file.close()
    open("index.js", "w").close()
    open("style.css", "w").close()

elif language == "rust":
    execute(f"cargo new .", True)

elif language == "node.js":
    with open(f"index.js", "w") as file:
        file.write(boiler_plate)
        file.close()

        output = execute("npm init -y")

        if not output:
            print("\nSkipping...")

else:
    with open("main" + extension, "w") as file:
        file.write(boiler_plate)
        file.close()

with open("README.MD", "w") as file:
    file.write("# " + project_name)
    file.close()

print(fc.GREEN + "Successfully generated files")

if not "-local" in flags and not "-l" in flags:
    if "-private" in flags or "-p" in flags:
        git_init(project_name, True)
    else:
        git_init(project_name)

# Open project
try:
    text_editor = config["text-editor"]
except KeyError:
    print(
        bg.YELLOW
        + fc.BLACK
        + "\rWARNING"
        + fc.RESET
        + bg.RESET
        + " "
        + "No text editor specified in config.json"
    )
    print(
        f"Set the default text editor to open the project with the {fc.CYAN}pycmd setup editor{fc.RESET} command."
    )
    exit()

if text_editor == "Visual Studio Code":
    execute(f"code {project_path}")

elif text_editor == "Sublime Text":
    execute(f"subl {project_path}")

elif text_editor == "Atom":
    execute(f"atom {project_path}")

elif text_editor == "PyCharm":
    execute(f"pycharm64.exe {project_path}")

else:
    execute(f"cd {project_path} && {text_editor}")
