# vAsk

**vAsk** is a Python library that enhances the standard `input()` function with a rich set of features: styled prompts, colored text, validation, type enforcement, and custom prompt symbols. Perfect for CLI applications where you want interactive, user-friendly input.

---

## Features

- **Styled prompts:** Bold, italic, underline, blink, strike, reverse, dim, and combinations.
- **Custom colors:** Use named Rich colors or hex codes (`#RRGGBB`) for your prompts.
- **Prompt symbols:** Pre-made symbols like `>>`, `>`, `•`, `*`, `?` or fully custom symbols.
- **Validation:** Restrict input to a list of allowed answers.
- **Type enforcement:** Force integer input.
- **Case handling:** Automatically convert input to upper or lower case.
- **Terminal clearing:** Optionally clear terminal before asking input.

---

## Installation

Since `vAsk` is a library, simply clone the repo and use it in your scripts:

```bash
git clone https://github.com/YourUsername/vAsk.git
cd vAsk
pip install .
```

## Usage
```py
from vAsk import Ask

# Basic input
name = Ask("What's your name?")

# Styled and colored input
age = Ask(
    "How old are you?",
    style="bold italic",
    color="cyan",
    force_int=True
)

# Input with allowed answers
answer = Ask(
    "Do you like pizza?",
    allowed_answers=["yes", "no"],
    case_sensetive=False,
    prompt_symbol="double-arrow",
    style="underline",
    color="#FF5733"
)
```
### Parameters

| Argument          | Type | Description                                                            |
| ----------------- | ---- | ---------------------------------------------------------------------- |
| `question`        | str  | The prompt question text.                                              |
| `allowed_answers` | list | List of valid answers. Input will repeat until one is given.           |
| `force_int`       | bool | Converts input to integer; raises error on invalid input.              |
| `clear_terminal`  | bool | Clears the terminal before showing the prompt.                         |
| `case_sensetive`  | bool | Determines whether allowed_answers matching is case-sensitive.         |
| `upper`           | bool | Converts returned input to uppercase. Cannot be combined with `lower`. |
| `lower`           | bool | Converts returned input to lowercase. Cannot be combined with `upper`. |
| `prompt_symbol`   | str  | Pre-defined or custom prompt symbol shown before input.                |
| `style`           | str  | Rich style(s) to apply to the prompt text (e.g., `bold italic`).       |
| `color`           | str  | Named Rich color or hex code (`#RRGGBB`) for the prompt.               |

### Styles

| Style            | Description                                  |
| -----------------| -------------------------------------------- |
| `bold`           | Makes text bold.                             |
| `italic`         | Italicizes the text.                         |
| `underline`      | Underlines the text.                         |
| `bold_italic`    | Bold and italic combined.                    |
| `dim`            | Dims the text (less bright).                 |
| `reverse`        | Reverses foreground and background colors.   |
| `blink`          | Makes the text blink (if terminal supports). |
| `strike`         | Strikes through the text.                    |

Multiple styles can be combined: ```bold italic underline```

Works seamlessly with color as well.
 
### Prompt symbols
| Symbol            | Description        |   
| ----------------- | ------------------ |
| `double-arrow`    | `>>`               |   
| `single-arrow`    | `>`                |   
| `bullet`          | `•`                |   
| `dash`            | `-`                |   
| `star`            | `*`                |   
| `question-mark`   | `?`                |  
| `hash`            | `#`                |   
| `caret`           | `^`                |   
| `tilde`           | `~`                |   
| `custom <string>` | Your custom string |   

## Examples

Custom prompt and color:
```py
answer = Ask(
    "Does pineapple belong on pizza?",
    prompt_symbol="custom (Hint, no)>>",
    style="bold italic",
    color="#FF3E1C"
)
```
Integer input with terminal clearing:
```py
age = Ask("Enter your age:", force_int=True, clear_terminal=True)
```
Validated input:
```py
choice = Ask(
    "Choose yes or no:",
    allowed_answers=["yes", "no"],
    case_sensetive=False
)
```
### Exceptions
ArgumentError – Raised when invalid argument combinations or unsupported options are used.
