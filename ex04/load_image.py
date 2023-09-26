from PIL import Image


def zoom(img: Image.Image, coor: tuple, mode: str) -> Image.Image:
    """
    Zoom in on an image, and return the image.
    Image path.
    Coordinate as a tuple (left, upper, right, lower).
    Mode ("L", "RGB", "RGBA", "CMYK", "HSV", "1", "P", "LA").
    """
    left, upper, right, lower = coor
    if (left > right):
        print(f"Wrong! Left coordinate {left}, "
              f"is greater than right coordinate {right}.")
        return
    elif (upper > lower):
        print(f"Wrong! Upper coordinate {upper}, "
              f"is greater than lower coordinate {lower}.")
        return
    mode = mode.upper()
    valid_modes = ["L", "RGB", "RGBA", "CMYK", "HSV", "1", "P", "LA"]
    if mode not in valid_modes:
        print(f"Wrong mode '{mode}', "
              f"only the ones in this list {valid_modes}.")
        return
    sliced_img = img.crop(coor).convert(mode)
    width, height = sliced_img.size
    no_of_channel = len(sliced_img.getbands())
    print(f"The shape of image is: {(height, width, no_of_channel)}", end=" ")
    print(f"or {height, width}")
    result = "[["
    for index, item in enumerate(sliced_img.getdata()):
        if index == (len(sliced_img.getdata()) - 1):
            result += f"[{str(item)}]" + "]]"
        else:
            result += f"[{str(item)}]" + "\n  "
    print(result)
    return sliced_img
