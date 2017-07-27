#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from PIL import Image, ImageFilter

im = Image.open('pil_test.jpg');
w,h = im.size
print ('Original image size: %sx%s' % (w, h))
im2 = im.filter(ImageFilter.BLUR)
im2.save('pil_test_2.jpg')
print ('ImageFilter')
