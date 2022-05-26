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

def hist_equalize(image, histogram, size):
    map = equalize_map(histogram, size)
    new_image = image.point(lambda p : pxl_map_eq_hist(p, map))
    return new_image
