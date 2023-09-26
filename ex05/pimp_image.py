from load_image import ft_load
from PIL import Image


def ft_invert(array) -> list:
    """Inverts the image."""
    if array is None:
        return None
    img = Image.open("landscape.jpg")
    width, height = img.size
    original_pixel = img.load()
    x, y = 0, 0
    for i in range(len(array)):
        r = 255 - array[i][0]
        g = 255 - array[i][1]
        b = 255 - array[i][2]
        original_pixel[x, y] = (r, g, b)
        x += 1
        if x == width:
            x = 0
            y += 1
    img.save("Inverted_image.jpg")
    pixel = list(img.getdata())
    return pixel


def ft_red(array) -> list:
    """Convert the image to red monochrome version."""
    if array is None:
        return None
    img = Image.open("landscape.jpg")
    width, height = img.size
    original_pixel = img.load()
    x, y = 0, 0
    for i in range(len(array)):
        r = array[i][0]
        g = 0
        b = 0
        original_pixel[x, y] = (r, g, b)
        x += 1
        if x == width:
            x = 0
            y += 1
    img.save("Red_image.jpg")
    pixel = list(img.getdata())
    return pixel


def ft_green(array) -> list:
    """Convert the image to green monochrome version."""
    if array is None:
        return None
    img = Image.open("landscape.jpg")
    width, height = img.size
    original_pixel = img.load()
    x, y = 0, 0
    for i in range(len(array)):
        r = 0
        g = array[i][1]
        b = 0
        original_pixel[x, y] = (r, g, b)
        x += 1
        if x == width:
            x = 0
            y += 1
    img.save("Green_image.jpg")
    pixel = list(img.getdata())
    return pixel


def ft_blue(array) -> list:
    """Convert the image to blue monochrome version."""
    if array is None:
        return None
    img = Image.open("landscape.jpg")
    width, height = img.size
    original_pixel = img.load()
    x, y = 0, 0
    for i in range(len(array)):
        r = 0
        g = 0
        b = array[i][2]
        original_pixel[x, y] = (r, g, b)
        x += 1
        if x == width:
            x = 0
            y += 1
    img.save("Blue_image.jpg")
    pixel = list(img.getdata())
    return pixel


def ft_grey(array) -> list:
    """Convert the image to grey monochrome version."""
    if array is None:
        return None
    img = Image.open("landscape.jpg")
    width, height = img.size
    original_pixel = img.load()
    x, y = 0, 0
    for y in range(height):
        for x in range(width):
            r, g, b = original_pixel[x, y]
            grey_value = (r + g + b) // 3
            original_pixel[x, y] = (grey_value, grey_value, grey_value)
    img.save("Grey_image.jpg")
    pixel = list(img.getdata())
    return pixel


if __name__ == "__main__":
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)
