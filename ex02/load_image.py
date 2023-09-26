from PIL import Image


def ft_load(path: str) -> str:
    """
    Print out the image shape and channels.
    Return the RGB value of each pixel.
    """
    try:
        img = Image.open(path)
    except FileNotFoundError:
        return "Give me a proper path for an image!!"
    else:
        width, height = img.size
        no_of_channel = len(img.getbands())
        print(f"The shape of the image is: {(height, width, no_of_channel)}")
        result = "[["
        for index, item in enumerate(img.getdata()):
            joined_str = " ".join(f"{i:2d}" for i in item)
            if index == (len(img.getdata()) - 1):
                result += f"[{joined_str}]" + "]]"
            else:
                result += f"[{joined_str}]" + "\n  "
        return result
