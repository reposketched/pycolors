"""
pyansicolor.main
=============

Defines constants and functions for ANSI 24-bit (True Color) terminal coloring.

Note:
    These functions work only on terminals that support ANSI escape codes.
"""

def ANSI_start(r: float, g: float, b: float) -> str:
    """
    Return the ANSI escape code for a 24-bit foreground color.

    Args:
        r (float): Red component (0-255).
        g (float): Green component (0-255).
        b (float): Blue component (0-255).

    Returns:
        str: ANSI escape sequence for the foreground color.
    """
    return f"\033[38;2;{r};{g};{b}m"

def ANSI_background(r: float, g: float, b: float) -> str:
    """
    Return the ANSI escape code for a 24-bit background color.

    Args:
        r (float): Red component (0-255).
        g (float): Green component (0-255).
        b (float): Blue component (0-255).

    Returns:
        str: ANSI escape sequence for the background color.
    """
    return f"\033[48;2;{r};{g};{b}m"

ANSI_RESET = "\033[0m"
"""ANSI escape code to reset all styles and colors."""

ANSI_BOLD = "\033[1m"
"""ANSI escape code to apply bold styling."""

ANSI_UNDERLINE = "\033[4m"
"""ANSI escape code to apply underline styling."""

ANSI_REVERSE = "\033[7m"
"""ANSI escape code to apply reverse video styling."""

ANSI_END = ANSI_RESET
"""Alias for ANSI_RESET."""

def colored(text: str, r: float, g: float, b: float, reset: bool = True) -> str:
    """
    Color the given text using a 24-bit foreground color.

    Args:
        text (str): The text to color.
        r (float): Red component (0-255).
        g (float): Green component (0-255).
        b (float): Blue component (0-255).
        reset (bool): Whether to append the reset code after the text.

    Returns:
        str: The colorized text string.
    """
    s: str = ANSI_start(r, g, b) + text
    if reset:
        s += ANSI_RESET
    return s

def ncolored(text: str, color: tuple[float, float, float]) -> str:
    """
    Color the text using an RGB tuple.

    Args:
        text (str): The text to color.
        color (tuple): A (r, g, b) tuple.

    Returns:
        str: Colorized text.
    """
    r, g, b = color
    return colored(text, r, g, b)

def background(text: str, r: float, g: float, b: float, reset: bool = True) -> str:
    """
    Color the background of text using a 24-bit color.

    Args:
        text (str): The text to apply background color to.
        r (float): Red component.
        g (float): Green component.
        b (float): Blue component.
        reset (bool): Whether to append reset after text.

    Returns:
        str: The text with background color applied.
    """
    s = ANSI_background(r, g, b) + text
    if reset:
        s += ANSI_RESET
    return s

def nbackground(text: str, color: tuple[float, float, float]) -> str:
    """
    Apply background color using RGB tuple.

    Args:
        text (str): Text to color.
        color (tuple): (r, g, b) background color.

    Returns:
        str: Text with background color.
    """
    r, g, b = color
    return background(text, r, g, b)

def colorize(text: str, fg: tuple[float, float, float], bg: tuple[float, float, float] = None) -> str:
    """
    Apply both foreground and (optional) background color.

    Args:
        text (str): The text to colorize.
        fg (tuple): (r, g, b) foreground color.
        bg (tuple, optional): (r, g, b) background color.

    Returns:
        str: The fully colorized text.
    """
    parts = [ANSI_start(*fg)]
    if bg:
        parts.append(ANSI_background(*bg))
    parts.append(text)
    parts.append(ANSI_RESET)
    return ''.join(parts)

def styled(text: str, r, g, b, bold=False, underline=False, reverse=False, reset=True):
    """
    Apply color and multiple text styles.

    Args:
        text (str): Text to style.
        r (float): Red component.
        g (float): Green component.
        b (float): Blue component.
        bold (bool): Whether to bold the text.
        underline (bool): Whether to underline the text.
        reverse (bool): Whether to reverse the video.
        reset (bool): Whether to append reset after text.

    Returns:
        str: Styled text.
    """
    style = ANSI_start(r, g, b)
    if bold:
        style += ANSI_BOLD
    if underline:
        style += ANSI_UNDERLINE
    if reverse:
        style += ANSI_REVERSE
    styled_text = style + text
    if reset:
        styled_text += ANSI_RESET
    return styled_text

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """
    Convert hex color string (e.g. "#FF0000") to RGB tuple.

    Args:
        hex_color (str): Hex color string.

    Returns:
        tuple[int, int, int]: RGB values.
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def hex_colored(text: str, hex_color: str) -> str:
    """
    Color text using a hex color code.

    Args:
        text (str): Text to color.
        hex_color (str): Hex code (e.g., "#00FF00").

    Returns:
        str: Colorized text.
    """
    r, g, b = hex_to_rgb(hex_color)
    return colored(text, r, g, b)

def reset():
    """
    Print the ANSI reset code to the terminal.
    """
    print(ANSI_RESET)

def bold(text: str) -> str:
    """
    Apply bold style to text.

    Args:
        text (str): Text to bold.

    Returns:
        str: Bold text.
    """
    return ANSI_BOLD + text + ANSI_RESET

def underline(text: str) -> str:
    """
    Underline the given text.

    Args:
        text (str): Text to underline.

    Returns:
        str: Underlined text.
    """
    return ANSI_UNDERLINE + text + ANSI_RESET

def reverse(text: str) -> str:
    """
    Reverse the foreground and background of the text.

    Args:
        text (str): Text to reverse.

    Returns:
        str: Reversed text.
    """
    return ANSI_REVERSE + text + ANSI_RESET

# Common color constants (RGB tuples)
black       = (0, 0, 0)
white       = (255, 255, 255)
red         = (255, 0, 0)
lime        = (0, 255, 0)
blue        = (0, 0, 255)
yellow      = (255, 255, 0)
cyan        = (0, 255, 255)
magenta     = (255, 0, 255)
gray        = (128, 128, 128)
dark_gray   = (64, 64, 64)
light_gray  = (192, 192, 192)
orange      = (255, 165, 0)
brown       = (165, 42, 42)
pink        = (255, 192, 203)
purple      = (128, 0, 128)
olive       = (128, 128, 0)
teal        = (0, 128, 128)
navy        = (0, 0, 128)
gold        = (255, 215, 0)
sky_blue    = (135, 206, 235)
coral       = (255, 127, 80)
salmon      = (250, 128, 114)
mint        = (189, 252, 201)
indigo      = (75, 0, 130)
