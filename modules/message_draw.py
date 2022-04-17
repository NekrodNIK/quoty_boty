import textwrap
from os import path
from pathlib import Path, PurePath

from PIL import Image, ImageDraw, ImageFont


def draw_message_image(text):
    new_image = Image.new("RGBA", (1500, 1000))
    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype(path.join("fonts", "Roboto-Regular.ttf"), 100)

    draw.rounded_rectangle((10, 10, 1490, 990), 100, fill="black")

    line = 0
    for i in textwrap.wrap(text, 30):
        draw.text((100, 100+line*100),
                  text=i,
                  font=font)
        line += 1

    return new_image


draw_message_image("Hello, World! Hello, World! Hello, World!").show()
