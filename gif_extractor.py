from PIL import Image
import os
import sys

gifFileName = sys.argv[1]
try:
    im = Image.open(gifFileName)
    pngDir = gifFileName[:-4]
    if not os.path.isdir(pngDir):
        os.mkdir(pngDir)
    try:
        while True:
            current = im.tell()
            im.save(os.path.join(pngDir, 'slice_'+str(current) + '.png'))
            im.seek(current + 1)
    except EOFError:
        pass
except IOError:
    print(gifFileName, ' not found')
