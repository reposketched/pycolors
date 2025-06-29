# test_pycolors.py
import pyansicolor

def test_colored_basic():
    result = pyansicolor.colored("test", 255, 0, 0)
    assert "\033[38;2;255;0;0mtest\033[0m" == result

def test_background_basic():
    result = pyansicolor.background("test", 0, 255, 0)
    assert "\033[48;2;0;255;0mtest\033[0m" == result

def test_hex_to_rgb():
    assert pyansicolor.hex_to_rgb("#FF0000") == (255, 0, 0)
    assert pyansicolor.hex_to_rgb("#00FF00") == (0, 255, 0)
    assert pyansicolor.hex_to_rgb("#0000FF") == (0, 0, 255)

def test_hex_colored():
    result = pyansicolor.hex_colored("test", "#00FF00")
    assert "\033[38;2;0;255;0mtest\033[0m" == result

def test_bold():
    assert pyansicolor.bold("test") == "\033[1mtest\033[0m"

def test_underline():
    assert pyansicolor.underline("test") == "\033[4mtest\033[0m"

def test_reverse():
    assert pyansicolor.reverse("test") == "\033[7mtest\033[0m"

def test_color_constants():
    assert pyansicolor.red == (255, 0, 0)
    assert pyansicolor.navy == (0, 0, 128)
    assert pyansicolor.gold == (255, 215, 0) 