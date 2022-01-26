# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2022 Mitchell Isaac Parker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import numpy as np
import matplotlib as mpl
import seaborn as sns

from .table import *
from .lst import *

white_hex = "#ffffff"
black_hex = "#000000"

blue_hex = "#1f77b4"
orange_hex = "#ff7f0e"
green_hex = "#2ca02c"
red_hex = "#d62728"
purple_hex = "#9467bd"
brown_hex = "#8c564b"
pink_hex = "#e377c2"
gray_hex = "#7f7f7f"
olive_hex = "#bcbd22"
cyan_hex = "#17becf"

light_blue_hex = "#aec7e8"
light_orange_hex = "#ffbb78"
light_green_hex = "#98df8a"
light_red_hex = "#ff9896"
light_purple_hex = "#c5b0d5"
light_brown_hex = "#c49c94"
light_pink_hex = "#f7b6d2"
light_gray_hex = "#c7c7c7"
light_olive_hex = "#dbdb8d"
light_cyan_hex = "#9edae5"

rama_color_dict = {"A": "#e78ac3", "B": "#8da0cb", "L": "#fc8d62", "E": "#66c2a5"}


def change_hex_alpha(hex_color, alpha):

    return tuple((1.0 - alpha) + np.array(mpl.colors.hex2color(hex_color)) * alpha)


def get_palette_hex_lst(palette, total=None):

    if total is None:
        palette = sns.color_palette(palette)
    else:
        palette = sns.color_palette(palette, total)

    hex_lst = palette.as_hex()

    return hex_lst


def get_hex(color):

    return mpl.colors.to_hex(color)


def get_rgb(color):

    return mpl.colors.to_rgb(color)


def get_hex_lst(color_lst):

    for idx, color in enumerate(color_lst):
        color_lst[idx] = get_hex(color)

    return color_lst


def get_rgb_lst(color_lst):

    for idx, color in enumerate(color_lst):
        color_lst[idx] = get_rgb(color)

    return color_lst


def get_lst_colors(
    label_lst,
    palette=None,
    return_rgb=False,
    return_dict=False,
    alpha=None,
):

    if type(palette) != dict:
        total = len(label_lst)

        if palette is None:

            if total <= 10:

                color_lst = get_palette_hex_lst("tab10")

            elif total <= 20:

                color_lst = get_palette_hex_lst("tab20")

            elif total <= 40:

                color_lst_1 = get_palette_hex_lst("tab20c")
                color_lst_2 = get_palette_hex_lst("tab20b")
                color_lst = color_lst_1 + color_lst_2

            elif total > 40:

                color_lst = get_palette_hex_lst("rainbow", total)

        else:
            if type(palette) == str:
                color_lst = get_palette_hex_lst(palette, total)
            else:
                color_lst = get_hex_lst(palette)

        colors = color_lst[:total]

        if "Noise" in label_lst or "None" in label_lst:
            label_lst = move_end_lst(label_lst, ["Noise", "None"])

            colors[-1] = gray_hex

            if "Noise" in label_lst and "None" in label_lst:
                colors[-2] = gray_hex

        if alpha is not None:
            colors = [change_hex_alpha(x, alpha) for x in colors]

        if return_rgb is True:
            colors = get_rgb_lst(colors)

        if return_dict is True:
            colors = make_dict(label_lst, colors)
    else:
        colors = palette

    return colors
