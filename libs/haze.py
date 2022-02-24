"""Single image dehazing."""
from __future__ import division
import cv2
import numpy as np
from datetime import datetime

class Channel_value:
    val = -1.0
    intensity = -1.0


def find_intensity_of_atmospheric_light(img, gray):
    start=datetime.now()
    top_num = int(img.shape[0] * img.shape[1] * 0.001)
    toplist = [Channel_value()] * top_num
    dark_channel = find_dark_channel(img)

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            val = img.item(y, x, dark_channel)
            intensity = gray.item(y, x)
            for t in toplist:
                if t.val < val or (t.val == val and t.intensity < intensity):
                    t.val = val
                    t.intensity = intensity
                    break

    max_channel = Channel_value()
    for t in toplist:
        if t.intensity > max_channel.intensity:
            max_channel = t
    print("find_intensity elapsed time", datetime.now()-start)
    return max_channel.intensity


def find_dark_channel(img):
    return np.unravel_index(np.argmin(img), img.shape)[2]


def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))


def dehaze(img, light_intensity, windowSize, t0, w):
    start=datetime.now()
    size = (img.shape[0], img.shape[1])

    outimg = np.zeros(img.shape, img.dtype)

    for y in range(size[0]):
        for x in range(size[1]):
            x_low = max(x-(windowSize//2), 0)
            y_low = max(y-(windowSize//2), 0)
            x_high = min(x+(windowSize//2), size[1])
            y_high = min(y+(windowSize//2), size[0])

            sliceimg = img[y_low:y_high, x_low:x_high]

            dark_channel = find_dark_channel(sliceimg)
            t = 1.0 - (w * img.item(y, x, dark_channel) / light_intensity)

            outimg.itemset((y,x,0), clamp(0, ((img.item(y,x,0) - light_intensity) / max(t, t0) + light_intensity), 255))
            outimg.itemset((y,x,1), clamp(0, ((img.item(y,x,1) - light_intensity) / max(t, t0) + light_intensity), 255))
            outimg.itemset((y,x,2), clamp(0, ((img.item(y,x,2) - light_intensity) / max(t, t0) + light_intensity), 255))
    print("dehaze elapsed time", datetime.now()-start)
    return outimg


def haze(img):# main()
    #imageName = '/home/ozan/Desktop/resler/train/1.jpg'  # eg. fg5.jpg
    #img = cv2.imread(imageName)
    #cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    light_intensity = find_intensity_of_atmospheric_light(img, gray)
    w = 0.95
    t0 = 0.45
    outimg = dehaze(img, light_intensity, 20, t0, w)
    return outimg
    #cv2.imshow("result",outimg)
    #if cv2.waitKey(0) & 0xFF ==ord('q'):
    #	pass

#if __name__ == "__main__": main()
