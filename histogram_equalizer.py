from PIL import Image

def pxl_map_eq_hist(pxl_val, eq_map):
    return eq_map[pxl_val]

def equalize_map(histogram, size):
    #nk/n
    normalized_hist = list()
    for i in histogram:
        normalized = i/size
        normalized_hist.append(normalized)

    #gk
    acc_probability = list()
    total_sum = 0
    for i in normalized_hist:
        total_sum = total_sum + i
        acc_probability.append(total_sum)

    #round(gk*L)
    rounded = list()
    for i in acc_probability:
        equalized = round(i * 255)
        rounded.append(equalized)

    return rounded

def hist_equalize(image, histogram):
    height, width = image.size
    size = width * height
    map = equalize_map(histogram, size)
    new_image = image.point(lambda p : pxl_map_eq_hist(p, map))
    return new_image

def hist_equalize_rgb(image, histogram_r, histogram_b, histogram_g):
    height, width = image.size
    size = width * height
    map_r = equalize_map(histogram_r, size)
    map_b = equalize_map(histogram_b, size)
    map_g = equalize_map(histogram_g, size)

    new_image = Image.new(mode="RGB", size=(height, width))

    for i in range(0, height):
        for j in range(0, width):
            r, g, b = image.getpixel((i,j))
            new_image.putpixel((i,j), (pxl_map_eq_hist(r, map_r), pxl_map_eq_hist(g, map_g), pxl_map_eq_hist(b, map_b)))

    return new_image