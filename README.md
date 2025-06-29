# pycolors

A Python library for ANSI 24-bit (True Color) terminal coloring with a simple and intuitive API.

## Features

- **24-bit True Color Support**: Full RGB color support for modern terminals
- **Simple API**: Easy-to-use functions for coloring text and backgrounds
- **Multiple Styles**: Support for bold, underline, and reverse video
- **Hex Color Support**: Convert hex colors to RGB automatically
- **Predefined Colors**: Common color constants included
- **No Dependencies**: Pure Python with no external dependencies

## Installation

### From PyPI (when published)
```bash
pip install pycolors
```

### From Source
```bash
git clone https://github.com/yourusername/pycolors.git
cd pycolors
pip install -e .
```

## Quick Start

```python
from pycolors import colored, background, colorize, hex_colored

# Basic text coloring
print(colored("Hello, World!", 255, 0, 0))  # Red text
print(background("Hello, World!", 0, 255, 0))  # Green background

# Using hex colors
print(hex_colored("Hello, World!", "#FF0000"))  # Red text

# Combining foreground and background
print(colorize("Hello, World!", (255, 0, 0), (0, 255, 0)))  # Red text on green background
```

## Usage Examples

### Basic Coloring

```python
from pycolors import colored, background

# Color text with RGB values
red_text = colored("This is red text", 255, 0, 0)
blue_text = colored("This is blue text", 0, 0, 255)
print(red_text)
print(blue_text)

# Color background
red_bg = background("This has a red background", 255, 0, 0)
print(red_bg)
```

### Using Predefined Colors

```python
from pycolors import colored, red, blue, green, yellow

# Use predefined color constants
print(colored("Red text", *red))
print(colored("Blue text", *blue))
print(colored("Green text", *green))
print(colored("Yellow text", *yellow))
```

### Hex Colors

```python
from pycolors import hex_colored, hex_to_rgb

# Color text using hex codes
print(hex_colored("Purple text", "#800080"))
print(hex_colored("Orange text", "#FFA500"))

# Convert hex to RGB
rgb = hex_to_rgb("#FF0000")
print(f"Red in RGB: {rgb}")  # (255, 0, 0)
```

### Text Styling

```python
from pycolors import styled, bold, underline, reverse

# Apply multiple styles
styled_text = styled("Bold red text", 255, 0, 0, bold=True)
print(styled_text)

# Individual style functions
print(bold("Bold text"))
print(underline("Underlined text"))
print(reverse("Reversed text"))
```

### Advanced Usage

```python
from pycolors import colorize, ncolored, nbackground

# Using RGB tuples
color = (255, 165, 0)  # Orange
print(ncolored("Orange text", color))

# Background with RGB tuple
bg_color = (0, 0, 128)  # Navy
print(nbackground("Navy background", bg_color))

# Both foreground and background
print(colorize("Orange text on navy background", (255, 165, 0), (0, 0, 128)))
```

## Available Functions

### Core Functions
- `colored(text, r, g, b, reset=True)`: Color text with RGB values
- `background(text, r, g, b, reset=True)`: Color background with RGB values
- `colorize(text, fg, bg=None)`: Apply both foreground and background colors
- `styled(text, r, g, b, bold=False, underline=False, reverse=False, reset=True)`: Apply color and styles

### Utility Functions
- `hex_to_rgb(hex_color)`: Convert hex color to RGB tuple
- `hex_colored(text, hex_color)`: Color text using hex code
- `ncolored(text, color)`: Color text using RGB tuple
- `nbackground(text, color)`: Color background using RGB tuple

### Style Functions
- `bold(text)`: Apply bold style
- `underline(text)`: Apply underline style
- `reverse(text)`: Apply reverse video style
- `reset()`: Print ANSI reset code

### Constants
- `ANSI_RESET`, `ANSI_BOLD`, `ANSI_UNDERLINE`, `ANSI_REVERSE`: ANSI escape codes
- Predefined color tuples: `red`, `blue`, `green`, `yellow`, `cyan`, `magenta`, etc.

## Terminal Compatibility

This library works on terminals that support ANSI escape codes, including:
- Most modern Unix/Linux terminals
- Windows 10+ with Windows Terminal
- macOS Terminal
- VS Code integrated terminal
- Most SSH sessions

## Development

### Setup Development Environment
```bash
git clone https://github.com/yourusername/pycolors.git
cd pycolors
pip install -e ".[dev]"
```

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black .
flake8 .
mypy .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog

### 1.0.0
- Initial release
- 24-bit True Color support
- Basic and advanced coloring functions
- Hex color support
- Text styling capabilities
- Predefined color constants 