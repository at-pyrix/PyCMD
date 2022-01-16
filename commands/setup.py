from colorama import Fore as fc, Back as bk, Style as st, init
import wx
import os
import json
init(autoreset=True)



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


print(f"\n\n{fc.CYAN}PYCMD Setup")

print("""
This script will help you to setup your PYCMD environment.
It saves your configuration in "config.json" in the json directory. 

After you have finished the setup, run `pycmd --help`
to get the list of commands and usage.    

You can change these settings anytime.

""")

print(fc.LIGHTBLACK_EX + "(Seperate multiple answers with a comma)\n")
print(fc.LIGHTBLACK_EX + fc.LIGHTWHITE_EX +
      "Which programming language do you work with?")
languages_wanted = [i.strip() for i in input(
    fc.CYAN + "» " + fc.GREEN).split(",")]
print(fc.RESET)
languages_supported = ['Python', 'Java',
                       'HTML', 'Javascript', 'py', 'js', 'web']
languages_supported_lower = [i.lower() for i in languages_supported]

languages_got = []
for i in languages_wanted:
    if i.lower() in languages_supported_lower:
        if i.lower() == "py":
            languages_got.append("Python")
        elif i.lower() == "js":
            languages_got.append("Javascript")
        elif i.lower() == "web":
            languages_got.append("HTML + CSS")
        else:
            languages_got.append(i.title())

del languages_supported_lower

if not languages_got:
    print(fc.RED + "Hmm, looks like we don't support any of those languages.")
    print("Here, have a cookie: 🍪")
    print('You can help us by adding it to the list of supported languages.')
    print(f'{fc.BLUE}https://www.github.com/Yasho022/pycmd/issues/new')
    exit(0)

else:
    del languages_supported
    print(f'Wow! You got lucky!\nWe support {len(languages_got)} of the languages you wanted:'
          if (len(languages_got)) != len(languages_wanted)
          else f'You got the luck of a banana!\nWe support all of the languages you mentioned!')
    print(fc.GREEN + ', '.join(languages_got))

config = {}

print(fc.LIGHTWHITE_EX + "\nDo you organize your projects in folders? (Y/n)")
response = input(fc.CYAN + "» " + fc.RESET).lower()
if response == "y" or response == "yes":

    for language in languages_got:
        print(fc.LIGHTWHITE_EX +f"\nWhere do you save all your {language} projects?")
        print(fc.CYAN + "» " + fc.GREEN, end="\r")
        path = get_path()
        print(fc.CYAN + "» " + fc.GREEN + path)
        if language == "HTML + CSS": language = "web"
        config[f'{language.lower()}_projects_path'] = path

json_location = os.path.abspath('json/config.json')

with open(json_location, 'r') as f:
    data = json.load(f)
    
data.update(config)

with open(json_location, 'w') as f:
    json.dump(data, f, indent=4)

print(fc.GREEN + "Good Boi, you organize your projects in folders. Respect ++")
print(fc.CYAN + "Saved in " + fc.GREEN + json_location)