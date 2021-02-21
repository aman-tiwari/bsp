from cld_steiner import rgb2line_steiner
from PIL import Image
from argparse import ArgumentParser
from multiprocessing import freeze_support
from time import time

args = ArgumentParser()
args.add_argument("-i", help="input")
args.add_argument("-o", help="output")


if __name__ == '__main__':
    freeze_support()
opts = args.parse_args()

img = Image.open(opts.i)
t0 = time()
for i in range(1):
    lines = rgb2line_steiner(img)

print(lines.keys())
import json
with open(opts.o, 'w') as f:
    f.write(json.dumps(lines))
    
t1 = time()
print("took:", (t1 - t0)/10.0, "s")

