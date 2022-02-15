import sys
import wx
from difflib import SequenceMatcher

def autocorrect(word: str, word_list: list[str], tolerance: float = 0.6, return_none=True) -> str:
    """
    ### Autocorrect
    Returns autocorrected `word` from the `word_list`.
    
    Returns `None` if no match found and `return_none` is `True` else returns `word`
    """
    
    for filter_word in word_list:
        if SequenceMatcher(a=word, b=filter_word).ratio() > tolerance:
            return filter_word
        
    return None if return_none else word 

def argparse(args: list=sys.argv):
    """
    ### Argument Parser
    Returns argument and flags from `sys.argv` or `args` list
    ```py
    return argument, flags
    ```
    """
    argument = ''
    flags = []
    for arg in args:
        if arg.startswith('-'):
            flags.append(arg)
        else:
            argument = arg
    return argument, flags

def get_path(prompt:str='Open'):
    """
    Get folder path by launching a popup dialog
    
    `prompt` is the title of the dialog
    """
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.DirDialog(None, prompt, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    
    return path

