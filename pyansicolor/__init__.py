"""
pyansicolor
========

A Python library for ANSI 24-bit (True Color) terminal coloring.

This package provides functions and utilities for coloring terminal output
using ANSI escape codes with full 24-bit RGB color support.
"""

from .main import (
    # Core functions
    colored,
    background,
    colorize,
    styled,
    
    # Utility functions
    hex_to_rgb,
    hex_colored,
    ncolored,
    nbackground,
    
    # Style functions
    bold,
    underline,
    reverse,
    reset,
    
    # ANSI constants
    ANSI_RESET,
    ANSI_BOLD,
    ANSI_UNDERLINE,
    ANSI_REVERSE,
    ANSI_END,
    
    # Color constants
    black,
    white,
    red,
    lime,
    blue,
    yellow,
    cyan,
    magenta,
    gray,
    dark_gray,
    light_gray,
    orange,
    brown,
    pink,
    purple,
    olive,
    teal,
    navy,
    gold,
    sky_blue,
    coral,
    salmon,
    mint,
    indigo,
)

__version__ = "1.0.0"
__author__ = "Sooryashankar Joy"
__email__ = ""
__description__ = "A Python library for ANSI 24-bit (True Color) terminal coloring"

__all__ = [
    # Core functions
    "colored",
    "background", 
    "colorize",
    "styled",
    
    # Utility functions
    "hex_to_rgb",
    "hex_colored",
    "ncolored",
    "nbackground",
    
    # Style functions
    "bold",
    "underline",
    "reverse",
    "reset",
    
    # ANSI constants
    "ANSI_RESET",
    "ANSI_BOLD",
    "ANSI_UNDERLINE",
    "ANSI_REVERSE",
    "ANSI_END",
    
    # Color constants
    "black",
    "white",
    "red",
    "lime",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    "gray",
    "dark_gray",
    "light_gray",
    "orange",
    "brown",
    "pink",
    "purple",
    "olive",
    "teal",
    "navy",
    "gold",
    "sky_blue",
    "coral",
    "salmon",
    "mint",
    "indigo",
] 