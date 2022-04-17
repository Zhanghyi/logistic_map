import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def hist(input_file, output_file):
    img = Image.open(input_file).convert('L')
    img = np.array(img, 'f')
    plt.hist(img.ravel(), 256, [0, 256])
    plt.savefig(output_file)


if __name__ == '__main__':
    hist('images/original_image.png', 'images/original_hist.png')
    hist('images/encrypted_image.png', 'images/encrypted_hist.png')
