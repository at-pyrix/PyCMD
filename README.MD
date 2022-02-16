<h1 align=center> PyCMD - A CLI tool</h1>

## TODO:
- Add the `rm` command
- Add the `ren` command
- Add the `ls` command
- Make it linux compatible
- Publish to PyPI somehow

## Contents
- [About](#description)
  - [Why PyCMD?](#why-pycmd)
- [Setup](#installation)
  - [Requirements](#requirements)
- [PyCMD Commands](#commands)
- [Usage](#usage)
- [How can you help?](#contribute-)
  - [Contributers](#contributers)
- [License](#license-)
- [Frequently Asked Questions](#faqs)


## Description

PyCmd is a **command-line tool** to help you **manage** your **projects**. It saves you a lot of clicks. It's **simple** and **easy** to use.


### Why PyCMD?

PYCMD helps you create, manage and do cool stuff your projects super-fast ⚡

**Here's how fast things are with PYCMD**

![](https://github.com/Yasho022/PyCmd/blob/master/images/Comparision-low.gif?raw=true)


## Installation:
It is recommended to install PyCMD in the `~`(user) folder.
- ⬇️ Clone the repo:

  ```console
  cd ~
  git clone https://www.github.com/Yasho/PyCMD.git
  ```
- ⚙️ Add the `bin` folder to your `PATH` environment variable.: 

  *I had to make a batch file to get the abspath of the folder.*

  ```console
  cd pycmd
  ./add_to_path
  rm ./add_to_path.cmd
  ```
<!--
<ul><li>
<details>
  <summary>
    Add the <code>bin</code> folder to your <code>PATH</code> environment variable.
  </summary>

  - Search for `environment variables for your account` in the start menu.
  - Click on `Edit environment variables for your account`.
  - In the `User Variables`, Select `Path` and click `Edit`.

    ![](https://i2.paste.pics/FNOQY.png)
  - Click `New` and add the `pycmd/bin/` folder to the `Path`.

    ![](https://i2.paste.pics/FNOSK.png)
  - Click `OK`.
  - Restart your terminal.
</details>
</li>
</ul>
-->

- ⚒️ Install the requirements:

  ```console
  pip install -r requirements.txt
  ```
  
- 🔃 **Restart your terminal** for the changes to take effect

- ✅ Run the `pycmd setup` command and follow the on-screen instructions.

  ```console
  pycmd setup
  ```
### Requirements
- [Python 3+ (Tested on 3.9.9)](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/downloads)
- [Windows](https://www.microsoft.com/en-in/windows)

[*Or if you're smart you can make it work on unix platforms ;​)*](https://www.github.com/Yasho022/Pycmd/fork)

## Commands

| Command | Description |
|---------|-------------|
| `pycmd` | Run the PyCMD command line interface. |
| `pycmd help` | Display help information. |
| `pycmd version` | Display the version number. |
| `pycmd setup` | Setup PyCMD. |
| `pycmd ls` | List all projects. |
| `pycmd open` | Open a project. |
| `pycmd rm` | Remove a project. |
| `pycmd create` | Create a new project + initialize a Git repository. |

## Usage

Use `pycmd` to run the command line interface.

Usage:
```
$ pycmd <command> <parameter> --<flags> 
```

Example:
```powershell
pycmd create hello_world.py -private -y
# Creates a new python project
```

## Contribute 💖

#### How do I contribute?
Thank you  for contributing to PyCMD
<!-- btw this (`​`) is zero-width space -->

Here are some ways you can help:

- [x]  Readme
- [x] Update CLI help command
- [ ] Unix Support
- [ ] New Commands
- [ ] `PYCMD Update` command which will merge the changes of a new release into your current branch. 

pls tell me about bugs in the code. I don't even use light mode.


### Contributers:
. 　　　。　　　　•　 　ﾟ　　。 　　.<br>

.　　 。　　　　　  。 . 　　 • 　　　　•<br>

 . 　**Hey look, you could be the first one!**　 。<br>

　　ﾟ　　　.　　　. ,　　　　.　 .<br>
  .　　　 　　.　　　　　。　　 。　. 　


## License 🔑
PYCMD is licensed under the [MIT license](https://www.opensource.org/licenses/mit-license.php).

```license
MIT License

Copyright (c) 2022 Yasho022

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (PYCMD), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## FAQs:

- Why did you name it **Py**CMD? 
>  ¯\\_\(ツ\)\_\/¯, but I think it's an **ok** name. Also `Py` represents the Python language in which PYCMD was written. Not the best name, but okay. 

- How do you use PyCMD?
> You can use the `pycmd` command. It will help you to get started.

- Why should I use PyCMD?
> PyCMD saves you a lot of time, you can use it to manage your projects if they are messy or if you want to make a lot of changes in short time. Not only that but also it will help you to make your projects more readable and maintainable.

- What are the Pros and Cons of PyCMD?

> | Pros | Cons |
> | ---- | ---- |
> | Easy to use | Might be an overkill |
> | Saves Time | Compaitable with Windows only |
> | Generates Boiler Plate | |
> | Manages GIT | |
> | Light - Doesn't take too much space |


- Does PyCMD collect any user data?
> No, PyCMD doesn't collect any user data. It stores the configuration in a file `config.json`.

- How do you contribute to PyCMD?
> You can contribute to PyCMD by [opening an issue](https://www.github.com/Yasho022/PyCMD/issues) or [forking](https://www.github.com/Yasho022/PyCMD/fork). 

- But seriously, I don't like the name?
> You can change the name of `PyCMD` to something else by renaming the `pycmd.cmd` in the `bin` folder.
> Example:
> ```
> ren bin/pycmd.cmd bred.cmd
> ```
> However, this will only change the name to use PYCMD, all the commands will still use the `PyCMD` name.

---

### Developer notes:

If you encounter any problems feel free to [Contact me](#contact-me-)

*I heard that emojis attract attention, don't mind me, I hate them too. (i have an official rivalry towards yellow circles)*

*inspired by npm and heroku cli*

### Contact Me 💌
          
<a href = "mailto:wiredhack022@gmail.com" target="_blank">
<img src="https://img.shields.io/badge/wiredhack022@gmail.com-e9ff40?style=for-the-badge&amp;logo=gmail&amp;logoColor=black" alt="GMail">
</a>
<a href = "https://www.reddit.com/user/Yasho022" target="_blank">
 <img src="https://img.shields.io/badge/NotYasho-ff4803?style=for-the-badge&amp;logo=reddit&amp;logoColor=white" alt = "Reddit">