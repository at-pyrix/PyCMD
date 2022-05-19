<h1 align=center> PyCMD - Manage your Projects</h1>

## Contents
- [About](#description)
  - [Why PyCMD?](#why-pycmd)
- [Setup](#installation)
  - [Manual Setup](#manual)
  - [Using pip](#pip)
  - [Requirements](#requirements)
- [PyCMD Commands](#commands)
- [Usage](#usage)
- [How can you help?](#contribute-)
  - [Contributers](#contributers)
- [License](#license-)
- [Frequently Asked Questions](#faqs)


## What is PyCMD?

PyCmd is a **command-line tool** to help you **manage** your **projects**. It saves you a lot of clicks. It's **simple** and **easy** to use. Interesting? [Give it a try](#installation)


### Why PyCMD?

PYCMD helps you create, manage and do cool stuff with your projects super-fast ⚡

**Here's how fast things are with PYCMD**

![](./images/Comparision-low.gif)

*kindly forgive me for the **forced "comedy"***


## Installation:

### Pip
```console
pip install pycmd-cli
pycmd setup
```
> Make sure you have the python `lib/site-packages` added to your `PATH`

### Manual

- ⬇️ Clone the repo:

  ```console
  git clone https://www.github.com/Yasho/PyCMD.git
  ```
- ```console
  cd pycmd
  pip install .
  ```

- ⚒️ Install the requirements:

  ```console
  pip install -r requirements.txt
  ```
  
- 🔃 **Restart your terminal** for the changes to take effect

- ✅ Run the `pycmd setup` command and follow the on-screen instructions.

  ```console
  pycmd setup
  ```

>  You can manually config the settings by editing the `config.json` file.
>  To do so, run:
>  ```console
>  pycmd src
>  ```
>  This will open the source code of pycmd. You can edit the config file located in `json/config.json` 


### Requirements
> ⚠️ Doesn't work on Python 3.10 yet
- [Python 3.6+ (Tested on 3.9.9)](https://www.python.org/downloads/) 
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/downloads)
- [Windows](https://www.microsoft.com/en-in/windows)

[*Or if you're smart you can make it work on unix platforms ;​)*](https://www.github.com/Yasho022/Pycmd/fork)

## Commands

| Command | Description |
|---------|-------------|
| `pycmd` | Run the PyCMD command line interface. |
| `pycmd help` | Display help information. |
| `pycmd setup` | Setup PyCMD. |
| `pycmd ls` | List all projects. (Including Github repositories) |
| `pycmd open` | Open a project. |
| `pycmd rm` | Remove a project. |
| `pycmd create` | Create a new project + initialize a Git repository. |
| `pycmd src` | View and edit the source code of PYCMD |

*It's okay if you misspell the commands, PYCMD will correct them ;​-)*

## Usage

Use `pycmd` to run the command line interface.<br>
*Really?*

**Usage:**
```
$ pycmd <command> <parameter> -<flags> 
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

*pls inform me about bugs in the code. i'll fix them as soon as possible*


### Contributers:
<!-- get a round image -->
[![](https://images.weserv.nl/?url=avatars.githubusercontent.com/u/58365481?s=50&v=4&mask=circle&fit=cover)](](https://github.com/Domin8668))


## License 🔑
PYCMD is licensed under the [MIT license](https://www.opensource.org/licenses/mit-license.php).

```license
MIT License

Copyright (c) 2022 Yasho

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
>  ¯\\_\(ツ\)\_\/¯, but I think it's an **ok** name. Also `Py` represents the Python language in which PYCMD was written. Not the best name, i'm bad at keeping names. 

- Why should I use PyCMD?
> PyCMD saves you a lot of time, you can use it to manage your projects if they are messy or if you want to make a lot of changes in short time. Not only that but also it will help you to make your projects more readable and maintainable.

- What are the Pros and Cons of PyCMD?

> | Pros | Cons |
> | ---- | ---- |
> | Easy to use | Might be an overkill |
> | Saves Time | Only compaitable with Windows currently |
> | Generates Boiler Plate | |
> | Easy to install/uninstall | |
> | Manages GIT | |
> | Light (Doesn't take too much space) |


- Where are the configs?
> All the configurations are stored in your local storage in the file `{pycmd-directory}/json/config.json`.
> You can run the command `pycmd src` to open the PyCMD folder with your text editor. You can edit the configs there itself.

- How do you contribute to PyCMD?
> You can contribute to PyCMD by [opening an issue](https://www.github.com/Yasho022/PyCMD/issues) or by a [pull request](https://www.github.com/Yasho022/PyCMD/fork). 

---

### Developer notes:

If you encounter any problems feel free to [Contact me](#contact-me-)

*I heard that emojis attract attention, that's why I used them. Really sorry if you hate them, I hate them too. (i too have an official rivalry towards those yellow circles)*

Inspired by npm and heroku cli

### Contact Me 💌
          
<a href = "mailto:probablynotyasho@gmail.com" target="_blank">
<img src="https://img.shields.io/badge/probablynotyasho@gmail.com-f5d742?style=for-the-badge&amp;logo=gmail&amp;logoColor=black" alt="Mail" title="Mail">
</a>
