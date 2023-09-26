from load_image import zoom
from PIL import Image
import matplotlib.pyplot as plt


def rotate(img: Image.Image):
    """
    Roate an image.
    x axis become y axis.
    y axis become x axis.
    Save it to a new image called new_image.jpeg
    """
    width, height = img.size
    transpose_img = Image.new(img.mode, (height, width))
    original_pixel = img.load()
    transpose_pixel = transpose_img.load()
    for x in range(width):
        for y in range(height):
            transpose_pixel[y, x] = original_pixel[x, y]
    plt.imshow(transpose_img)
    plt.savefig("new_image.jpeg")
    print(f"New shape after Transpose: {(width, height)}")
    pixel = list(img.getdata())
    result = "["
    for index, item in enumerate(pixel):
        if index % width == 0:
            if index != 0:
                result += "]\n "
            result += "["
        result += f"{item}"
        if (index + 1) % width != 0:
            result += " "
    result += "]]"
    return result


if __name__ == "__main__":
    try:
        img = Image.open("landscape.jpg")
    except FileNotFoundError:
        print("Give me a proper path for an image!!")
    else:
        return_img = zoom(img, (0, 0, 400, 400), "L")
        print(rotate(return_img))
