from colorama import Fore as fc, init
import wx
import requests
from difflib import SequenceMatcher
import msvcrt
from textwrap import dedent
import requests
from time import sleep
import dotenv
import sys
import os
import json
init(autoreset=True)
dotenv.load_dotenv()

# WARNING: SUPER UGLY CODE AHEAD

def autocorrect(word: str, word_list: list[str], tolerance: float = 0.6) -> str:
    # Returns autocorrected word from the word_list
    # If no match is found, returns the original word
    # Lower tolerance = more strict
    
    for filter_word in word_list:
        if SequenceMatcher(a=word, b=filter_word).ratio() > tolerance:
            return filter_word
    return word


def get_path():
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.DirDialog(None, 'Open', style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path


def getpass(prompt='', max_length=None):
    p_s = ''
    proxy_string = ['​'] * max_length
    while True:
        sys.stdout.write('\x0D' + prompt + ''.join(proxy_string))
        c = msvcrt.getch()
        if c == b'\x03': # Ctrl-C
            raise KeyboardInterrupt
        if c == b'\r': # Enter
            break
        elif c == b'\x08': # Backspace
            p_s = p_s[:-1]
            proxy_string[len(p_s)] = " "
        else:
            proxy_string[len(p_s)] = "*"
            p_s += c.decode()
    sys.stdout.write('\n')
    return p_s


def projects_setup():
    config = {"projects": {}}

    print("\r" + fc.LIGHTWHITE_EX +
          "Which programming languages do you work with?")
    print(fc.LIGHTBLACK_EX + "Seperate multiple answers with a comma (,)\n")

    languages_supported = ['Python', 'C++',
                           'C#', 'Java', 'Go', 'Rust', 'Node.js', 'TypeScript', 'Web', 'Other']

    for i in languages_supported:
        if i == 'Web':
            print(f'{fc.LIGHTBLACK_EX}•{fc.LIGHTBLUE_EX} {i} (HTML + CSS)')
            continue
        print(f"{fc.LIGHTBLACK_EX}•{fc.LIGHTBLUE_EX} {i}")
        sleep(0.05)
    print()

    languages_wanted = [i.lower().strip() for i in input(
        fc.CYAN + "» " + fc.GREEN).split(",")]
    print(fc.RESET)

    languages_got = []

    for lang in languages_wanted:
        i = autocorrect(lang, languages_supported, 0.4)

        # Abbreviations
        if lang == 'css' or lang == 'html':
            i = 'Web'
        if lang == 'js' or lang == 'javascript':
            i = 'Node.js'
        if lang == 'ts':
            i = 'TypeScript'
        if lang == 'py':
            i = 'Python'
        if lang == 'go':
            i = 'Go'
        if lang == 'rs':
            i = 'Rust'
        if lang == 'cpp':
            i = 'C++'

        if i in languages_supported:
            languages_got.append(i)

    languages_got = list(set(languages_got))

    if languages_got == ['Other']:
        print("\r" + fc.LIGHTWHITE_EX +
              "What programming language do you work with?")
        selection = input(fc.CYAN + "» " + fc.GREEN)
        languages_got = [selection]

    if not languages_got:
        print(fc.LIGHTRED_EX + "Whoops!")
        print("Looks like we don't support any of those languages.")
        print("Here, have a cookie: 🍪\n")
        print('You can help us by adding it to the list of supported languages.')
        print(f'{fc.BLUE}https://www.github.com/Yasho022/pycmd/issues/new')
        exit(1)

    else:
        print(fc.GREEN + ', '.join(languages_got))

    print(fc.LIGHTWHITE_EX + "\nDo you organize your projects in folders? (Y/n)")
    print(fc.CYAN + "» " + fc.CYAN, end='')
    key = msvcrt.getch()

    if key == b"y":
        print('\r' + fc.CYAN + f"» {fc.GREEN}Yes")
        print(fc.GREEN + "\nAwesome! Let's set up your project folders.")
        print(fc.LIGHTBLACK_EX + "─" * 58)
        print(fc.LIGHTBLACK_EX +
              "Select the folder from the folder input dialog\n(maybe it's already open but not in focus)")

        try:
            for i in languages_got:
                print(fc.LIGHTWHITE_EX +
                      f"\nWhere do you save all your {i} projects?")
                print(fc.CYAN + "» " + fc.GREEN, end="\r")
                path = get_path()
                print(fc.CYAN + "» " + fc.GREEN + path)
                config['projects'][f'{i.lower()}_projects_path'] = path
        except:
            print(fc.CYAN + "» " +
                  fc.RED + "You didn't select a folder :/")
            exit(1)
            
    elif key == b"\x03":
        raise KeyboardInterrupt

    else:
        print('\r' + fc.CYAN + f"» {fc.RED}No")
        print("\nAlright! We'll create the folders for you.")
        print(fc.LIGHTBLACK_EX +
              "Select the folder from the folder input dialog\n(maybe it's already open but not in focus)")
        print(fc.LIGHTWHITE_EX +
              "\nAlright, just tell us your root folder where you save all your projects.")
        print(fc.CYAN + "» " + fc.GREEN, end="\r")
        root_folder = get_path()

        if root_folder is None:
            print(fc.CYAN + "» " + fc.RED + "No folder selected :/")
            print(
                fc.GREEN + "\nHmm... we'll just use the PYCMD/Projects directory.")
            print(fc.LIGHTWHITE_EX +
                  "\nIf you're okay with that, press [Y] to continue.")
            key = msvcrt.getch()
            
            if key == b'y':
                os.mkdir('Projects')
                root_folder = os.path.abspath('Projects')
            elif key == b'\x03':
                raise KeyboardInterrupt
            else:
                print(fc.RED + "Sorry, we can't continue without a root folder.")
                exit(1)

        print(fc.CYAN + "» " + fc.GREEN + root_folder + '\n')
        for i in languages_got:

            folder = os.path.join(root_folder, i)

            try:
                os.mkdir(folder)
                
            except FileExistsError:
                pass

            config['projects'][f'{i.lower()}_projects_path'] = folder

            print(
                f"{fc.MAGENTA}Created folder for {fc.YELLOW}{i} Projects{fc.LIGHTBLACK_EX}:{fc.RESET} {folder}")
        
    save_to_json(config)
    return config


def git_setup():
    
    print("\n" + fc.GREEN + "GIT Setup\n")

    print('\nThis is so PYCMD can initialize and delete git repositories.\n')
    print(
        f"Get your GitHub token from {fc.BLUE}https://github.com/settings/tokens/new")
    print("and give it the following scopes:\n")

    scopes = {'repo': ['repo:status', 'repo_deployment', 'public_repo',
                       'repo:invite', 'security_events'], 'delete_repo': ['All']}

    for i in scopes:
        print(
            f"{fc.LIGHTBLACK_EX}•{fc.LIGHTBLUE_EX} {i}{fc.LIGHTBLACK_EX}: {fc.GREEN}{', '.join(scopes[i])}")
    print('\nSet the expiration date to atleast a month or you will be asked to re-authenticate.')
    print('You can also do this in the .env file.')
    print('\n' + fc.LIGHTWHITE_EX + "Press [Y] to continue.", end="")
    key = msvcrt.getch()

    if key != b'n' and key != b'\x03':
        print(fc.LIGHTWHITE_EX + '\rEnter your GitHub token?')

        length_valid = False
        
        while not length_valid:
            try:
                github_token = getpass(fc.CYAN + "» " + fc.GREEN, 40)
            except IndexError:
                print(fc.RED + '\nToken length must be not more than 40 characters.')
            else:
                length_valid = True

        del length_valid

        token_valid = requests.head(
            f'https://api.github.com/', headers={
                'Authorization': f'token {github_token}',
            }).status_code == 200

        if token_valid:
            print(
                fc.GREEN + '\nGreat! We\'ll use this token to authenticate with GitHub.\n')
            dotenv.set_key(dotenv.find_dotenv(), 'GITHUB_TOKEN', github_token)
            return
        else:
            print('\n' + fc.RED + 'Invalid token. Git Setup Incomplete')
    
    else:
        print(fc.RED + '\rGit Setup Incomplete')

def editor_setup():
    
    config = {'text-editor': ''}
    
    print('\n' + fc.CYAN + 'Editor Setup\n')
    print(fc.LIGHTWHITE_EX + '\nWhat is your preferred text editor?\n')
    
    editors_available = ['Vim', 'GNU Nano', 'GNU Emacs',
                         'Visual Studio Code', 'Sublime Text', 'Atom', 'Other']
    
    for i in editors_available:
        print(f'{fc.LIGHTBLACK_EX}•{fc.LIGHTBLUE_EX} {i}')

    editor = input(f'\n{fc.CYAN}» {fc.GREEN}')
    editor = autocorrect(editor, editors_available, 0.4)
    editor = 'Visual Studio Code' if 'code' in editor else editor

    print('\n' + editor)

    if editor == 'Other' or editor not in editors_available:
        print('\nSorry we don\'t support any other text-editors or IDE at the moment.')
        print('Here, Have a Potato: 🥔 (oh wait lemme cook it for you) 🔥🥔🔥')
        print('Here, 🍠')
        exit(1)

    config['text-editor'] = editor
    
    save_to_json(config)
    return config


def save_to_json(config):
    json_location = os.path.abspath('json/config.json')

    with open(json_location, 'r') as f:
        data = json.load(f)
        f.close()

    data.update(config)

    with open(json_location, 'w') as f:
        json.dump(data, f, indent=4)
        f.close()


# <-- MAIN PART --> (or I should say "clean part")

try:

    if "projects" in sys.argv:
        projects_setup()
        print('\n' + fc.CYAN + 'Setup complete!')

    elif "git" in sys.argv:
        git_setup()
        print('\n' + fc.CYAN + 'Setup complete!')

    elif 'editor' in sys.argv:
        editor_setup()
        print('\n' + fc.CYAN + 'Setup complete!')

    else:
        print(f"\n\n{fc.CYAN}PYCMD Setup")

        print(dedent(f"""
        This script will help you to setup your PYCMD environment.
        It saves your configuration in "config.json" in the json directory. 

        After you have finished the setup, run `pycmd --help`
        to get the list of commands and usage.    

        You can change these settings anytime.

        {fc.LIGHTBLACK_EX}Ctrl^C to exit.
        """))

        print("── Press any key to continue ──", end="\r")
        if msvcrt.getch() == b'\x03':
            raise KeyboardInterrupt

        projects_setup()
        editor_setup()
        git_setup()
        
        save_to_json({"is_setup": True})
        
        print('\n' + fc.CYAN + 'Setup complete!')
        print('\n' + fc.GREEN + "We've saved everything to the config ;)")
        print("Here, have some bread: 🍞👍")

except KeyboardInterrupt:
    print(fc.LIGHTRED_EX + '\n\nSetup cancelled.')
    exit(1)
