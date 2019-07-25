
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/25/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-------------------------------
Implement Hough Line Transform
-------------------------------"""

from matplotlib import pyplot as plt
import numpy as np
import argparse
import math
import cv2

# ------------------ Do Hough Line Transform ------------------ #
def hough_line(edge):
    # Theta 0 - 180 degree
    # Calculate 'cos' and 'sin' value ahead to improve running time
    theta = np.arange(0, 180, 1)
    cos = np.cos(np.deg2rad(theta))
    sin = np.sin(np.deg2rad(theta))

    # Generate a accumulator matrix to store the values
    rho_range = round(math.sqrt(edge.shape[0]**2 + edge.shape[1]**2))
    accumulator = np.zeros((2 * rho_range, len(theta)), dtype=np.uint8)

    # Threshold to get edges pixel location (x,y)
    edge_pixels = np.where(edge == 255)
    coordinates = list(zip(edge_pixels[0], edge_pixels[1]))

    # Calculate rho value for each edge location (x,y) with all the theta range
    for p in range(len(coordinates)):
        for t in range(len(theta)):
            rho = int(round(coordinates[p][1] * cos[t] + coordinates[p][0] * sin[t]))
            accumulator[rho, t] += 2 # Suppose add 1 only, Just want to get clear result

    return accumulator

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # command line >> python hough_line_transform.py -i line.png
    # command line >> python hough_line_transform.py -i square.png

    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required = True, help = "Path to source image")
    args = vars(ap.parse_args())

    # read image then convert to grayscale and find the edges by Canny Edge Detection
    image = cv2.imread(args["image"])
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayscale,50,150)

    # Function to do hough line transform
    accumulator = hough_line(edges)

    # Threshold some high values then draw the line
    edge_pixels = np.where(accumulator > 110)
    coordinates = list(zip(edge_pixels[0], edge_pixels[1]))

    # Use line equation to draw detected line on an original image
    for i in range(0, len(coordinates)):
        a = np.cos(np.deg2rad(coordinates[i][1]))
        b = np.sin(np.deg2rad(coordinates[i][1]))
        x0 = a*coordinates[i][0]
        y0 = b*coordinates[i][0]
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),1)

    # show result
    plt.subplot(121), plt.imshow(image)
    plt.subplot(122), plt.imshow(accumulator)
    plt.show()
