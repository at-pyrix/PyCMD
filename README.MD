<h1 align=center> PyCMD - A CLI tool</h1>

## ToDo:
- Add the `rm` command
- Add the `ren` command
- Add the `ls` command
- Update `readme`

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

**PyCmd is a command-line interface tool to help you manage your projects. It saves you a lot of clicks. If that sounds interesting, [Setup PyCMD](#installation)**


### Why PyCMD?

PYCMD helps you create, manage and do cool stuff your projects super-fast ⚡

**Here's how things are faster with PYCMD**
  <!-- TODO: SHOW COMPARISION WITH GIF -->


PYCMD only supports `Windows` at the moment.<br>

[*Or if you're smart you can make it work on unix platforms ;​)*](https://www.github.com/Yasho022/Pycmd/fork)

## Installation:
- Clone the repo:

  ```console
  git clone https://www.github.com/Yasho/PyCMD.git
  ```
- Install the dependencies:

  ```console
  pip install -r requirements.txt
  ```
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

- Run the `pycmd setup` command and follow the on-screen instructions.

  ```console
  pycmd setup
  ```
### Requirements
- [Python 3+ (Tested on 3.9.9)](https://www.python.org/downloads/)
- [Windows](https://www.microsoft.com/en-in/windows)
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/downloads)
- [VS Code](https://code.visualstudio.com/download)

## Commands

| Command | Description |
|---------|-------------|
| `pycmd` | Run the PyCMD command line interface. |
| `pycmd help` | Display help information. |
| `pycmd setup` | Setup PyCMD. |
| `pycmd ls` | List all projects. |
| `pycmd open` | Open a project. |
| `pycmd rm` | Remove a project. |
| `pycmd create` | Create a new project + initialize a Git repository. |

## Usage

Use `pycmd` to run the command line interface.

Usage:
```console
$ pycmd <command> <parameter> --<flags> 
```

Example:
```powershell
pycmd create hello_world.py -private -y
# Creates a new python project
```

## Contribute 💖

#### How do I contribute?
Thank you kind person for contributing to PyCMD. You're awesome! ;​)
<!-- btw this (`​`) is zero-width space -->

Here are some ways you can help:

- [x]  Readme
- [ ] Update CLI help command
- [ ] Make it work on other platforms
- [ ] Other Language Support
- [ ] New Commands
- [ ] Simplify Commands
- [ ] `PYCMD Update` command which will merge the changes of a new release into your current branch. 

pls tell me about bugs in the code. I don't even use light mode.


### Contributers:
. 　　　。　　　　•　 　ﾟ　　。 　　.<br>

.　　 。　　　　　  。 . 　　 • 　　　　•<br>

 . Hey look, you could be the first one!　 。<br>

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
> ren bin/pycmd.cmd nevergonnagiveyouup.cmd
> ```
> However, this will only change the name to use PYCMD, all the commands will still use the `PyCMD` name.
---

*inspired by npm and heroku cli*

