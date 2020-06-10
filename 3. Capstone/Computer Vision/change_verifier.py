# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:38:28 2020

@author: Fernando


# import sys
# if img_gray is None:
#     sys.exit("Could not read the image.")

print(img_gray.size)
print(img_gray.dtype)

"""

import cv2 as cv
import numpy as np

circle_size = 20

def get_coin_radius(circle):
    radius = []
    for coord in circle[0,:]:
        radius.append(coord[2])
    return radius

def get_brightness(img, coin, size):
    av_value = []
    for coord in coin[0, :]:
        col = np.mean(img[coord[1]-size:coord[1]+size,coord[0]-size:coord[0]+size])
        av_value.append(col)
    return av_value

def get_coin_value(brightness, radius):
    value_list = []
    for a,b in zip(brightness, radius):
        if a > 150 and b > 110:
            value_list.append(10)
        if a > 150 and b <= 110:
            value_list.append(5)
        if a < 150 and b > 110:
            value_list.append(2)
        if a < 150 and b <= 110:
            value_list.append(1)
    return value_list
    
def print_Onimage(img, c):
    count = 0
    for i in c[0,:]:
        # draw the outer circle
        cv.circle(img,(i[0],i[1]),i[2],(0,255,0),4)
        # draw the center of the circle
        cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
        # cv.putText(img_original, str(count), (i[0],i[1]), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2)
        cv.putText(img, str(values[count]) + 'p',(i[0],i[1]), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2)
        count += 1
    cv.putText(img, 'Estimated total value: ' + str(sum(values)) + 'p', (200, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (180,50,50), 2)


img_original = cv.imread("capstone_coins.png")
img_gray = cv.imread("capstone_coins.png",cv.IMREAD_GRAYSCALE)

img_gray = cv.GaussianBlur(img_gray, (5,5), 2,2)

circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 0.9, 120,
                param1=35,param2=45,minRadius=60,maxRadius=150)
circles = np.uint16(np.around(circles))


radius = get_coin_radius(circles)
brt = get_brightness(img_gray, circles, circle_size)
values = get_coin_value(brt, radius)
# print_Onimage(img_original,circles)

# cv.imshow("Display window", img_original)
# cv.waitKey(0)
# cv.destroyAllWindows()
    
#========== TRY 50 P


# thresh = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 1)
# kernel = np.ones((3, 3), np.uint8)
# closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=4)

# cont_img = closing.copy()
# contours, hierarchy = cv.findContours(cont_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
#     area = cv.contourArea(cnt)
#     ellipse = cv.fitEllipse(cnt)
#     cv.ellipse(img_gray, ellipse, (0,255,0), 2)
# cv.imshow('Contours', img_gray)

    