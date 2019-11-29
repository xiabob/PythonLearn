# _*_ coding:utf-8 _*_

import os
from PIL import Image
import shutil
import sys


def convert_image(source_dir, image_type):
    out_path = source_dir + "_" + image_type
    if not os.path.exists(out_path):
        os.mkdir(out_path)

    files = []
    image_list = os.listdir(source_dir)
    files = [os.path.join(source_dir, _) for _ in image_list]
    for index, origin_image in enumerate(files):
        try:
            image = Image.open(origin_image)
            w, h = image.size
            limit_size = min(w, h)
            # left, upper, right, lower
            box = ((w - limit_size) / 2, (h - limit_size) / 2, (w + limit_size) / 2, (h + limit_size) / 2)
            out_image = image.resize((limit_size, limit_size), Image.NEAREST, box)  # resize
            out_image = out_image.resize((328, 328))
            origin_full_name = os.path.split(origin_image)[-1]
            origin_name = os.path.splitext(origin_full_name)[0]
            out_image_path = out_path + "/" + origin_name + "." + image_type
            out_image.save(out_image_path)  # change image format
        except IOError as e:
            print(e)

source_dir = "/Users/xia/Downloads/Icon/genre"
convert_image(source_dir, "png")
print("xxx")