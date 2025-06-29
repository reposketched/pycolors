#test file
import pycolors

def test_colored_basic():
    result = pycolors.colored("test", 255, 0, 0)
    assert "\033[38;2;255;0;0mtest\033[0m" == result

def test_background_basic():
    result = pycolors.background("test", 0, 255, 0)
    assert "\033[48;2;0;255;0mtest\033[0m" == result

def test_hex_to_rgb():
    assert pycolors.hex_to_rgb("#FF0000") == (255, 0, 0)
    assert pycolors.hex_to_rgb("#00FF00") == (0, 255, 0)
    assert pycolors.hex_to_rgb("#0000FF") == (0, 0, 255)

def test_hex_colored():
    result = pycolors.hex_colored("test", "#00FF00")
    assert "\033[38;2;0;255;0mtest\033[0m" == result

def test_bold():
    assert pycolors.bold("test") == "\033[1mtest\033[0m"

def test_underline():
    assert pycolors.underline("test") == "\033[4mtest\033[0m"

def test_reverse():
    assert pycolors.reverse("test") == "\033[7mtest\033[0m"

def test_color_constants():
    assert pycolors.red == (255, 0, 0)
    assert pycolors.navy == (0, 0, 128)
    assert pycolors.gold == (255, 215, 0)

if __name__ == "__main__":
    try:
        test_colored_basic()
        test_background_basic()
        test_hex_to_rgb()
        test_hex_colored()
        test_bold()
        test_underline()
        test_reverse()
        test_color_constants()
    except AssertionError as e:
        raise Exception("AssertionError: test failed at {e}".format(e=e))