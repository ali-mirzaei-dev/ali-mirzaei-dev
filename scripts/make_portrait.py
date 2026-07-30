#!/usr/bin/env python3

import argparse
import sys

import cv2
import numpy as np
from PIL import Image
from rembg import remove

RAMP = " .`:-=+*cs#%@"

COLS = 90

CLAHE_CLIP = 3.0

GAMMA = 1.0

CURVE = 1.7

CROP_BOTTOM = 0.0

ROW_RATIO = 0.48

FG_LIGHT = "#6e7681"

FG_DARK = "#c9d1d9"

CHAR_W = 7.74

FONT_SIZE = 12.9

LINE_H = 15

ROW_DELAY = 0.09

FAMILY = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

def prep(path, crop=None):
    """Prepare the image for ASCII conversion."""

    src = Image.open(path).convert("RGBA")

    if crop:
        src = src.crop(crop)

    cut = remove(src)

    alpha = np.array(cut.split()[-1])

    white = Image.new("RGBA", cut.size, (255, 255, 255, 255))

    gray = np.array(Image.alpha_composite(white, cut).convert("L"))

    gray = cv2.bilateralFilter(gray, 11, 50, 50)

    gray = cv2.createCLAHE(
        clipLimit=CLAHE_CLIP,
        tileGridSize=(8, 8)
    ).apply(gray)

    gray = (255.0 * (gray / 255.0) ** CURVE).astype("uint8")

    gray[alpha < 20] = 255

    return Image.fromarray(gray)
