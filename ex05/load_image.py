from PIL import Image


def ft_load(path: str) -> list:
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print("Give a proper path for an Image!!")
    else:
        width, height = img.size
        no_of_channel = len(img.getbands())
        print(f"The shape of image is: {height, width, no_of_channel}")
        result = "[["
        for index, item in enumerate(img.getdata()):
            joined_str = " ".join(f"{i:2d}" for i in item)
            if index == (len(img.getdata()) - 1):
                result += f"[{joined_str}]" + "]]"
            else:
                result += f"[{joined_str}]" + "\n  "
        print(result)
        pixel = list(img.getdata())
        return pixel
