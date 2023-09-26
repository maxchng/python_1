from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom(img: Image.Image, coor: tuple, mode: str) -> str:
    """
    Zoom in on an image, and save a new image file called new_image.jpeg.
    Image path.
    Coordinate as a tuple (left, upper, right, lower).
    Mode ("L", "RGB", "RGBA", "CMYK", "HSV", "1", "P", "LA").
    """
    left, upper, right, lower = coor
    if (left > right):
        return (f"Wrong! Left coordinate {left}, "
                f"is greater than right coordinate {right}.")
    elif (upper > lower):
        return (f"Wrong! Upper coordinate {upper}, "
                f"is greater than lower coordinate {lower}.")
    mode = mode.upper()
    valid_modes = ["L", "RGB", "RGBA", "CMYK", "HSV", "1", "P", "LA"]
    if mode not in valid_modes:
        return (f"Wrong mode '{mode}', "
                f"only the ones in this list {valid_modes}.")
    sliced_img = img.crop(coor).convert(mode)
    plt.imshow(sliced_img)
    plt.savefig("new_image.jpeg")
    width, height = sliced_img.size
    no_of_channel = len(sliced_img.getbands())
    print(f"New shape after slicing: "
          f"{(height, width, no_of_channel)}", end=" ")
    print(f"or {height, width}")
    result = "[["
    for index, item in enumerate(sliced_img.getdata()):
        if index == (len(sliced_img.getdata()) - 1):
            result += f"[{str(item)}]" + "]]"
        else:
            result += f"[{str(item)}]" + "\n  "
    return result


if __name__ == "__main__":
    try:
        img = Image.open("animal.jpeg")
    except FileNotFoundError:
        print("Give me a proper path for an image!!")
    else:
        print(ft_load(img))
        print(zoom(img, (0, 0, 400, 400), "L"))
