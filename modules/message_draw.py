import textwrap
from os import path
from pathlib import Path, PurePath

from PIL import Image, ImageDraw, ImageFont


def draw_message_image(text, title):
    bubble_padding = 50
    width = 1024
    height = 80 * (len(textwrap.wrap(text, 35)) + 2) + bubble_padding*2
    new_image = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype(path.join("fonts", "Roboto-Regular.ttf"), 50)

    draw.rounded_rectangle((bubble_padding,
                            bubble_padding,
                            width-bubble_padding,
                            height-bubble_padding), 25, fill="black")

    draw.text(xy=(100, 100),
              text=title,
              font=font,
              stroke_width=1,
              fill="#00bfff")

    line = 0
    for i in textwrap.wrap(text, 35):
        draw.text(xy=(100, 180+line*80),
                  text=i,
                  font=font)
        line += 1

    return new_image


draw_message_image("Helloworld!WorldisGood!Worldishello!", "Vasilyi Pupkin").show()
