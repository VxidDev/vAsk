import subprocess , os , re
from rich.console import Console

console = Console()

prompt_symboles = {
    "double-arrow": ">>",
    "single-arrow": ">",
    "bullet": "•",
    "dash": "-",
    "star": "*",
    "question-mark": "?",
    "hash": "#",
    "caret": "^",
    "tilde": "~",
    "pipe": "|"
}

styles = ["bold",
          "italic",
          "underline",              
          "bold_italic",
          "dim",
          "reverse",
          "blink",
          "strike"]

colors = [
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_black",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white"
]

class ArgumentError(Exception):
    # Custom exception for vAsk.
    pass

def Ask(question , allowed_answers=None , force_int=False , clear_terminal=False , case_sensetive=False , upper=False , lower=False , prompt_symbol=None , style=None ,  color=None):
    if upper and lower:
        raise ArgumentError("Both 'upper' and 'lower' arguments are True. Please use only only one.")
    elif (upper or lower) and force_int:
        if upper is True:
            invalid_argument = "upper"
        else:
            invalid_argument = "lower"
        raise ArgumentError(f"Cant use '{invalid_argument}' with 'force_int' argument!")
    
    if color is not None:
        color_clean = color.strip()
        if color_clean.lower() not in colors:
            if not re.match(r"^#[0-9a-fA-F]{6}$", color_clean):
                raise ArgumentError(f"{color_clean} not in supported colors. Documentation at 'https://github.com/VxidDev/vAsk'")

    if prompt_symbol is not None:
        prompt_symbol_splitted = prompt_symbol.split(maxsplit=1)
        if len(prompt_symbol_splitted) == 2:
            if prompt_symbol_splitted[0] == "custom":
                if prompt_symbol_splitted[1] == "":
                    raise ArgumentError("'prompt_symbol' cant be an empty string!")
                question += f"\n{prompt_symbol_splitted[1]}"
            else:
                raise ArgumentError("Invalid 'prompt_symbol' argument. Documentation at 'https://github.com/VxidDev/vAsk'")
        else:
            if prompt_symbol not in prompt_symboles.keys():
                raise ArgumentError("Unknown 'prompt_symbol' selection. Documentation at 'https://github.com/VxidDev/vAsk'")
            else:
                question += f"\n{prompt_symboles[prompt_symbol]}"
    
    if style is not None:
        styles_list = style.split()
        for style in styles_list:
            if style not in styles:
                raise ArgumentError("Invalid 'style' selection. Documentation at 'https://github.com/VxidDev/vAsk'")
        else:
            style_tag = " ".join(styles_list)
            if color is not None:
                style_tag += f" {color}"
            question = f"[{style_tag}]{question}[/{style_tag}]"
    else:
        if color is not None:
            question = f"[{color}]{question}[/{color}]"
                
    if clear_terminal:
        subprocess.run("cls" if os.name == "nt" else "clear")

    if allowed_answers is not None and force_int is not True:
        if case_sensetive is False:
            allowed_answers = [answer.lower() for answer in allowed_answers]
        user_input = None
        while user_input not in allowed_answers:
            if clear_terminal:
                subprocess.run("cls" if os.name == "nt" else "clear")
            console.print(question , end=" ")
            if case_sensetive:
                user_input = input()
            else:
                user_input = input().lower()

    elif force_int is True:
        while True:
            try:
                if clear_terminal:
                    subprocess.run("cls" if os.name == "nt" else "clear")
                console.print(question , end=" ")
                user_input = int(input())
                break
            except ValueError:
                print("Input must be a number!")
    
    else:
        console.print(question , end=" ")
        user_input = input()

    if lower:
        return user_input.lower()
    elif upper:
        return user_input.upper()
    else:
        return user_input