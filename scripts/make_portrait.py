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
