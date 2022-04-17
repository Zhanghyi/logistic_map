import numpy as np
from PIL import Image
from logistic import logistic

x0 = 0.4
u = 4

if __name__ == '__main__':
    im = Image.open('images/original_image.png', 'r')
    width, height = im.size
    num_pixels = width * height
    # pos 每个像素转换之后的位置
    pos = [0] * num_pixels
    # taken 该位置是否被占据
    taken = [False] * num_pixels
    xk = x0
    for i in range(num_pixels):
        xk = logistic(xk, u)
        real_pos = int(xk * num_pixels)
        while taken[real_pos]:
            xk = logistic(xk, u)
            real_pos = int(xk * num_pixels)
        pos[i] = real_pos
        taken[real_pos] = True

    old_arr = np.asarray(im)
    new_arr = np.copy(old_arr)

    for i in range(height):
        for j in range(width):
            x = int(pos[width * i + j] / width)
            y = pos[width * i + j] % width
            new_arr[i][j] = old_arr[x][y]

    new_image = Image.fromarray(new_arr)
    new_image.save('images/encrypted_image.png')
